# # from typing import Optional
# class TreeNode:
#     def __init__(self, val = None, left = None, right = None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution():
#     def MinDBT(self, root):
#         return self.getdepth(root)
    
#     def getdepth(self, node):
#         if node == None:
#             return 0
        
#         leftheight = self.getdepth(node.left)
#         rightheight = self.getdepth(node.right)
        
#         if node.left != None and node.right == None:
#             return 1 + leftheight
        
#         if node.right != None and node.left == None:
#             return 1 + rightheight
        
#         return 1 + min(leftheight, rightheight)


# # def build_tree_from_list(lst, index=0):
# #     if index >= len(lst) or lst[index] is None:
# #         return None
    
# #     node = TreeNode(lst[index])
# #     node.left = build_tree_from_list(lst, 2 * index + 1)
# #     node.right = build_tree_from_list(lst, 2 * index + 2)
# #     return node

# # root_list = [3, 9, 20, None, None, 15, 7]
# # root_node = build_tree_from_list(root_list)

# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.left = TreeNode(7)

# sol_instance = Solution()
# res = sol_instance.MinDBT(root)

# print(res)


import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-10-01 15:53:57

class TreeNode():
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def MinDepth(self, root: TreeNode):
        if not root:
            return 0
        
        leftMinDepth = self.minDepth(root.left)
        rightMinDepth = self.minDepth(root.right)

        if root.left == None and root.right != None:
            return 1 + rightMinDepth
        
        if root.left != None and root.right == None:
            return 1 + leftMinDepth
        
        MinDepth = 1 + min(leftMinDepth, rightMinDepth)

        return MinDepth
    