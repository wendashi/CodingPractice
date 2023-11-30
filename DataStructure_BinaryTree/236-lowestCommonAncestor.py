import datetime
from collections import deque
# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("current time:", formatted_time)

# current time: 2023-11-30 10:32:30

# 从下往上->后序遍历：左右中

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def lowestCommonAncestor(self, root, p, q):
        # ending condition
        if root is None:
            print('???')
            return root
        if root == p or root == q:
            print(root.val)
            return root # 如果出现了 p 或 q，就向上返回
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            print('root',root)
            return root
        
        if left is None and right is not None:
            print('right',right)
            return right
        elif left is not None and right is None:
            print('left',left)
            return left
        else:
            return None

def print_tn(root: TreeNode):
    que = deque([root])
    print_res = []

    while que:
        for _ in range(len(que)):
            cur = que.popleft()
            print_res.append(cur.val)
            if cur.left:
                que.append(cur.left)
            if cur.right:
                que.append(cur.right)
    
    return print(print_res)

tn = TreeNode(3)
tn.left = TreeNode(5)
tn.right = TreeNode(1)
tn.left.left = TreeNode(6)
tn.left.right = TreeNode(2)
tn.right.left = TreeNode(0)
tn.right.right = TreeNode(8)
tn.left.right.left = TreeNode(7)
tn.left.right.right = TreeNode(4)

print_tn(tn)

sol = Solution()

result1 = sol.lowestCommonAncestor(tn, p = tn.left, q = tn.right)
result2 = sol.lowestCommonAncestor(tn, p = tn.left, q = tn.left.right.right)

# p 和 q 要传入节点，而不是节点的值！！！
# result1 = sol.lowestCommonAncestor(tn, p = 5, q = 1)
# result2 = sol.lowestCommonAncestor(tn, p = 5, q = 4)

# 最终的输出也是节点的值！！
print('result1:',result1.val)
print('result2:',result2.val)