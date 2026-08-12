# Definition for singly-linked list.

# https://leetcode.cn/problems/intersection-of-two-linked-lists/solutions/12624/intersection-of-two-linked-lists-shuang-zhi-zhen-l/

# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# 输出：Intersected at '8'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA

        # 如果不相交，会在 None 相遇(可理解成“指针空了”)

        return A
