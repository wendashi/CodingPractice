class Solution():
    def vp(self, s:  str):
        stack = []

        for i in s:
            if i == '(':
                stack.append(')')
            elif i == '[':
                stack.append(']')
            elif i == '{':
                stack.append('}')
            elif not stack or stack[-1] != i:
                return False
            else:
                stack.pop()


        return True if not stack else False

sol = Solution()

res = sol.vp(s = '(){}[')

print(res)