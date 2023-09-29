# class Solution():
#     def removeaad(self, s: str):
#         stack = []

#         for i in s:
#             if stack and i == stack[-1]:
#                 stack.pop()
#             else:
#                 stack.append(i)
            
#         return ''.join(stack)

# sol = Solution()
# res = sol.removeaad('abbaca')

# print(res)

#2023.9.7(5th)

# class Solution():
#     def removeaad(self, s: str):
#         stack = []
#         for i in s:
#             if stack and i == stack[-1]:
#                 stack.pop()
#             else:
#                 stack.append(i)
        
#         return ''.join(stack)
    

# sol = Solution()
# res = sol.removeaad(s = "abbaca")
# print(res)

# 2023.9.12(6th)

# class Solution():
#     def removeaad(self, s: str):
#         stack = []
#         for i in s:
#             if stack and i == stack[-1]:
#                 stack.pop()
#             else:
#                 stack.append(i)
            
#         return ''.join(stack)

# sol = Solution()
# res = sol.removeaad(s = "abbaca")
# print(res)

# 时间复杂度：O(n),空间：O(n)

import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-29 09:54:13（6th）

class Solution():
    def raads(self, s: str):
        stack = []
        for i in s:
            print(stack)
            if stack and i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        
        return ''.join(stack)

sol = Solution()
res = sol.raads("abbaca")
print(res)