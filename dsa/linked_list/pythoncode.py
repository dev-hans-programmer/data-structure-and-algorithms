from typing import Self
from dataclasses import dataclass


@dataclass
class Node:
    data: int
    next: Self | None = None


class Sll:
    def __init__(self) -> None:
        self.start: Node | None = None

    def is_empty(self):
        return self.start is None

    def prepend(self, data: int):
        new_node = Node(data)

        new_node.next = self.start
        self.start = new_node

    def append(self, data: int):
        if self.is_empty():
            self.prepend(data)
        else:
            n = Node(data)
            temp = self.start

            while temp and temp.next is not None:
                temp = temp.next
            if temp:
                temp.next = n

    def search(self, item: int):
        if self.is_empty():
            raise ValueError("List is empty")
        temp = self.start

        while temp:
            if temp.data == item:
                return temp
            temp = temp.next
        print("Value not found")

    def del_first(self):
        if self.is_empty():
            raise ValueError("No node present to delete")

        if self.start:
            self.start = self.start.next

    def del_last(self):
        if self.is_empty():
            raise ValueError("No node present to delete")
        # Single Node
        if self.start and self.start.next is None:
            self.start = None
            return
        current = self.start

        while current and current.next and current.next.next:
            current = current.next
        if current:
            current.next = None

    def display(self):
        if not self.is_empty() and self.start:
            temp = self.start

            while temp.next is not None:
                print(f"{temp.data} -> ", end=" ")
                temp = temp.next
            print(temp.data)


def test_sll():
    sll = Sll()
    sll.prepend(20)
    sll.prepend(10)
    sll.prepend(5)
    sll.append(30)
    sll.append(40)
    sll.prepend(1)
    sll.append(60)
    sll.del_first()
    sll.del_first()
    sll.del_last()
    sll.del_last()
    sll.display()
    # sll.search(40)


test_sll()
