from typing import Any

class LLQueue:
    def remove_from_head(self) -> Node | None:
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        temp.set_next(None)
        return temp

    # don't touch below this line

    def add_to_tail(self, node: Node) -> None:
        if self.tail is None:
            self.head = node
            self.tail = node
            return
        assert self.tail is not None
        self.tail.set_next(node)
        self.tail = node

    def __init__(self) -> None:
        self.tail: Node | None = None
        self.head: Node | None = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " <- ".join(nodes)

class Node:
    def __init__(self, val: Any) -> None:
        self.val = val
        self.next: "Node | None" = None

    def set_next(self, node: "Node | None") -> None:
        self.next = node

    def __repr__(self) -> str:
        return self.val

