import datetime
from collections import deque

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# print current time
print("current time is:", formatted_time)

# current time is: 2023-11-28 13:41:39

# queue 

class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lOB(self, root):
        if not root:
            return []
        
        queue = deque([root])
        result = []

        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(level)
        
        return result[::-1]

tn = TreeNode(3)
tn.left = TreeNode(9)
tn.right = TreeNode(20)
tn.right.left = TreeNode(15)
tn.right.right = TreeNode(7)

tn1 = TreeNode(1)

tn2 = []

sol = Solution()
res = sol.lOB(tn2)
print(res)

# current time is: 2023-11-28 14:16:11