"""
Task:
- Implement Depth First Search (DFS) and Breadth First Search (BFS) algorithms for a binary tree.
- Visualize the traversal of the binary tree using NetworkX and Matplotlib.
- Use different colors to represent the order of traversal.
"""
import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

class Node:
    """
    Class to represent a node in a binary tree.

    Attributes:
    - left: Node - left child of the node
    - right: Node - right child of the node
    - val: int - value of the node
    - color: str - color of the node
    - id: str - unique identifier of the node

    Methods:
    - __init__(key): initialize the node with a value

    Time complexity:
    - __init__: O(1)
    """
    def __init__(self, key: int) -> None:
        """
        Initialize the node with a value.

        :param key: int - value of the node

        :return: None

        Time complexity: O(1)
        """
        self.left = None
        self.right = None
        self.val = key
        self.color = "#FFFFFF"  # White color by default
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
    if node:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

def draw_tree(tree_root):
    """
    Function to draw a binary heap tree using NetworkX and Matplotlib.

    :param tree_root: Node - the root of the binary heap tree

    :return: None

    Time complexity: O(n)
    """
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=3000, node_color=colors)
    plt.show()

def generate_colors(n: int) -> list:
    """
    Function to generate a list of n colors using a colormap.

    :param n: int - number of colors to generate

    :return: list - list of n colors

    Time complexity: O(n)
    """
    cmap = plt.cm.Blues  # Uses colormap Blues for color generation
    return [mcolors.rgb2hex(cmap(i)) for i in np.linspace(0, 1, n)]

def update_colors(node: Node, color_map: list, order: list) -> None:
    """
    Function to update the colors of the nodes in the tree.

    :param node: Node - the current node
    :param color_map: list - list of colors
    :param order: list - order of the nodes

    :return: None

    Time complexity: O(n)
    """
    if node:
        node.color = color_map[order.index(node.id)]
        update_colors(node.left, color_map, order)
        update_colors(node.right, color_map, order)

def dfs(node: Node, visited: list = None) -> list:
    """
    Function to perform Depth First Search (DFS) on a binary tree.

    :param node: Node - the current node
    :param visited: list - list to store visited nodes

    :return: list - list of visited nodes

    Time complexity
    - Worst-case: O(n)
    - Best-case: O(1)
    """
    if visited is None:
        visited = []
    if node:
        visited.append(node.id)
        dfs(node.left, visited)
        dfs(node.right, visited)
    return visited

def bfs(node: Node):
    """
    Function to perform Breadth First Search (BFS) on a binary tree.

    :param node: Node - the root node of the tree

    :return: list - list of visited nodes

    Time complexity
    - Worst-case: O(n)
    - Best-case: O(1)
    """
    queue = [node]
    visited = []
    while queue:
        current = queue.pop(0)
        if current:
            visited.append(current.id)
            queue.append(current.left)
            queue.append(current.right)
    return visited

if __name__ == "__main__":
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    root.right.right = Node(2)

    dfs_order = dfs(root)
    bfs_order = bfs(root)
    colors_dfs = generate_colors(len(dfs_order))
    colors_bfs = generate_colors(len(bfs_order))

    # Візуалізація DFS
    update_colors(root, colors_dfs, dfs_order)
    draw_tree(root)

    # Візуалізація BFS
    update_colors(root, colors_bfs, bfs_order)
    draw_tree(root)
