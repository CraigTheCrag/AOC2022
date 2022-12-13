import Node

INPUT_FILE = "input.txt"

def load_data(f: str) -> list:
    file = open(f, "r")

    return file.readlines()

def change_directory(root, target):
    if (target == "/"):
        return root
    elif (target == ".."):
        return root.find_node(Node.get_parent(target))
    return root.find_node(target)

if __name__ == "__main__":
    '''
    lines = load_data(INPUT_FILE)

    root = Node.Node("/", is_directory=True)
    current_node = root

    for line in lines:
        split_line = line.split(" ")
        if (split_line[0] == "$"):
            if (split_line[1] == "cd"):
                current_node = change_directory(root, split_line[2])
        elif (split_line[0] == "dir"):
            current_node.add_child(Node.Node(split_line[1], is_directory=True))
        else:
            current_node.add_child(Node.Node(split_line[1], size=int(split_line[0])))
    '''

    #Test Code:
    n = Node.Node("/", is_directory=True)
    n.add_child(Node.Node("a.txt", size=50))
    n.add_child(Node.Node("b.txt", size=20))
    n.add_child(Node.Node("directory", is_directory=True))

    b = n.find_node("b.txt")
    b.add_sibling(Node.Node("b_2.txt", size=30))

    directory = n.find_node("directory")
    directory.add_child(Node.Node("c.txt", size=100))

    print(Node.get_all_directory_sizes(n))

    print(Node.get_parent(n, "b.txt"))

    print(n.get_size())
    print(b.get_size())
    