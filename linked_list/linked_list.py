class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val, insert_in_start=True):
        if self.lookup(val) != -1:
            # print('%s already exists in linked-list' % val)
            return False

        if self.head is None:
            self.head = Node(val)
            return True

        if insert_in_start:
            temp = self.head
            self.head = Node(val)
            self.head.next = temp
            return True

        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(val)
        return True

    def lookup(self, val):
        curr = self.head
        position = -1
        while curr is not None:
            position += 1
            if curr.val == val:
                return position
            curr = curr.next

        return -1

    def remove(self, val):
        if self.lookup(val) == -1:
            # print('%s doesn\'t exist in linked-list' % val)
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


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = None
