# https://leetcode.cn/problems/design-linked-list/description/
# 2023.9.21(7th)
# 2026.8.11(8th)

import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# class ListNode():
#     def __init__(self, val = 0, next = None) -> None:
#         self.val = val
#         self.next = next
    
# class MyLinkedList():
#     def __init__(self) -> None:
#         self.len = 0
#         self.dummy = ListNode(0)

#     def get(self, index: int) -> int:
#         if index >= self.len:
#             return -1

#         cur = self.dummy
#         while index:
#             cur = cur.next
#             index -= 1
#         return cur.next.val
    
#     def addAtHead(self, val: int):
#         self.addAtIndex(0, val)
        
#     def addAtTail(self, val: int):
#         self.addAtIndex(self.len, val)

#     def addAtIndex(self, index: int, val: int):
          # 不是>=，因为可以在最后面加
#         if index > self.len:
#             return -1
        
#         cur = self.dummy
#         to_add = ListNode(val)
#         while index:
#             cur = cur.next
#             index -= 1
#         next = cur.next
#         cur.next = to_add
#         to_add.next = next
#         self.len += 1

#         return self.dummy.next
    
#     def deleteAtIndex(self, index: int):
#         if index >= self.len:
#             return -1
        
#         cur = self.dummy
#         while index:
#             cur = cur.next
#             index -= 1
#         cur.next = cur.next.next
#         self.len -= 1

#         return self.dummy.next

class ListNode():
    def __init__(self, val= 0, next = None):
        self.val = val
        self.next = next

class MyLinkedLists():
    def __init__(self): # 是链表对象自己的属性，不需要外部传入
        self.len = 0
        self.dummy = ListNode(0)

    def get(self, index: int):
        if index >= self.len:
            return -1
        
        cur = self.dummy
        while index:
            cur = cur.next
            index -= 1
        
        return cur.next.val

    def addAtHead(self, val: int):
        self.addAtIndex(0, val)

    def addAtTail(self, val: int):
        self.addAtIndex(self.len, val)

    def addAtIndex(self, index: int, val: int):
        if index > self.len:
            return -1
        
        to_add = ListNode(val)
        cur = self.dummy
        while index:
            cur = cur.next
            index -= 1
        next = cur.next
        to_add.next = next
        cur.next = to_add

        self.len += 1 # 🔥🔥🔥

        return self.dummy.next


    def deleteAtIndex(self, index: int, val: int):
        if index >= self.len:
            return -1

        cur = self.dummy
        while index:
            cur = cur.next
            index -= 1
        cur.next = cur.next.next

        self.len -= 1 # 🔥🔥🔥

        return self.dummy.next
        