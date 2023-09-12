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

class Solution():
    def removeaad(self, s: str):
        stack = []
        for i in s:
            if stack and i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
            
        return ''.join(stack)

sol = Solution()
res = sol.removeaad(s = "abbaca")
print(res)

# 时间复杂度：O(n),空间：O(n)