# class ListNode():
#     def __init__(self, val = 0, next = None):
#         self.val = val
#         self.next = next
    
# class Solution():
#     def Swap(self, head):
#         dummy = ListNode(next = head)
#         cur = dummy

#         while cur.next and cur.next.next:
#             temp1 = cur.next
#             temp2 = cur.next.next.next

#             cur.next = cur.next.next
#             cur.next.next = temp1
#             temp1.next = temp2
#             cur = cur.next.next

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
#     if head is None:
#         return None
    
#     cur = head
#     while cur :
#         print(cur.val, end='->')
#         cur = cur.next
    

# head = [1,2,3,4]
# head_ll = list2ll(head)

# print_ll(head_ll)

# print('\n')
# sol = Solution()
# res = sol.Swap(head_ll)

# print_ll(res)

#2023.9.20 (6th)

class ListNode():
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class Solution():
    def swap(self, head):
        dummy = ListNode(next = head)
        cur = dummy
        while cur.next and cur.next.next:
            temp1 = cur.next
            temp2 = cur.next.next

            cur.next = cur.next.next
            cur.next.next = temp1
            temp1.next = temp2
            cur = cur.next.next

        return dummy.next

