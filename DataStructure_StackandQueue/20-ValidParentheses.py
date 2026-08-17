# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

# 有效字符串需满足：

# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 每个右括号都有一个对应的相同类型的左括号。

# 示例 1：
# 输入：s = "()"
# 输出：true

# 示例 2：
# 输入：s = "()[]{}"
# 输出：true

# 示例 3：
# 输入：s = "(]"
# 输出：false

# 示例 4：
# 输入：s = "([])"
# 输出：true

# 示例 5：
# 输入：s = "([)]"
# 输出：false

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

class Solution:
    def isValid(self, s: str) -> bool:
        # False: 1)左括号多，2)右括号更多，3)左右不匹配
        stack = []
        for i in s:
            if i in '([{':      # 左括号进栈
                stack.append(i)
            
            else:
                
                if not stack:  #  右括号更多
                    return False

                top = stack.pop()
                # 左右不匹配
                if (i == ')' and top != '(' ) or \
                    (i == ']' and top != '[' ) or \
                    (i == '}' and top != '{' ):
                    return False

        return not stack # 最后得是空的，不然就是左括号多
    
sol = Solution()
res = sol.vp(s = '((()))')
print(res)
