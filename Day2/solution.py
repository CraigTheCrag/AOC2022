INPUT_FILE = "input.txt"

# Format:
# Key = My Choice
# Value = Tuple:
#   1. Score of my choice (i.e. X scores 1)
#   2. Value that my choice beats (i.e. X beats C)
#   3. Value that my choice draws (i.e. X draws with A)
combinations = {
    "X": [1, "C", "A"],
    "Y": [2, "A", "B"],
    "Z": [3, "B", "C"]
}

def load_data(f: str) -> list:
    data_input = open(f, "r")
    
    return data_input.readlines()

def calculate_wrong_score(data: list) -> int:
    total = 0
    for line in data:
        split_data = line.replace("\n", "").split(" ")
        theirs = split_data[0]
        my_entry = combinations[split_data[1]]
        total += my_entry[0]

        if (my_entry[1] == theirs):
            total += 6
        elif (my_entry[2] == theirs):
            total += 3
    return total

match_fixing_scores = {
    "X": {"A": 3, "B": 1, "C": 2},
    "Y": {"A": 4, "B": 5, "C": 6},
    "Z": {"A": 8, "B": 9, "C": 7}
}

def calculate_correct_score(data: list) -> int:
    total = 0
    for line in data:
        split_data = line.replace("\n", "").split(" ")
        theirs = split_data[0]
        outcome = split_data[1]

        total += match_fixing_scores[outcome][theirs]
    return total

if __name__ == '__main__':
    data = load_data(INPUT_FILE)

    total = calculate_wrong_score(data)
    print(total)

    total = calculate_correct_score(data)
    print(total)
