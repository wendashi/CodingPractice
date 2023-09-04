class Solution():
    def vp(self, s:  str):
        stack = []

        for i in s:
            print(stack)
            if i == '(':
                stack.append(')')
            elif i == '[':
                stack.append(']')
            elif i == '{':
                stack.append('}')
            # elif not stack or stack[-1] != i:
            #     return False
            # else:
            #     stack.pop()
            # else 分支中的 stack.pop() 操作将在每次执行 else 时都执行
            else:
                if not stack or i != stack.pop(): 
                    return False    
                
        return True if not stack else False

sol = Solution()

res = sol.vp(s = '(()))')

print(res)