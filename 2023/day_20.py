"""This is day 20 of advent of code 2023"""
from queue import Queue
from math import lcm
from copy import deepcopy
from utils.file import list_lines

with open(file="inputs/day_20.txt", mode='r', encoding="utf-8") as f:
    all_lines = list_lines(f)

#High pic = True
#Low pic = False

class Module:
    """A class to define a Module"""
    def __init__(self) -> None:
        pass

    def excited(self, s_in: bool, input_module: str):
        """The response of this module according to the input"""

class Flipflop(Module):
    """A class to describe the behavior of a flipflop module"""
    def __init__(self, module_id, outputs):
        self.value = False
        self.id = module_id
        self.outputs = outputs

    def excited(self, s_in: bool, input_module = None):
        """The response of this module according to the input"""
        # flipflop on and low pulse
        if self.value and not s_in:
            self.value = not self.value
            # Return a low pulse and list of outputs
            return s_in, self.outputs
        # flipflop off and low pulse
        if not self.value and not s_in:
            self.value = not self.value
            # Return a high pulse and list of outputs
            return not s_in, self.outputs
        return None, None

class Conjunction(Module):
    """A class to describe the behavior of a conjunction module"""
    def __init__(self, module_id, inputs, outputs):
        self.inputs: dict[str, bool] = {}
        self.id = module_id
        # Initialise all inputs values to low pulse (False)
        for init_input in inputs:
            self.inputs[init_input] = False
        self.outputs = outputs

    def excited(self, s_in, input_module):
        """The response of this module according to the input"""
        # Update the memory
        self.inputs[input_module] = s_in
        # Emit a low pulse if there are all high pulse
        if len(set(self.inputs.values())) == 1 and s_in:
            # Return the opposite signal
            return not s_in, self.outputs
        # Otherwise, it sends a high pulse
        return True, self.outputs

class Broadcaster(Module):
    """A class to describe the behavior of a broadcaster module"""
    def __init__(self, outputs):
        self.outputs = outputs

    def excited(self, s_in, input_module = None):
        """The response of this module according to the input"""
        return s_in, self.outputs


modules: dict[str, Module] = {}
# creation of flipflop modules
for line in all_lines:
    if line[0] == '%':
        label, values = line[1:].split(' -> ')
        values = values.split(', ')
        modules[label] = Flipflop(label, values)
    elif line[:11] == 'broadcaster':
        _, values = line.split(' -> ')
        values = values.split(', ')
        modules['broadcaster'] = Broadcaster(values)
    elif line[0] == '&':
        # Conjuction module
        conj_label, outputs_label = line[1:].split(' -> ')
        outputs_label = outputs_label.split(', ')
        inputs_modules = []
        for module in all_lines:
            label, module_outputs = module[1:].split(' -> ')
            module_outputs = module_outputs.split(', ')
            if conj_label in module_outputs:
                if label == 'broadcaster':
                    inputs_modules.append('broadcaster')
                else:
                    inputs_modules.append(label)
        modules[conj_label] = Conjunction(conj_label, inputs_modules, outputs_label)

modules_part2 = deepcopy(modules)

def part_1(all_modules: dict[str, Module]):
    """Print the answer of part 1"""
    count_high_pulse = 0
    count_low_pulse = 0
    nb_click = 1000
    for _ in range(nb_click):
        init_signal = False #Low pic
        # Data structure : origin, signal, module
        pulse_queue = Queue()
        pulse_queue.put(['button', init_signal, 'broadcaster'])
        while not pulse_queue.empty():
            origin, signal_in, dest_module = pulse_queue.get()
            # Count high pulse
            if signal_in:
                count_high_pulse += 1
            elif not signal_in:
                count_low_pulse += 1
            # Check if the destination module exists
            if dest_module not in all_modules:
                continue
            current_module = all_modules[dest_module]
            signal_out, outputs_modules = current_module.excited(signal_in, origin)
            if signal_out is not None:
                # If a signal is emitted we add it to the queue
                for out_module in outputs_modules:
                    pulse_queue.put([dest_module, signal_out, out_module])

    print(f"The total score is {count_low_pulse*count_high_pulse}")

def part_2(all_modules: dict[str, Module]):
    """Print the answer of part 2"""
    total_clicks = []
    origin_clicks = []
    count_click = 0
    # Check the number of count found for the 4 pools
    while len(total_clicks) != 4:
        count_click +=1
        init_signal = False #Low pic
        # Data structure : origin, signal, module
        pulse_queue = Queue()
        pulse_queue.put(['button', init_signal, 'broadcaster'])
        while not pulse_queue.empty():
            origin, signal_in, dest_module = pulse_queue.get()
            # 'qn' is the conjunctive parent of 'rx'
            if dest_module == 'rx':
                continue
            current_module = all_modules[dest_module]
            if 'rx' in current_module.outputs and signal_in and origin not in origin_clicks:
                origin_clicks.append(origin)
                total_clicks.append(count_click)
            signal_out, outputs_modules = current_module.excited(signal_in, origin)
            if signal_out is not None:
                # If a signal is emitted we add it to the queue
                for out_module in outputs_modules:
                    pulse_queue.put([dest_module, signal_out, out_module])
    total_clicks = list(map(lambda x: x, total_clicks))
    print(f"The minimum number of button presses to deliver a single low pulse to rx is {lcm(*total_clicks)}")

# Run part 1
part_1(modules)

# Run part 2
part_2(modules_part2)
