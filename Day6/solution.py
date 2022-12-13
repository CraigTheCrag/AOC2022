INPUT_FILE = "input.txt"

def get_start_of_packet_index(f: str, marker_size: int) -> int:
    marker_start_index = 0
    current_chars = f[marker_start_index:marker_start_index+marker_size]

    while (len(current_chars) != len(set(current_chars))):
        marker_start_index += 1
        current_chars = f[marker_start_index:marker_start_index+marker_size]

    return marker_start_index + marker_size

def load_data(f: str) -> str:
    data_input = open(f, "r")
    
    return data_input.readlines()[0]

if __name__ == "__main__":
    data = load_data(INPUT_FILE)
    index = get_start_of_packet_index(data, 4)
    print(index)
    index = get_start_of_packet_index(data, 14)
    print(index)