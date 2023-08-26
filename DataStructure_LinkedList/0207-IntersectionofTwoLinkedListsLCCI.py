class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution():
    def intesection(self, headA, headB):
        A = headA
        B = headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        
        return A

def print_ll(head):
    if not head:
        return None

    cur = head
    while cur:
        print(cur.val, end='->')
        cur = cur.next

def createIntersectingLists(intersectVal, listA, listB, skipA, skipB):
    intersect_node = ListNode(intersectVal)
    cur = intersect_node
    for val in listA[skipA+1:]:
        print(val)
        cur.next = ListNode(val)
        cur = cur.next

    headA = ListNode(listA[0])
    current_A = headA
    for val in listA[1:skipA]:
        current_A.next = ListNode(val)
        current_A = current_A.next
    
    current_A.next = intersect_node
    # print('headA1')
    # print_ll(headA)
    # print('\n','intersect_nodeA1')
    # print_ll(intersect_node)

    headB = ListNode(listB[0])
    current_B = headB
    for val in listB[1:skipB]:
        current_B.next = ListNode(val)
        current_B = current_B.next
    
    current_B.next = intersect_node

    # print('\n', 'headB1')
    # print_ll(headB)
    # print('\n', 'intersect_nodeB1')
    # print_ll(intersect_node)

    return headA, headB, intersect_node

# Example values
intersectVal = 8
listA = [4, 1, 8, 4, 5]
listB = [5, 0, 1, 8, 4, 5]
skipA = 2
skipB = 3

# Create intersecting lists
headA, headB , intersect_node= createIntersectingLists(intersectVal, listA, listB, skipA, skipB)

print('headA:')
print_ll(headA)
print('\n','headB:')
print_ll(headB)
print('\n','intersect_node:')
print_ll(intersect_node)

sol = Solution()
res = sol.intesection(headA, headB)

print('\n','res:')
print_ll(res)
