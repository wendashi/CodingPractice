# from typing import Optional

# class TreeNode:
#     def __init__(self, val = 0, left = None, right = None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution():
#     def MDBT(self, root: Optional[TreeNode]):
#         return self.getdepth(root)
#     # 根结点的最大高度就是二叉树的最大深度
#     def getdepth(self, node: Optional[TreeNode]):
#         if node is None:
#             return 0
#         leftheight = self.getdepth(node.left)
#         rightheight = self.getdepth(node.right)
#         depth = 1 + max(leftheight, rightheight)

#         return depth


# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

# sol_instance = Solution()
# res = sol_instance.MDBT(root)

# print(res)


import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-10-01 12:17:01(3rd)

class TreeNode():
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right
    
class Solution():
    def maxDepth(self, root: TreeNode):
        return self.getheight(root)
    
    def getheight(self, root: TreeNode):
        if not root:
            return 0
        
        left_height = self.getheight(root.left)
        right_height = self.getheight(root.right)
        height = 1 + max(left_height, right_height)
        return height


        