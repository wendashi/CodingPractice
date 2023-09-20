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

class ListNode():
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class Solution():
    def Rever(self, head):
        cur = head
        pre = ListNode(None)
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next

        return pre

def print_ll(head):
    if head is None:
        return -1
    cur = head
    while cur is not None:
        print(cur.val, end='->')
        cur = cur.next


def list2ll(list):
    if not list:
        return None
    
    head = ListNode(list[0])
    cur = head
    for val in list[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    
    return head

head1 = [1,2,3,4,5]
head2 = list2ll(head1)

print_ll(head2)

sol_instance = Solution()
res = sol_instance.Rever(head2)

print('\n')
print_ll(res)



