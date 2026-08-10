# https://leetcode.cn/problems/remove-linked-list-elements/description/
# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
# 示例 1：
# 输入：head = [1,2,6,3,4,5,6], val = 6
# 输出：[1,2,3,4,5]

# 示例 2：
# 输入：head = [], val = 1
# 输出：[]

# 示例 3：
# 输入：head = [7,7,7,7], val = 7
# 输出：[]


import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-10-02 12:03:53 (8th)

# class ListNode():
#     def __init__(self, val = 0, next = None) -> None:
#         self.val = val
#         self.next = next
    
# class Solution():
#     def remove(self, head: ListNode, val: int):
          # 🔥 head 不是一个额外的节点， 它只是指向第一个节点的引用 。
#         cur = ListNode(next = head) # dummy/cur -> head -> 1...
#         dummy = cur
#         while cur.next: # 因为要用 cur.next.next 
#             if cur.next.val == val:
#                 # 2 -> 6 (cur.next) -> 3(cur.next.next)
#                 # 2.next = 6 变成 2.next = 3
#                 cur.next = cur.next.next 
#             else:
#                 cur = cur.next

#         return dummy.next

# def list2ln(list):
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

# sol = Solution()

# head1 = list2ln([1,2,6,3,4,5,6])

# print_ll(head1)

# print('\n')

# res = sol.remove(head1, 6)

# print_ll(res)

class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

# [1,2,6,3,4,5,6]
# 2 -> 6 -> 3
# cur -> cur.next -> cur.next.next
# cur -> cur.next.next
 
class Solution():
    def remove(self, head: ListNode(), val: int):
        cur = ListNode(next = head)
        dummy = cur
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
                # 删了就别动（因为可能连续存在 == val 的情况），没删再后移。
            else:
                cur = cur.next

        return dummy.next

def list2ListNode(list):
    if not list:
        return None
    head = ListNode(list[0])
    cur = head

    for val in list[1:]:
        cur.next = ListNode(val)
        cur = cur.next
        
    return head

def printListNode(head):
    if not head:
        return None
    
    cur = head
    while cur:
        print('cur.val:', cur.val)
        cur = cur.next
    
sol = Solution()
input = [1,2,3,4,6,5,6,6,]
value = 6
head = list2ListNode(input)

result = sol.remove(head, value)
printListNode(result)