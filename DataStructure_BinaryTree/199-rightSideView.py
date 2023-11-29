import datetime
import collections # from collections import deque

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# print current time
print("current time is:", formatted_time)

# current time is: 2023-11-29 10:15:38

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode):
        if not root:
            return []
        
        queue = collections.deque([root]) # deque([root])
        right_view = []

        while queue:
            level_size = len(queue) # 一层有几个

            for i in range(level_size):
                node = queue.popleft()

                if i == level_size - 1: # 每层的最后一个
                    right_view.append(node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

        return right_view

tn1 = TreeNode(1)
tn1.left = TreeNode(2)
tn1.right = TreeNode(3)
tn1.left.right = TreeNode(5)
tn1.right.right = TreeNode(4)

sol = Solution()
result = sol.rightSideView(tn1)
print(result)

# current time is: 2023-11-29 10:34:53