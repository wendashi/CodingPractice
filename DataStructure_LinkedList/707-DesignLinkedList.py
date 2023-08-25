class ListNode():
    def __init__(self, val = 0 , next = None):
        self.val = val
        self.next = next

class MyLinkedList():
    def __init__(self):
        self.size = 0
        self.dummyhead = ListNode(0)

    def get(self, index:int):
        if index < 0 or index >= self.size:
            return -1
        cur = self.dummyhead

        for _ in range(index+1):
           cur = cur.next
        return cur.val
    
    def addAtHead(self, val:int):
        self.addAtIndex(0 , val)

    def addAtTail(self, val:int):
        self.addAtIndex(index = self.size, val = val)

    def addAtIndex(self, index:int, val:int):
        if index < 0 or index > self.size:
            return -1
        
        cur = self.dummyhead

        for _ in range(index):
           cur = cur.next
        cur.next = ListNode(val, cur.next)
        self.size += 1

    def deleteAtIndex(self, index:int):
        if index < 0 or index >= self.size:
            return -1

        cur = self.dummyhead

        for _ in range(index):
           cur = cur.next

        cur.next = cur.next.next
        self.size -= 1

def print_ll(head):
    if head is None:
        return -1
    cur = head
    while cur is not None:
        print(cur.val, end = '->')
        cur = cur.next


obj = MyLinkedList()
obj.addAtHead(1)
print_ll(obj.dummyhead.next)
print('\n---')
obj.addAtTail(3)
print_ll(obj.dummyhead.next)
print('\n---')
obj.addAtIndex(1,2)
print_ll(obj.dummyhead.next)
print('\n---')
obj.get(1)
obj.deleteAtIndex(1)
print_ll(obj.dummyhead.next)
print('\n---')
obj.get(1)


        