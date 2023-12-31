import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-30 15:19:10(2nd)

# 递归-自己调用自己

class TreeNode():
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def preordertraversal(self, root: TreeNode):
        if not root:
            return []

        left = self.preordertraversal(root.left)
        right = self.preordertraversal(root.right)

        return [root.val] + left + right

root = TreeNode(1)
root.left = None
root.right = TreeNode(2)
root.right.left = TreeNode(3)

sol = Solution()
res = sol.preordertraversal(root)
print(res)