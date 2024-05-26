#!/usr/bin/python3
"""This module contains singly linked list"""


class Node:
    """Node class represents each element in the linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a Node with data and a reference to the next node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method for data."""
        return self._data

    @data.setter
    def data(self, value):
        """Setter method for data."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """Getter method for next_node."""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method for next_node."""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """SinglyLinkedList represents a singly linked list."""

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.head = None

    def sorted_insert(self, value):
        """Insert a value into the linked list in sorted order."""
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Return a string representation of the linked list."""
        lines = []
        current = self.head
        while current:
            lines.append(str(current.data))
            current = current.next_node
        return "\n".join(lines)
