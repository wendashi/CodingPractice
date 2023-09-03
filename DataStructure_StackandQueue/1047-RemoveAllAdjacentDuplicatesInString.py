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
res = sol.removeaad('abbaca')

print(res)