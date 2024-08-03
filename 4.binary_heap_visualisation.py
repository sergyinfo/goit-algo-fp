"""
A binary heap is a complete binary tree that satisfies the heap property.
The heap property states that for every node i, the value of i is greater than or equal to the value of its parent.
A binary heap can be represented as an array, where the parent of the node at index i is at index (i-1)/2.
The left child of the node at index i is at index 2*i+1, and the right child is at index 2*i+2.

In this snippet, we will implement a binary heap using a binary tree data structure.
We will also visualize the binary heap tree using NetworkX and Matplotlib.

Time complexity:
- add_edges: O(n)
- add_heap_node: O(n)
- build_heap: O(n)
- draw_tree: O(n)
"""
import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    """
    Class to represent a node in a binary heap.

    Attributes:
    - left: Node - left child of the node
    - right: Node - right child of the node
    - val: int - value of the node
    - color: str - color of the node
    - id: str - unique identifier of the node

    Methods:
    - __init__(key, color="skyblue"): initialize the node with a value and color

    Time complexity:
    - __init__: O(1)
    """
    def __init__(self, key: int, color: str = "skyblue") -> None:
        """
        Initialize the node with a value and color.

        :param key: int - value of the node
        :param color: str - color of the node

        :return: None

        Time complexity: O(1)
        """
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph: nx.DiGraph, node: Node, pos: dict, x: float = 0, y: float = 0, layer: int = 1):
    """
  Function to add edges to the binary heap tree.

    :param graph: nx.DiGraph - graph object to store the tree
    :param node: Node - the current node
    :param pos: dict - dictionary to store the position of the nodes
    :param x: float - x-coordinate of the node
    :param y: float - y-coordinate of the node
    :param layer: int - current layer of the tree

    :return: nx.DiGraph - graph object with edges added

    Time complexity: O(n)
    """
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def add_heap_node(arr: list, index: int) -> Node:
    """
    Function to add a node to a binary heap.

    :param arr: list - list of values to add to the heap
    :param index: int - index of the current node

    :return: Node - the root of the binary heap

    Time complexity: O(n)
    """
    node = Node(arr[index])
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < len(arr):
        node.left = add_heap_node(arr, left_index)
    if right_index < len(arr):
        node.right = add_heap_node(arr, right_index)
    return node

def build_heap(arr: list) -> Node:
    """
    Function to build a binary heap from a list of values.

    :param arr: list - list of values to add to the heap

    :return: Node - the root of the binary heap

    Time complexity: O(n)
    """
    return add_heap_node(arr, 0)

def draw_tree(tree_root):
    """
    Function to draw a binary heap tree using NetworkX and Matplotlib.

    :param tree_root: Node - the root of the binary heap tree

    :return: None

    Time complexity: O(n)
    """
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

if __name__ == "__main__":
    heap_values = [10, 4, 11, 12, 20, 15, 16]
    root = build_heap(heap_values)
    draw_tree(root)
