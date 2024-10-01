# Define a Node class
class Node:
    def __init__(self, data):
        self.data = data  # Store data in the node
        self.children = []  # List to store child nodes

    # Add a child node to the current node
    def add_child(self, child_node):
        self.children.append(child_node)

# Build a tree
def build_tree():
    root = Node("Root")  # Create root node

    # Create children and grandchildren
    child1 = Node("Child 1")
    child2 = Node("Child 2")
    grandchild1 = Node("Grandchild 1.1")
    grandchild2 = Node("Grandchild 2.1")

    # Add grandchildren to respective children
    child1.add_child(grandchild1)
    child2.add_child(grandchild2)

    # Add children to the root node
    root.add_child(child1)
    root.add_child(child2)

    return root  # Return the root node with the tree

root_node = build_tree()  # Build the tree

