# from operator import add, sub, mul

# class Solution():
#     op_map = {'+': add, '-': sub, '*': mul, '/': lambda x, y: int(x / y)}
    
#     def ERP(self, tokens: list[str]):
#         stack = []

#         for i in tokens:
#             if i not in ('+', '-', '*', '/'):
#                 stack.append(int(i))
#             else:
#                 op2 = stack.pop()
#                 op1 = stack.pop()
#                 stack.append(self.op_map[i](op1, op2))
        

#         return stack.pop()
    
# sol = Solution()
# res = sol.ERP(tokens = ["2","1","+","3","*"])
# print(res)

#2023.9.7(5th)

from operator import add, sub, mul

class Solution():
    op_map = {'+': add, '-': sub, '*': mul, '/': lambda x, y: int(x / y)}

    def ERP(self, tokens: list[str]):
        stack = []

        for i in tokens:
            if i in self.op_map:
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                ans = self.op_map[i](op2 , op1)
                stack.append(ans)
            else:
                stack.append(int(i))

        return stack.pop()

sol = Solution()
res = sol.ERP(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print(res)