INPUT_FILE = "input.txt"

def load_data(f: str) -> list:
    data_input = open(f, "r")
    
    return data_input.readlines()

def get_ranges(pair: str) -> list:
    pair = pair.replace("\n", "")
    split_pair = pair.split(",")
    ranges = []

    for i in range(len(split_pair)):
        ranges.append(list(map(lambda x : int(x), split_pair[i].split("-"))))

    return ranges

def do_overlap(pair: list, check_contain: bool = False) -> bool:
    first, second = pair[0], pair[1]

    if (check_contain):
        return (((first[0] <= second[0]) & (first[1] >= second[1])) | ((second[0] <= first[0]) & (second[1] >= first[1])))

    first_check = ((first[0] <= second[0]) & (first[1] >= second[0])) | ((first[0] <= second[1]) & (first[1] >= second[1]))
    second_check = ((second[0] <= first[0]) & (second[1] >= first[0])) | ((second[0] <= first[1]) & (second[1] >= first[1]))
    return (first_check | second_check)


def count_overlaps(pairs: list, check_contain: bool = False) -> int:
    count = 0
    for i in range(len(pairs)):
        if (check_contain):
            overlap = do_overlap(pairs[i], True)
        else:
            overlap = do_overlap(pairs[i])
        count += int(overlap)
    return count

if __name__ == "__main__":
    data = load_data(INPUT_FILE)
    ranges = list(map(get_ranges, data))
    print(count_overlaps(ranges, True))
    print(count_overlaps(ranges))