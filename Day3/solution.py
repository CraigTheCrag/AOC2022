import functools
import operator

INPUT_FILE = "input.txt"

# Added space to offset indexes correctly.
priority_str = " abcdefghijklmnopqrstuvwyxzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def load_data(f: str) -> list:
    data_input = open(f, "r")
    
    return data_input.readlines()

def get_priority(c: chr) -> int:
    return priority_str.index(c)

def get_common_item(data: str) -> chr:
    half = len(data) // 2
    first_half, second_half = data[:half], data[half:]
    
    # Should only be 1 value left.
    common_value = set([*first_half]).intersection(set([*second_half]))
    return "".join(common_value)

def group_elves(data: list) -> list:
    new_list = []
    group_size = 3

    for i in range(0, len(data), group_size):
        new_list.append(data[i:i+group_size])

    return new_list

def get_common_between_many(data: list) -> chr:
    compound_set = set([*data[0].replace("\n", "")])

    for i in range(1, len(data)):
        compound_set = compound_set.intersection([*data[i].replace("\n", "")])

    return "".join(compound_set)


if __name__ == '__main__':
    data = load_data(INPUT_FILE)
    common_priorities = list(map(lambda x : get_priority(get_common_item(x)), data))
    print(sum(common_priorities))

    grouped_data = group_elves(data)

    common_amongst_group = list(map(lambda x: get_priority(get_common_between_many(x)), grouped_data))
    
    print(functools.reduce(operator.add, common_amongst_group))
