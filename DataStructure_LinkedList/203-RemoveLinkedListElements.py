class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution():
    def RL(self, head, val):
        dummy = ListNode(next=head)
        cur = dummy 
        while cur.next != None:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next


def list_to_linked_list(lst):
    if not lst:
        return None

    head = ListNode(lst[0])
    current = head

    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next

    return head

# 给定输入列表
input_list = [1, 2, 6, 3, 4, 5, 6]

# 将列表转化为链表
head1 = list_to_linked_list(input_list)

# 打印链表的值
def print_ll(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

print_ll(head1)

sol_instance = Solution()
res = sol_instance.RL(head1, val = 6)

print_ll(res)