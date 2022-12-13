INPUT_FILE = "input.txt"

stack_list = [
    [], # Add blank element at index 0 to line indexes up with input.
    ["D","H", "N", "Q", "T", "W", "V", "B"],
    ["D", "W", "B"],
    ["T", "S", "Q", "W", "J", "C"],
    ["F", "J", "R", "N", "Z", "T", "P"],
    ["G", "P", "V", "J", "M", "S", "T"],
    ["B", "W", "F", "T", "N"],
    ["B", "L", "D", "Q", "F", "H", "V", "N"],
    ["H", "P", "F", "R"],
    ["Z", "S", "M", "B", "L", "N", "P", "H"]
]

def load_data(f: str) -> list:
    data_input = open(f, "r")
    
    return data_input.readlines()

def parse_nums(lines: list) -> list:
    parsed = []

    for line in lines:
        split = line.split(" ")
        move = []
        move.append(int(split[1]))
        move.append(int(split[3]))
        move.append(int(split[5]))
        parsed.append(move)
    return parsed

def move_crates(movements: list, stacks: list) -> list:
    for movement in movements:
        crates_to_move = []
        for i in range(movement[0]):
            crates_to_move.append(stacks[movement[1]].pop())

        stacks[movement[2]].extend(crates_to_move[::-1])
    return stacks

if __name__ == "__main__":
    data = load_data(INPUT_FILE)

    movements = parse_nums(data)

    ending = move_crates(movements, stack_list)

    for i in range(1, len(ending)):
        print(ending[i][len(ending[i])-1])