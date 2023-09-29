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

# from operator import add, sub, mul

# class Solution():
#     op_map = {'+': add, '-': sub, '*': mul, '/': lambda x, y: int(x / y)}

#     def ERP(self, tokens: list[str]):
#         stack = []

#         for i in tokens:
#             if i in self.op_map:
#                 op1 = int(stack.pop())
#                 op2 = int(stack.pop())
#                 ans = self.op_map[i](op2 , op1)
#                 stack.append(ans)
#             else:
#                 stack.append(int(i))

#         return stack.pop()

# sol = Solution()
# res = sol.ERP(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
# print(res)

# 2023.9.12（6th）

# from operator import add, sub, mul

# class Solution():
#     hash1 = {'+': add, '-': sub, '*': mul, '/': lambda x,y: int(x / y)}

#     def erp(self, tokens: list[str]):
#         stack = []
#         for i in tokens:
#             if i in self.hash1:
#                 op1 = int(stack.pop())
#                 op2 = int(stack.pop())
#                 res = self.hash1[i](op2, op1)
#                 stack.append(res)
#             else:
#                 stack.append(int(i))
        
#         return stack.pop()

# sol = Solution()
# res = sol.erp(tokens = ["4","13","5","/","+"])
# print(res)

# 时间复杂度：O(n) ；空间复杂度：O(n)
# 时间复杂度分析：循环次数+循环中的操作

# 在函数中，我们使用一个循环来迭代处理输入的字符串列表 tokens，其长度为 n。
# 在循环内部，我们检查每个字符串是否为运算符（+、-、*、/）或操作数。这些操作的时间复杂度都是O(1)，因为它们只涉及基本的算术运算和栈操作。
# 在循环中，我们使用栈 stack 来存储操作数和中间结果。每个元素都会被压入栈一次，然后最终弹出。因此，循环中的操作次数是线性的，与输入列表的大小 n 相关。
# 总体来说，循环内的操作次数是O(n)，因此时间复杂度为O(n)。
# 空间复杂度分析：

# 在函数中，我们使用了一个栈 stack 来存储操作数和中间结果。
# 栈 stack 的最大可能大小取决于输入列表 tokens 中的元素数量。在最坏的情况下，当输入的逆波兰表达式是有效的且没有多余的操作符时，栈的大小会达到 n/2，其中 n 是输入列表 tokens 的长度。
# 因此，栈 stack 的空间复杂度是O(n)。
# 综上所述，这个函数的时间复杂度是O(n)，空间复杂度也是O(n)，其中 n 是输入列表 tokens 的长度。这是因为在最坏情况下，栈的大小会达到输入列表长度的一半。

import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

from operator import add, sub, mul

class Solution():
    op_map = {'+': add, '-': sub, '*': mul, '/': lambda x, y : int(x / y)}

    def erp(self, tokens: list[str]):
        stack = []
        for i in tokens:
            print('i:', i,'stack:', stack)
            if i not in ['+', '-', '*', '/']:
                stack.append(i)
            else:
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                res = self.op_map[i](op2, op1)
                stack.append(res)
        
        return stack[0]
    
sol = Solution()
res = sol.erp(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print(res)