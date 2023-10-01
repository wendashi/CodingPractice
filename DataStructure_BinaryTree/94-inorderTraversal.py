import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-30 15:51:58 (2nd)

class TreeNode():
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def midtraversal(self, root: TreeNode):
        if not root:
            return []
        
        left = self.midtraversal(root.left)
        right = self.midtraversal(root.right)
        print('left', left, 'root', root.val, 'right', right)

        return left + [root.val] + right

tn = TreeNode(1)
tn.left = None
tn.right = TreeNode(2)
tn.right.left = TreeNode(3)

sol = Solution()
res = sol.midtraversal(tn)
print(res)