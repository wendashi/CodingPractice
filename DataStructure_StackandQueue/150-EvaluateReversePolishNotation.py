# 给你一个字符串数组 tokens ，表示一个根据 逆波兰表示法 表示的算术表达式。

# 请你计算该表达式。返回一个表示表达式值的整数。

# 注意：

# 有效的算符为 '+'、'-'、'*' 和 '/' 。
# 每个操作数（运算对象）都可以是一个整数或者另一个表达式。
# 两个整数之间的除法总是 向零截断 。
# 表达式中不含除零运算。
# 输入是一个根据逆波兰表示法表示的算术表达式。
# 答案及所有中间计算结果可以用 32 位 整数表示。

# 2023.9.12（6th）

# 时间复杂度：O(n) 
# 在函数中，我们使用一个循环来迭代处理输入的字符串列表 tokens，其长度为 n。

# 空间复杂度分析：
# 栈 stack 的最大可能大小取决于输入列表 tokens 中的元素数量。在最坏的情况下，当输入的逆波兰表达式是有效的且没有多余的操作符时，栈的大小会达到 n/2，其中 n 是输入列表 tokens 的长度。

import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

from typing import List

class Solution:
    def erp(self, tokens: List[str]) -> int:
        stack = []

        # 2) 用集合快速判断当前 token 是否是运算符
        ops = {"+", "-", "*", "/"}

        def div_towards_zero(a: int, b: int) -> int:
            # 3) Python // 是向下取整，和题目“向零截断”不同
            #  对负数的小数结果（如 -2.7），向零截断是 -2
            #  但从 Python 的 //（向下取整）结果 -3 修正为 -2，所以要 +1。
            q = a // b
            if (a < 0) != (b < 0) and a % b != 0:
                q += 1
            return q

        for t in tokens:
            # 4) 当前 token 是数字：转 int 后入栈（栈里只放整数，后续更清晰）
            if t not in ops:
                stack.append(int(t))
            
            else:
                # 5) 当前 token 是操作符：按 RPN 规则弹出两个操作数
                #    注意先弹出的是右操作数 b，再弹出的是左操作数 a
                b = stack.pop() 
                a = stack.pop()

                # 6) 一旦计算出子表达式结果，立即压回栈
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:  # "/"
                    stack.append(div_towards_zero(a, b))

        # 7) 所有 token 处理完后，栈顶就是最终答案
        return stack[-1]

    
sol = Solution()
res = sol.erp(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print(res)