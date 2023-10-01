import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-30 19:49:37 (2nd)

from collections import deque

class TreeNode():
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        
        que = deque([root])
        res = []
        while que:
            level = []
            for _ in range(len(que)):
                cur = que.popleft()
                level.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            res.append(level)   
        
        return res

tn = TreeNode(3)
tn.left = TreeNode(9)
tn.right = TreeNode(20)
tn.right.left = TreeNode(15)
tn.right.right = TreeNode(7)

sol = Solution()
res = sol.levelOrder(tn)
print(res)



