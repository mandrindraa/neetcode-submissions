class LinkedList:
    class Node:
        def __init__(self, val: int):
            self.val = val
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val

    def insertHead(self, val: int) -> None:
        node = LinkedList.Node(val)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = self.head
        self.size += 1

    def insertTail(self, val: int) -> None:
        node = LinkedList.Node(val)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.size -= 1
            return True
        cur = self.head
        for _ in range(index - 1):
            cur = cur.next
        cur.next = cur.next.next
        if cur.next is None:
            self.tail = cur
        self.size -= 1
        return True

    def getValues(self) -> list[int]:
        result = []
        cur = self.head
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result
        
