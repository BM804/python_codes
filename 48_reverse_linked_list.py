"""Question 48: Reverse a singly linked list.

Write a function that reverses the links in a singly linked list and returns
the new head. The solution changes the links in place.
"""


class Node:
    """One item in a singly linked list."""

    def __init__(self, value: int, next_node: "Node | None" = None):
        self.value = value
        self.next = next_node


def reverse_list(head: Node | None) -> Node | None:
    """Reverse the list and return its new head.

    Runs in O(n) time and uses O(1) extra space.
    """
    previous = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous


def values_from(head: Node | None) -> list[int]:
    """Return the list values, useful for displaying the example."""
    values = []
    while head is not None:
        values.append(head.value)
        head = head.next
    return values


if __name__ == "__main__":
    head = Node(1, Node(2, Node(3)))
    print(values_from(reverse_list(head)))  # [3, 2, 1]
