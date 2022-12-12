INPUT_FILE = "input.txt"

def load_data(f: str):
    data_input = open(INPUT_FILE, "r")
    current_sum = 0
    sums = []

    for line in data_input:
        if line == "\n":
            sums.append(current_sum)
            current_sum = 0
        else:
            current_sum += int(line.replace("\n", ""))

    data_input.close()
    return sums



if __name__ == "__main__":
    sorted_list = load_data(INPUT_FILE)
    sorted_list.sort()

    print(str(sorted_list[-1]) + "\n")

    top3_sum = sum(sorted_list[-3::1])    
    print(top3_sum)



