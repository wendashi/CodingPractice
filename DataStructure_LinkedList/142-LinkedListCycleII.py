class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution():
    def findcycle(self, head):
        fast , slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                temp = slow
                cur1 = temp
                cur2 = head
                while cur1 != cur2:
                    cur1 = cur1.next    
                    cur2 = cur2.next
                return cur1
        
        return None
    
def print_ll(head):
    if not head:
        return None
    
    cur = head
    while cur:
        print(cur.val, end='->')
        cur = cur.next


def list2cll(list, pos):# pos 是链表内环的起始位置
    if not list:
        return None
    
    head = ListNode(list[0])
    cur = head
    for val in list[1:]:
        cur.next = ListNode(val)
        cur = cur.next

    cur1 = head
    while pos:
        cur1 = cur1.next
        pos -= 1
    cur.next = cur1
    
    return head

head = [3,2,0,-4]
pos = 1

head1 = list2cll(head, pos)
sol = Solution()
res = sol.findcycle(head1)

print_ll(res)
