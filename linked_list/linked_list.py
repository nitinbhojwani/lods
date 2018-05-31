class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val, insert_in_start=True):
        if self.head is None:
            self.head = Node(val)
            return

        if insert_in_start:
            temp = self.head
            self.head = Node(val)
            self.head.next = temp
            return

        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(val)

    def look_up(self, val):
        curr = self.head
        result = -1
        while curr is not None:
            if curr.val == val:
                result += 1
                break
            curr = curr.next

        return result

    def remove(self, val):
        curr = self.head
        if curr.val == val:
            self.head = curr.next
            del curr
            return

        last = curr
        curr = curr.next
        while curr.val is not None:
            if curr.val == val:
                last.next = curr.next
                del curr
                return

    def size(self):
        return len(self.items)


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = None
