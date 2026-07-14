'''
Assignment

LockedIn uses a Queue to keep track of the order that recruiters should use to reach out to job seekers.

Implement the following operations on the Queue class:

    queue.push(item): Adds an item to the tail of the queue (index 0 of list)
    queue.pop(): Removes and returns an item from the head of the queue (last index of list)
    queue.peek(): Returns an item from the head of the queue
    queue.size(): Returns the number of items in the queue

Note: You'll often hear words used interchangeably in programming. For example, here we're saying push and pop, but enqueue and dequeue are also common words for the same ideas.
term 1 	term 2 	description
Push 	Enqueue 	Adds an item to the tail of the queue
Pop 	Dequeue 	Removes and returns an item from the head of the queue

Tips
The underlying data type we're using is just a List. Don't forget to guard against IndexErrors by returning 'None' if the queue is empty.
The .insert List method may be helpful.

It's important to understand what a queue is and how it works. 
A queue is data structure that follows the First In First Out (FIFO) principle. 
The first item added to the queue will be the first one to be removed. 
Think of it like a line of people waiting for a service; the person who arrives first is served first.
That means, if we want to push (add) an item to the queue we use the append method to add an item to the end of the list.
Don't assign an item to the last index -1 self.items[-1] of the list, that's not adding, that's overwriting the last item in the list.
And if we want to pop (remove) an item from the queue we do it from the front of the list index 0. del(self.items[0])
'''

from typing import Any


class Queue:
    def __init__(self) -> None:
        self.items: list[Any] = []

    def is_empty(self) -> int:
        return len(self.items) == 0
    
    def push(self, item: Any) -> None:
        self.items.append(item)
        return None

    def pop(self) -> Any:
        if self.is_empty():
            return None
        tmp_item = self.items[0]
        del(self.items[0])
        return tmp_item

    def peek(self) -> Any:
        if self.is_empty():
            return None
        return self.items[0]

    def size(self) -> int:
        return len(self.items)