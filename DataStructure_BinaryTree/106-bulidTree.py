import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-10-01 19:59:26

class TreeNode():
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def buildTree(self, inorder: list[int], postorder: list[int]):
        if not postorder:
            return None
        
        split_val = postorder[-1]
        root = TreeNode(split_val)

        split_index = inorder.index(split_val)

        inorder_left = inorder[:split_index]
        inorder_right = inorder[split_index + 1:]

        postorder_left = postorder[: len(inorder_left)]
        postorder_right = postorder[len(inorder_left) : len(postorder) - 1]
        
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        return root

# 当前时间是: 2023-10-01 20:49:42
