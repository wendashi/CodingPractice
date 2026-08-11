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

# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

# 示例 1：
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]

# 示例 2：
# 输入：head = [1], n = 1
# 输出：[]

# 示例 3：
# 输入：head = [1,2], n = 1
# 输出：[1]

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
        dummy = ListNode(next = head)
        slow = dummy
        fast = dummy

        while n >= 0:
            fast = fast.next
            n -= 1
        
        while fast:
            fast = fast.next
            slow = slow.next
        # 当 fast = None

        slow.next = slow.next.next

        return dummy.next
    
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
head1 = list2ll([1])
print_ll(head1)

print('\n')
res = sol.remove(head1, 1)

print_ll(res)
