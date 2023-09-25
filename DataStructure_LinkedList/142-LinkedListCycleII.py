# class ListNode():
#     def __init__(self, val = 0, next = None):
#         self.val = val
#         self.next = next

# class Solution():
#     def findcycle(self, head):
#         fast , slow = head, head

#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next

#             if slow == fast:
#                 temp = slow
#                 cur1 = temp
#                 cur2 = head
#                 while cur1 != cur2:
#                     cur1 = cur1.next    
#                     cur2 = cur2.next
#                 return cur1
        
#         return None
    
# def print_ll(head):
#     if not head:
#         return None
    
#     cur = head
#     while cur:
#         print(cur.val, end='->')
#         cur = cur.next


# def list2cll(list, pos):# pos 是链表内环的起始位置
#     if not list:
#         return None
    
#     head = ListNode(list[0])
#     cur = head
#     for val in list[1:]:
#         cur.next = ListNode(val)
#         cur = cur.next

#     cur1 = head
#     while pos:
#         cur1 = cur1.next
#         pos -= 1
#     cur.next = cur1
    
#     return head

# head = [3,2,0,-4]
# pos = 1

# head1 = list2cll(head, pos)
# sol = Solution()
# res = sol.findcycle(head1)

# print_ll(res)

# 2023.9.20(6th)

# class ListNode():
#     def __init__(self, val = 0, next = None) -> None:
#         self.val = val
#         self.next = next

# class Solution():
#     def circle(self, head: ListNode, pos: int):
#         if head is None or head.next is None:
#             return None
        
#         fast = head
#         slow = head
#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next
#             print('slow', slow.val)
#             print('fast', fast.val)

#             if slow == fast:
#                 meet = slow
#                 print(meet.val)#第一步起，就是从第二个节点开始
#                 cur = head 
#                 while cur != slow:
#                     # print(cur.val)
#                     cur = cur.next
#                     slow = slow.next
#                 return cur.val
            
#         return None

# head4 = ListNode(-4)
# head3 = ListNode(0, head4)
# head2 = ListNode(2, head3)
# head1 = ListNode(3, head2)

# head4.next = head2 #在后面加一下 next 就行～

# sol = Solution()
# res = sol.circle(head1, pos = 1)

# print(res)

# 2023.9.21(7th)

class ListNode():
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class Solution():
    def llc(self, head: ListNode, pos: int):
        if head is None or head.next is None:
            return None
    
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                cur = head
                while cur != slow:
                    cur = cur.next
                    slow = slow.next
                
                return cur.val
        
        return None

head4 = ListNode(-4)
head3 = ListNode(0, head4)
head2 = ListNode(2, head3)
head1 = ListNode(3, head2)

head4.next = head2

sol = Solution()
res = sol.llc(head1, 1)
print(res)