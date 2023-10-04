# class ListNode():
#     def __init__(self, val = 0, next = None):
#         self.val = val
#         self.next = next

# class Solution():
#     def remove(self, head, n:int):
#         dummy = ListNode(next = head)
#         slow, fast = dummy, dummy

#         while n >= 0:
#             fast = fast.next
#             n -= 1

#         while fast:
#             slow = slow.next
#             fast = fast.next

#         slow.next = slow.next.next

#         return dummy.next
    
# def list2ll(list):
#     if not list:
#         return None
    
#     head = ListNode(list[0])
#     cur = head

#     for val in list[1:]:
#         cur.next = ListNode(val)
#         cur = cur.next

#     return head

# def print_ll(head):
#     if not head:
#         return None
    
#     cur = head
#     while cur:
#         print(cur.val, end = '->')
#         cur = cur.next

# head_list = [1,2,3,4,5]
# n = 2

# head_ll = list2ll(head_list)

# print_ll(head_ll)

# print('\n')
# sol = Solution()
# res = sol.remove(head_ll, n)

# print_ll(res)

# #test

# class ListNode():
#     def __init__(self, val = 0, next = None) -> None:
#         self.val = val
#         self.next = next

# class Solution():
#     def remove(self, head: ListNode, n: int):
#         dummy = ListNode(next = head)
#         slow , fast = dummy, dummy
#         while n :
#             fast = fast.next
#             n -= 1
        
#         while slow.next and fast.next:
#             slow = slow.next
#             fast = fast.next
        
#         slow.next = slow.next.next

#         return dummy.next

# def list2ln(list):
#     if not list:
#         return None
    
#     head = ListNode(val = list[0])
#     cur = head
#     for val in list[1:]:
#         cur.next = ListNode(val)
#         cur = cur.next
    
#     return head

# def println(head):
#     if not head:
#         return None
#     cur = head
#     while cur:
#         print(cur.val , end= '->')
#         cur = cur.next
    
#     return print("None")

# sol = Solution()
# head1 = list2ln([1,2,3,4,5])
# print('head1:')
# println(head1)

# res = sol.remove(head1 , n = 2)

# println(res)

import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)
    
# 当前时间是: 2023-10-02 13:34:18

class ListNode():
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class Solution():
    def remove(self, head: ListNode, n: int):
        slow = head
        fast = head

        while n >= 0:
            fast = fast.next
            n -= 1
        
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return head
    
def list2ll(list):
    head = ListNode(list[0])

    cur = head
    for val in list[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    
    return head

def print_ll(head):
    cur = head
    while cur:
        print(cur.val, end = '->')
        cur = cur.next

sol = Solution()
head1 = list2ll([1,2,3,4,5])
print_ll(head1)

print('\n')
res = sol.remove(head1, 2)

print_ll(res)
