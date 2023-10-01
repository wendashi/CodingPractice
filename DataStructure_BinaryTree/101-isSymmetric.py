import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-10-01 11:15:44

class TreeNode():
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def isSymmetric(self, root: TreeNode):
        if not root:
            return True
        
        return self.compare(root.left, root.right)
    
    def compare(self, left, right):
        if left == None and right != None: return False
        elif left != None and right == None: return False
        elif left == None and right == None: return True

        elif left.val != right.val: return False
        
        outside = self.compare(left.left, right.right)
        inside = self.compare(left.right, right.left)
        isSym = outside and inside

        return isSym
    
rt = TreeNode(1)
rt.left = TreeNode(2)
rt.left.left = TreeNode(3)
rt.left.right = TreeNode(4)
rt.right = TreeNode(2)
rt.right.right = TreeNode(4)
rt.right.left = TreeNode(4)

sol = Solution()
res = sol.isSymmetric(rt)
print(res)


        