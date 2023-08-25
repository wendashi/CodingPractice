class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution():
    def remove(self, head, n:int):
        dummy = ListNode(next = head)
        slow, fast = dummy, dummy

        while n >= 0:
            fast = fast.next
            n -= 1

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next
    
def list2ll(list):
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

head_list = [1,2,3,4,5]
n = 2

head_ll = list2ll(head_list)

print_ll(head_ll)

print('\n')
sol = Solution()
res = sol.remove(head_ll, n)

print_ll(res)

#test



