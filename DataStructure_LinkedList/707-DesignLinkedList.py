# class ListNode():
#     def __init__(self, val = 0 , next = None):
#         self.val = val
#         self.next = next

# class MyLinkedList():
#     def __init__(self):
#         self.size = 0
#         self.dummyhead = ListNode(0)

#     def get(self, index:int):
#         if index < 0 or index >= self.size:
#             return -1
#         cur = self.dummyhead

#         for _ in range(index+1):
#            cur = cur.next
#         return cur.val
    
#     def addAtHead(self, val:int):
#         self.addAtIndex(0 , val)

#     def addAtTail(self, val:int):
#         self.addAtIndex(index = self.size, val = val)

#     def addAtIndex(self, index:int, val:int):
#         if index < 0 or index > self.size:
#             return -1
        
#         cur = self.dummyhead

#         for _ in range(index):
#            cur = cur.next
#         cur.next = ListNode(val, cur.next)
#         self.size += 1

#     def deleteAtIndex(self, index:int):
#         if index < 0 or index >= self.size:
#             return -1

#         cur = self.dummyhead

#         for _ in range(index):
#            cur = cur.next

#         cur.next = cur.next.next
#         self.size -= 1

# def print_ll(head):
#     if head is None:
#         return -1
#     cur = head
#     while cur is not None:
#         print(cur.val, end = '->')
#         cur = cur.next


# obj = MyLinkedList()
# obj.addAtHead(1)
# print_ll(obj.dummyhead.next)
# print('\n---')
# obj.addAtTail(3)
# print_ll(obj.dummyhead.next)
# print('\n---')
# obj.addAtIndex(1,2)
# print_ll(obj.dummyhead.next)
# print('\n---')
# obj.get(1)
# obj.deleteAtIndex(1)
# print_ll(obj.dummyhead.next)
# print('\n---')
# obj.get(1)

# 2023.9.19（6th）

class ListNode():
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class MyLinkedList():
    def __init__(self) -> None:
        self.len = 0
        self.dummy = ListNode(0)

    def get(self, x: int):
        if x >= self.len or x < 0: # x 是下标
            return -1
        
        cur = self.dummy

        for _ in range(x + 1):
            cur = cur.next
        
        return cur.val
    
    def addAtHead(self, v: int):
        self.addAtIndex(0, v)

    def addAtTail(self, v: int):
        self.addAtIndex(self.len, v)
    
    def addAtIndex(self, x:int, v:int):
        if x > self.len:
            return None
        
        to_add = ListNode(val = v)
        cur = self.dummy
        for _ in range(x):
            cur = cur.next
        cur.next = ListNode(v, cur.next) # 在 cur 和 cur.next 中间插一个值！
        
        self.len += 1

        return self.dummy.next

    def deleteAtIndex(self, x: int):
        if x >= self.len:
            return None
        
        cur = self.dummy
        for _ in range(x):
            cur = cur.next
        cur.next = cur.next.next  
        self.len -= 1          

        return self.dummy.next

    
def printll(head):
    cur = head
    while cur: 
        print(cur.val, end = '->')
        cur = cur.next

    return print('None')


myll = MyLinkedList()
h1 = myll.addAtHead(1)
printll(h1)

h2 = myll.addAtTail(3)
printll(h2)

h3 = myll.addAtIndex(1, 2)
printll(h3)

h4 = myll.get(1)
print(h4)

h5 = myll.deleteAtIndex(1)
printll(h5)

h6 = myll.get(1)
print(h6)

