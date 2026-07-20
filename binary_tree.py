'''
Assignment

Complete the insert method of the BSTNode class. It takes a User object as input and adds it to a new node if the value doesn't already exist in the tree.

    If the node doesn't have a value yet, store the given value and return
    If the node's value is equal to the given value, just return, no duplicates allowed
    If the given value is less than the node's value and the node doesn't have a left child, create a new left child node with the given value and return
    If the given value is less than the node's value and the node does have a left child, recursively call insert off of that left child with the given value and return
    Since we already checked if the given value is equal to or less than the node, the value must be greater than the node. Handle whether or not the node already has a right child

Tip

I'd highly recommend using pencil/paper or some kind of drawing tool to visualize the tree as you go through the assignments in this chapter.
'''


# Import the Any type so the tree can store values of any data type
from typing import Any


# Define a class representing a single node in a Binary Search Tree (BST)
class BSTNode:

    def get_min(self) -> Any:
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self) -> Any:
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    # Constructor that creates a new node
    def __init__(self, val: Any = None) -> None:

        # Initialize the left child pointer as None (no left child yet)
        self.left: "BSTNode | None" = None

        # Initialize the right child pointer as None (no right child yet)
        self.right: "BSTNode | None" = None

        # Store the value of the node
        self.val = val

    # Method to insert a new value into the BST
    def insert(self, val: Any) -> None:

        # If the current node has no value, assign the new value to it
        if not self.val:
            self.val = val

            # Exit after inserting
            return

        # If the value already exists, do nothing (no duplicates allowed)
        elif self.val == val:
            return

        # If the new value is smaller and there is no left child,
        # create a new left child node
        elif val < self.val and not self.left:
            self.left = BSTNode(val)

        # If the new value is smaller and a left child exists,
        # recursively insert it into the left subtree
        elif val < self.val and self.left:
            self.left.insert(val)

            # Exit after the recursive insertion
            return

        # Otherwise, the value is greater than the current node,
        # so it belongs in the right subtree
        else:

            # If there is no right child, create one
            if not self.right:
                self.right = BSTNode(val)

                # Exit after inserting
                return

            # Otherwise, recursively insert into the right subtree
            else:
                self.right.insert(val)