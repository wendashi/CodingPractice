# class Solution():
#     def vp(self, s:  str):
#         stack = []

#         for i in s:
#             print(stack)
#             if i == '(':
#                 stack.append(')')
#             elif i == '[':
#                 stack.append(']')
#             elif i == '{':
#                 stack.append('}')
#             # elif not stack or stack[-1] != i:
#             #     return False
#             # else:
#             #     stack.pop()
#             # else 分支中的 stack.pop() 操作将在每次执行 else 时都执行
#             else:
#                 if not stack or i != stack.pop(): 
#                     return False    
                
#         return True if not stack else False

# sol = Solution()

# res = sol.vp(s = '(()))')

# print(res)

# 2023.9.7(5th)

# class Solution():
#     def validparentheses(self, s: str):
#         stack = []
#         for i in s:
#             if i == '(':
#                 stack.append(')')
#             elif i == '[':
#                 stack.append(']')
#             elif i == '{':
#                 stack.append('}')
#             else:
#                 if not stack or i != stack.pop():
#                     return False
        
#         return True if not stack else False

# sol = Solution()
# res = sol.validparentheses(s = "[()]")
# print(res)

# 2023.9.12(6th)
# class Solution():
#     def validparenthese(self, s: str):
#         stack = []
#         for i in s:
#             if i == '(':
#                 stack.append(')')
#             elif i == '[':
#                 stack.append(']')
#             elif i == '{':
#                 stack.append('}')
#             else:
#                 if not stack or i != stack.pop():
#                     return False
        
#         return False if stack else True

# sol = Solution()
# res = sol.validparenthese(s = "()[]{}")
# print(res)

# 时间复杂度：O(n)
# 空间复杂度：O(n)


import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

from collections import deque

# 当前时间是: 2023-09-29 09:35:44（7th）

class Solution():
    def vp(self, s: str):
        stack = []

        for i in s:
            print(stack)
            if i == '(':
                stack.append(')')
            elif i == '[':
                stack.append(']')
            elif i == '{':
                stack.append('}')
            elif not stack or i != stack.pop():
            # elif i != stack.pop() or not stack:
                return False
            
        return True if not stack else False
    
sol = Solution()
res = sol.vp(s = '((()))')
print(res)
