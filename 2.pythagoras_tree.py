"""
Pythagoras tree is a plane fractal constructed from squares. 
In this fractal, a square is successively divided into smaller squares.
The smallest squares are arranged in such a way that they form 
a right-angled triangle. The Pythagoras tree is named after 
the ancient Greek mathematician Pythagoras, who is best 
known for the Pythagorean theorem.

In this snippet, we will draw a Pythagoras tree using recursion.
The Pythagoras tree is constructed by starting with a square.
Two smaller squares are attached to the sides of the original square.
The process is repeated recursively for each new square.

The Pythagoras tree is a beautiful example of a fractal that
can be created using simple geometric rules and recursion.

Time complexity:
- draw_tree: O(2^n)
"""
import matplotlib.pyplot as plt
import numpy as np

def draw_tree(x: float, y: float, angle: float, length: float, level: int, ax: plt.Axes) -> None:
    """
    Function to draw a Pythagoras tree using recursion.

    :param x: float
    :param y: float
    :param angle: float
    :param length: float
    :param level: int
    :param ax: Axes

    :return: None

    Time complexity: O(2^n)
    """
    if level == 0:
        return

    # A new point for the end of the branch
    x_end = x + length * np.cos(np.radians(angle))
    y_end = y + length * np.sin(np.radians(angle))

    # Create a line from (x, y) to (x_end, y_end) using the Axes object
    ax.plot([x, x_end], [y, y_end], 'k-')

    # Calculate the new length of the branch
    new_length = length * np.sqrt(2) / 2

    # Left branch
    draw_tree(x_end, y_end, angle + 45, new_length, level - 1, ax)
    # Right branch
    draw_tree(x_end, y_end, angle - 45, new_length, level - 1, ax)

if __name__ == '__main__':
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')  # Turn off the axis for a cleaner plot

    level = int(input("Введіть рівень рекурсії: "))
    draw_tree(0, 0, 90, 10, level, ax)  # Start from the origin (0, 0) with an angle of 90 degrees and a length of 10
    plt.show()
