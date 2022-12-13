class Node:
    def __init__(self,  name: str,
    first_child = None,
    sibling = None,
    size: int = 0,
    is_directory: bool = False) -> None:

        self.name = name
        self.first_child = first_child
        self.sibling = sibling
        self.is_directory = is_directory
        if (self.is_directory):
            self.size = 0
        else:
            self.size = size
    
    def get_size(self):
        sum = self.size

        if (self.first_child != None):
            sum += self.first_child.get_size()

        if (self.sibling != None):
            sum += self.sibling.get_size()

        return sum

    def add_child(self, child):
        if (self.first_child == child.name):
            return
        if (self.first_child != None):
            self.first_child.add_sibling(child)
        else:
            self.first_child = child

    def add_sibling(self, sibling):
        if (self.name == sibling.name):
            return
        if (self.sibling != None):
            self.sibling.add_sibling(sibling)
        else:
            self.sibling = sibling

    def find_node(self, name: str):
        if (self.name == name):
            return self

        if (self.first_child != None):
            returned_val = self.first_child.find_node(name)
            if (returned_val != None):
                return returned_val

        if (self.sibling != None):
            returned_val = self.sibling.find_node(name)
            if (returned_val != None):
                return returned_val

        return None
        
def get_parent(node: Node, child: str, parent: str = None) -> str:
    if (node is None):
        return None

    if (node.name == child):
        return parent
    else:
        returned_val = get_parent(node.first_child, child, node.name)
        if (returned_val != None):
            return returned_val
        return get_parent(node.sibling, child, parent)
        
def get_all_directory_sizes(node: Node, sizes={}):
    if (node.is_directory):
        sizes[node.name] = node.get_size()

    if (node.first_child != None):
        sizes = get_all_directory_sizes(node.first_child, sizes)
    
    if (node.sibling != None):
        sizes = get_all_directory_sizes(node.sibling, sizes)

    return sizes
        
    
