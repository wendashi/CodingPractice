from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def MDBT(self, root: Optional[TreeNode]):
        return self.getdepth(root)
    # 根结点的最大高度就是二叉树的最大深度
    def getdepth(self, node: Optional[TreeNode]):
        if node is None:
            return 0
        leftheight = self.getdepth(node.left)
        rightheight = self.getdepth(node.right)
        depth = 1 + max(leftheight, rightheight)

        return depth


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol_instance = Solution()
res = sol_instance.MDBT(root)

print(res)

