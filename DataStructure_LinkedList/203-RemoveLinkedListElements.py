# class ListNode:
#     def __init__(self, val = 0, next = None):
#         self.val = val
#         self.next = next


# class Solution():
#     def RL(self, head, val):
#         dummy = ListNode(next=head)
#         cur = dummy 
#         while cur.next != None:
#             if cur.next.val == val:
#                 cur.next = cur.next.next
#             else:
#                 cur = cur.next

#         return dummy.next


# def list_to_linked_list(lst):
#     if not lst:
#         return None

#     head = ListNode(lst[0])
#     current = head

#     for val in lst[1:]:
#         current.next = ListNode(val)
#         current = current.next

#     return head

# # 给定输入列表
# input_list = [1, 2, 6, 3, 4, 5, 6]

# # 将列表转化为链表
# head1 = list_to_linked_list(input_list)

# # 打印链表的值
# def print_ll(head):
#     current = head
#     while current:
#         print(current.val, end=" -> ")
#         current = current.next
#     print("None")

# print_ll(head1)

# sol_instance = Solution()
# res = sol_instance.RL(head1, val = 6)

# print_ll(res)

#2023.9.19(7th)

# class listnode():
#     def __init__(self, next = None, val = 0) -> None:
#         self.next = next
#         self.val = val

# class Solution():
#     def remove(self, head: list, val: int):
#         if head is None:
#             return None
#         dummy = listnode(next = head) # 虚拟头节点
#         cur = dummy                   # 具体操作时不要用虚拟头节点
#         while cur.next:
#             if cur.next.val == val:
#                 cur.next = cur.next.next
#             else:
#                 cur = cur.next
        
#         return dummy.next

# def list2ln(list):
#     if not list:
#         return None
    
#     head = listnode(val = list[0])
#     cur = head

#     for i in range(1, len(list)):
#         cur.next = listnode(val = list[i])
#         cur = cur.next

#     return head

# def printll(head):
#     cur = head
#     while cur:
#         print(cur.val, end = '->')
#         cur = cur.next
#     return print('None')

# head1 = list2ln([1,2,6,3,4,5,6])
# printll(head1)

# print('--------------')
# sol = Solution()
# res = sol.remove(head = head1, val = 6)
# printll(res)

import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-10-02 12:03:53

class ListNode():
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next
    
class Solution():
    def remove(self, head: ListNode, val: int):
        cur = ListNode(next = head)
        dummy = cur
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next

def list2ln(list):
    if not list:
        return None
    head = ListNode(list[0])
    cur = head

    for val in list[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head

def print_ll(head):
    if not head:
        return None
    
    cur = head
    while cur:
        print(cur.val, end = '->')
        cur = cur.next

sol = Solution()

head1 = list2ln([1,2,6,3,4,5,6])

print_ll(head1)

print('\n')

res = sol.remove(head1, 6)

print_ll(res)
