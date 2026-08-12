# 2023.9.21(7th)
# 2026.8.12(8th)

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
            
            # 第一次相遇说明“头到入口的距离 = 相遇点再走到入口的距离（模环长意义下）”
            # 所以一个从 head 出发，一个从相遇点出发，同速前进，就会在入口重合。
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