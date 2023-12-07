"""This is day 5 of advent of code 2023"""
from utils.file import list_lines

with open(file="inputs/day_5.txt", mode='r', encoding="utf-8") as f:
    all_lines = list_lines(f)

seeds = all_lines[0][7:].split(" ")
seeds = set(map(int, seeds))


class SourceDest:
    """ A class to create conversion table and possibility to convert given seeds"""
    def __init__(self, lines):
        table = map(lambda x: x.split(" "), lines)
        self.table = set(map(lambda x: tuple([int(y) for y in x]), table))

    def convert(self, sources):
        """Convert given seeds"""
        destination = set()
        for source in sources:
            compat = set(filter(lambda x: x[1] <= source and source <= x[1] + x[2] - 1, self.table))
            if len(compat) == 0:
                destination.add(source)
            else:
                transfer = compat.pop()
                shift = source - transfer[1]
                destination.add(transfer[0] + shift)
        return destination


    def convert_with_range(self, sources_with_range: set[int, int]):
        """Convert given seeds with their range"""
        destination_with_range = set()
        for source, range_source in sources_with_range:
            source_begin = set(
                filter(
                    lambda x: x[1] <= source and source <= x[1] +
                    x[2] -
                    1,
                    self.table))
            source_end = set(
                filter(
                    lambda x: x[1] <= source +
                    range_source -
                    1 and source +
                    range_source -
                    1 <= x[1] +
                    x[2] -
                    1,
                    self.table))
            if source_begin == source_end:
                if len(source_begin) == 0:
                    # outside every table or range inside
                    inside_table = None
                    for tables in self.table:
                        if source <= tables[1] and source + range_source -1 >= tables[1] + tables[2] - 1:
                            if inside_table is None:
                                inside_table = tables
                            else:
                                if tables[1] <= inside_table[1]:
                                    inside_table = tables
                            
                    if inside_table is not None:
                        destination_with_range.add((source, inside_table[1]-source))
                        print((source, inside_table[1]-source))
                        other_dest = self.convert_with_range({(inside_table[1], range_source -(inside_table[1]-source))})
                        for dest_range in other_dest:
                            destination_with_range.add(dest_range)
                            print(dest_range)

                    else:
                        destination_with_range.add((source, range_source))

                else:
                    # all inside a table
                    transfer = source_begin.pop()
                    destination_with_range.add((transfer[0] + (source - transfer[1]), range_source))
                    print(transfer[0] + (source - transfer[1]), range_source)
            else:
                if len(source_begin) == 0:
                    # only end inside a table
                    transfer_end = source_end.pop()
                    end_source = source + range_source - 1
                    shift = end_source - transfer_end[1]
                    destination_with_range.add((transfer_end[0], shift+1))
                    new_sources_with_range = {(source, range_source - shift -1)}
                else:
                    # start and end inside different table
                    transfer = source_begin.pop()
                    shift = source - transfer[1]
                    destination_with_range.add((transfer[0] + shift, transfer[2] - shift))
                    new_sources_with_range = {(transfer[1] + transfer[2], range_source - transfer[2] + shift)}
                print(new_sources_with_range)
                other_dest = self.convert_with_range(new_sources_with_range)

                for dest_range in other_dest:
                    destination_with_range.add(dest_range)
        return destination_with_range


seed2soil = SourceDest(all_lines[3:40])
soil2fertilizer = SourceDest(all_lines[42:52])
fertilizer2water = SourceDest(all_lines[54:90])
water2light = SourceDest(all_lines[92:138])
light2temperature = SourceDest(all_lines[140:168])
temperature2humidity = SourceDest(all_lines[170:210])
humidity2location = SourceDest(all_lines[212:254])

list_conversion = [
    seed2soil,
    soil2fertilizer,
    fertilizer2water,
    water2light,
    light2temperature,
    temperature2humidity,
    humidity2location]

# Part 1
converted = seeds
for tables in list_conversion:
    converted = tables.convert(converted)

print(f"The minimum value after conversion is {min(converted)}")

# Part 2
new_seeds = all_lines[0][7:].split(" ")
new_seeds = list(map(int, seeds))
all_new_seeds = set()

for range_seed, seed in zip(new_seeds[::2], new_seeds[1::2]):
    all_new_seeds.add((seed, range_seed))

converted_elt = all_new_seeds
for tables in list_conversion:
    converted_elt = tables.convert_with_range(converted_elt)

init_elt = [x[0] for x in converted_elt if x[0]!=0]
print(converted_elt)
print(f"The minimum value after conversion is {min(init_elt)}")
