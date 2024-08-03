"""
Linked List
-----------

A linked list is a linear data structure where each element 
is a separate object. Each element is called a node and consists of two items: 
the data and a reference to the next node. 
The last node has a reference to None.

There are two types of linked lists:
1. Singly-linked list: Each node has a reference to the next node.
2. Doubly-linked list: Each node has a reference to the next and previous node.

Linked lists are used to implement other data structures like stacks, queues, and graphs.

In this snippet, we will implement the following functions:
1. Reverse a singly-linked list.
2. Merge two sorted linked lists.
3. Sort a linked list using merge sort.

Time complexity:
- Reverse a singly-linked list: O(n)
- Merge two sorted linked lists: O(n)
- Sort a linked list using merge sort: O(n log n)
"""
class ListNode:
    """
    Definition for singly-linked list.
    """
    def __init__(self, value=0, next=None):
        """
        Initialize the node with value and next pointer.

        :param value: int
        :param next: ListNode

        :return: None
        """
        self.value = value
        self.next = next

class LinkedList:
    """
    Definition for singly-linked list.
    """
    def __init__(self):
        """
        Initialize the head of the linked list.
        """
        self.head = None

def reverse_list(head: ListNode) -> ListNode:
    """
    Reverse a singly-linked list.

    :param head: ListNode

    :return: ListNode

    Time complexity: O(n)
    """
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def merge_sort(head: ListNode) -> ListNode:
    """
    Sort a singly-linked list using merge sort.

    :param head: ListNode

    :return: ListNode

    Time complexity: O(n log n)
    """
    if not head or not head.next:
        return head

    # Find the middle of the list
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    left = merge_sort(head)
    right = merge_sort(mid)

    return merge(left, right)


def merge(left: ListNode, right: ListNode) -> ListNode:
    """
    Merge two sorted linked lists.

    :param left: ListNode
    :param right: ListNode

    :return: ListNode

    Time complexity: O(n)
    """
    dummy = ListNode()
    tail = dummy

    while left and right:
        if left.value < right.value:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next

    tail.next = left if left else right
    return dummy.next

def merge_sorted_lists(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Merge two sorted linked lists.

    :param l1: ListNode
    :param l2: ListNode

    :return: ListNode

    Time complexity: O(n)
    """
    dummy = ListNode()
    current = dummy

    while l1 and l2:
        if l1.value < l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # Append the remaining nodes
    current.next = l1 if l1 else l2
    return dummy.next


def print_list(head: ListNode) -> None:
    """
    Print the linked list.

    :param head: ListNode

    :return: None
    """
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

if __name__ == "__main__":
    # Create a linked list
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    # Merge two sorted linked lists
    merged = merge_sorted_lists(l1, l2)
    print_list(merged)

    # Reverse a linked list
    reversed_list = reverse_list(merged)
    print_list(reversed_list)

    # Sort a linked list using merge sort
    sorted_list = merge_sort(reversed_list)
    print_list(sorted_list)
