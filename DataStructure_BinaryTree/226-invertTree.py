import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-30 20:20:42 (1st)

from collections import deque

class TreeNode():
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def invertTree(self, root: TreeNode):
        if not root:
            return None #不能是[] 
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

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

rt = TreeNode(4)
rt.left = TreeNode(2)
rt.left.left = TreeNode(1)
rt.left.right = TreeNode(3)
rt.right = TreeNode(7)
rt.right.left = TreeNode(6)
rt.right.right = TreeNode(9)
print_tn(rt)

sol = Solution()
res = sol.invertTree(rt)

print_tn(rt) #?
print_tn(res)

    
