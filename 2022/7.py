# Init of the dictionnary
myTree = {}


def build_tree(file):
    # To save the path of a file
    current_directory = []
    for i in file:
        if i[0] == '$':
            # Change directory
            if i[2:4] == "cd":
                if i[5] == '/':
                    # Add root to the tree
                    myTree.update({'/': {"weight": 0, "children": {}}})
                    current_directory.append('/')
                elif i[5:7] == "..":
                    # Come back in path
                    current_directory.pop()
                    current_directory.pop()
                else:
                    # Go to the directory
                    name_dir = get_name_dir(i)
                    current_directory.append("children")
                    current_directory.append(name_dir[1:])
        else:
            if i[0:3] == "dir":
                # Add the directory in the tree
                name_dir = get_name_dir(i)
                (get_element_from_tree(current_directory)["children"]).update(
                    {name_dir: {"weight": 0, "children": {}}})
            else:
                # Add the file in the tree
                name_file, weight = get_file(i)
                get_element_from_tree(current_directory).update(
                    {name_file: int(weight)})

# Get the directory name


def get_name_dir(line):
    length_dir = len(line)-len("dir \n")
    return line[4:4+length_dir]

# Get the name of the file and its weight


def get_file(line):
    end_weight = 0
    end_line = 0
    for i in range(len(line)):
        if line[i] == ' ':
            end_weight = i
        elif line[i] == '\n':
            end_line = i
    weight = line[:end_weight]
    name_file = line[end_weight+1:end_line]
    return name_file, weight

# Get the sub tree, giving a path


def get_element_from_tree(list_of_dir):
    current_tree = myTree
    for i in list_of_dir:
        current_tree = current_tree[i]
    return current_tree

# Set weight recursively


def set_weight(tree, somme, liste):
    total_weight = 0
    liste_values = tree.values()
    # Summing up all the weight of the file of the current directory
    for elt in liste_values:
        if type(elt) == int:
            total_weight += elt

    tree["weight"] += total_weight
    # In case, there is no directories in the current folder
    if tree["children"] == {}:
        # We refresh the sum that respect the condition
        somme += atmost_condition(total_weight)
        # We add the weight for part 2
        liste.append(total_weight)
        return total_weight, somme, liste
    else:
        all_keys = list(tree["children"].keys())
        # For all subdirectories, we set their weight and add it to the parent directory
        for i in range(len(tree["children"])):
            if all_keys[i] != "weight":
                res = set_weight(
                    tree["children"][all_keys[i]], somme, liste)
                tree["weight"] += res[0]
                somme = res[1]
        total_weight = tree["weight"]
        somme += atmost_condition(total_weight)
        liste.append(total_weight)
        return total_weight, somme, liste

# Set the condition of part 1


def atmost_condition(input):
    if input <= 100000:
        return input
    else:
        return 0


with open("inputs/7.txt", 'r') as file:
    lines = file.readlines()
    build_tree(lines)

somme_total = 0
total_poids = 0
list_poids = []
total_poids, somme_total, list_poids = set_weight(
    myTree['/'], somme_total, list_poids)

needed_space = 30000000
used_space = myTree["/"]["weight"]
size_to_find = used_space+needed_space - 70000000

# Filter all the weights according to the criteria
list_with_criteria = list(filter(lambda x: x >= size_to_find, list_poids))

print(f"La somme de tous les fichiers fait {somme_total}")

print(
    f"Needed space is {needed_space}, used space is {used_space}, we need to free at least {size_to_find}")

print(f"Minimum weight to erase is {min(list_with_criteria)}")

print(f"La somme de tous ces fichiers fait {somme_total}")
