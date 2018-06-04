class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val, in_start=True):
        if self.lookup(val) != -1:
            return False

        if self.head is None:
            self.head = Node(val)
            return True

        if in_start:
            temp = self.head
            self.head = Node(val)
            self.head.next = temp
            temp.prev = self.head
            return True

        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(val)
        curr.next.prev = curr.next
        return True

    def insert_before(self, val, insert_before_val):
        if insert_before_val is None or self.lookup(insert_before_val) == -1:
            return False

        curr = self.head
        while curr.val != insert_before_val:
            curr = curr.next

        prev = curr.prev
        curr.prev = Node(val)
        curr.prev.next = curr
        curr.prev.prev = prev
        return True

    def insert_after(self, val, insert_after_val):
        if insert_after_val is None or self.lookup(insert_after_val) == -1:
            return False

        curr = self.head
        while curr.val != insert_after_val:
            curr = curr.next

        nxt = curr.next
        curr.next = Node(val)
        curr.next.prev = curr.next
        curr.next.next = nxt
        return True

    def lookup(self, val):
        curr = self.head
        result = -1
        while curr is not None:
            result += 1
            if curr.val == val:
                return result
            curr = curr.next

        return -1

    def remove(self, val):
        if self.lookup(val) == -1:
            return False

        curr = self.head
        if curr.val == val:
            self.head = curr.next
            del curr
            return True

        last = curr
        curr = curr.next
        while curr is not None:
            if curr.val == val:
                last.next = curr.next
                del curr
                return True
            curr = curr.next

    def size(self):
        return len(self.items)


class Node:
    def __init__(self, val=None, prev=None, nxt=None):
        self.val = val
        self.next = nxt
        self.prev = prev
