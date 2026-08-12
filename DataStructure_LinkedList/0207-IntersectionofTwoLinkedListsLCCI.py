# class ListNode():
#     def __init__(self, val = 0, next = None):
#         self.val = val
#         self.next = next


# class Solution():
#     def intesection(self, headA, headB):
#         A = headA
#         B = headB
#         while A != B:
#             A = A.next if A else headB
#             B = B.next if B else headA
        
#         return A

# def print_ll(head):
#     if not head:
#         return None

#     cur = head
#     while cur:
#         print(cur.val, end='->')
#         cur = cur.next

# # Example values
# intersectVal = 8
# listA = [4, 1, 8, 4, 5]
# listB = [5, 0, 1, 8, 4, 5]
# skipA = 2
# skipB = 3


# print('headA:')
# print_ll(headA)
# print('\n','headB:')
# print_ll(headB)
# print('\n','intersect_node:')
# print_ll(intersect_node)

# sol = Solution()
# res = sol.intesection(headA, headB)

# print('\n','res:')
# print_ll(res)

# 2023.9.20(6th)

# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。

# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
# 输出：Intersected at '8'
# 解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
# 从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
# 在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。


class ListNode():
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class Solution():
    def intersect(self, headA: ListNode, headB: ListNode):
        # curA 先走 A 再走 B， curB 先走 B 再走 A。这样两个人总路程都变成 A长度 + B长度
        # 因为循环退出条件是 curA == curB ，所以退出时 curA 和 curB 指向的是 同一个东西 ，要么是相交节点，要么是 None ，
        curA = headA
        curB = headB
        while curA != curB:
            curA = curA.next if curA is not None else headB
            curB = curB.next if curB is not None else headA
        
        return curA

headA5 = ListNode(5)
headA4 = ListNode(4, headA5)
headA3 = ListNode(8, headA4)
headA2 = ListNode(1, headA3)
headA1 = ListNode(4, headA2)

headB3 = ListNode(1, headA3)
headB2 = ListNode(0, headB3)
headB1 = ListNode(5, headB2)

sol = Solution()
res = sol.intersect(headA1, headB1)
print(res.val)