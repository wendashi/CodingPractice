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

# （版本一）双指针法
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         cur = head   
#         pre = None
#         while cur:
#             temp = cur.next # 保存一下 cur的下一个节点，因为接下来要改变cur->next
#             cur.next = pre #反转
#             #更新pre、cur指针
#             pre = cur
#             cur = temp
#         return pre

# （版本二）递归法
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         return self.reverse(head, None)
#     def reverse(self, cur: ListNode, pre: ListNode) -> ListNode:
#         if cur == None:
#             return pre
#         temp = cur.next
#         cur.next = pre
#         return self.reverse(temp, cur)

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

        # 结束 while 时，cur 已经是 None了
        return prev


def list2ListNode(list):
    head = ListNode(list[0])
    cur = head

    for i in range(1, len(list)):
        cur.next = ListNode(list[i])
        cur = cur.next
    
    return head


def printListNode(head):
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next


input = [1, 2, 3, 4, 5]
head = list2ListNode(input)
print('Before:')
printListNode(head)

sol = Solutuion()
result = sol.ReverseLinkedList(head)
print('After:')
printListNode(result)
