import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-10-01 16:38:50

class TreeNode():
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def countNodes(self, root: TreeNode):
        if not root:
            return 0
        
        count = 1
        left = root.left
        right = root.right
        while left and right:
            count += 1
            left = left.left
            right = right.right

        if not left and not right:
            return 2 ** count - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)        