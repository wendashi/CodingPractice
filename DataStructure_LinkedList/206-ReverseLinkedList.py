# class ListNode():
#     def __init__(self, val = 0, next = None):
#         self.val = val
#         self.next = next

# class Solution():
#     def ReverseLinkedList(self, head):
#         # if head is None or head.next is None:
#         #     return head
        
#         # res = self.ReverseLinkedList(head.next)
#         # head.next.next = head
#         # head.next = None
#         # return res
#         pre, cur = None, head
#         while cur:
#             next = cur.next
#             cur.next = pre
#             pre = cur
#             cur = next
        
#         return pre
    

# def print_ll(head):
#     if head is None:
#         return -1
#     cur = head
#     while cur is not None:
#         print(cur.val, end='->')
#         cur = cur.next


# def list2ll(list):
#     if not list:
#         return None
    
#     head = ListNode(list[0])
#     cur = head
#     for val in list[1:]:
#         cur.next = ListNode(val)
#         cur = cur.next
    
#     return head

# head1 = [1,2,3,4,5]
# head2 = list2ll(head1)

# print_ll(head2)

# sol_instance = Solution()
# res = sol_instance.ReverseLinkedList(head2)

# print('\n')
# print_ll(res)

# 2023.9.19(6th)

# class ListNode():
#     def __init__(self, val = 0, next = None) -> None:
#         self.val = val
#         self.next = next

# class Solution():
#     def Rever(self, head):
#         cur = head
#         pre = ListNode(None)
#         while cur:
#             next = cur.next
#             cur.next = pre
#             pre = cur
#             cur = next

#         return pre

# def print_ll(head):
#     if head is None:
#         return -1
#     cur = head
#     while cur is not None:
#         print(cur.val, end='->')
#         cur = cur.next


# def list2ll(list):
#     if not list:
#         return None
    
#     head = ListNode(list[0])
#     cur = head
#     for val in list[1:]:
#         cur.next = ListNode(val)
#         cur = cur.next
    
#     return head

# head1 = [1,2,3,4,5]
# head2 = list2ll(head1)

# print_ll(head2)

# sol_instance = Solution()
# res = sol_instance.Rever(head2)

# print('\n')
# print_ll(res)


# 2023.9.21(7th) #迭代

# class ListNode():
#     def __init__(self, val = 0, next = None) -> None:
#         self.val = val
#         self.next = next

# class Solution():#迭代
#     def rever(self, head):
#         # pre = None
#         # cur = head

#         # while cur:
#         #     next = cur.next
#         #     cur.next = pre
#         #     pre = cur
#         #     cur = next
        
#         # return pre
#         if head is None or head.next is None:
#             return head
        
#         res = self.rever(head.next)
#         head.next.next = head
#         head.next = None

#         return res


# def list2ll(list):
#     if not list:
#         return None
    
#     head = ListNode(list[0])
#     cur = head
#     for val in list[1:]:
#         cur.next = ListNode(val)
#         cur = cur.next
    
#     return head

# def printll(head):
#     if not head:
#         return print('None')
    
#     cur = head
#     while cur:
#         print(cur.val , end= '->')
#         cur = cur.next

#     return print('None')

# head1 = list2ll([1,2,3,4,5])
# printll(head1)

# sol = Solution()
# head2 = sol.rever(head1)
# printll(head2)

import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

class ListNode():
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class Solutuion():
    def ReverseLinkedList(self, head):
        prev = None
        cur = head

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        return prev

