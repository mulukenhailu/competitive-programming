class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < self.length:
            i = 0
            ptr = self.head
            while ptr:
                if i == index:
                    return ptr.data
                i += 1
                ptr = ptr.next
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = new_node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        elif index < self.length:
            new_node = Node(val)
            ptr = self.head
            i = 0
            while ptr.next is not None:
                if i + 1 == index:
                    new_node.next = ptr.next
                    ptr.next = new_node
                    break
                i += 1
                ptr = ptr.next
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < self.length:
            if index == 0:
                self.head = self.head.next
            else:
                ptr = self.head
                i = 0
                while ptr.next is not None:
                    if i + 1 == index:
                        ptr.next = ptr.next.next
                        break
                    i += 1
                    ptr = ptr.next
            self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
