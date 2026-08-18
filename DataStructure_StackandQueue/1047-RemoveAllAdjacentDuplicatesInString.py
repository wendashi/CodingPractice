# 给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
# 在 S 上反复执行重复项删除操作，直到无法继续删除。
# 在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

# 示例：
# 输入："abbaca"
# 输出："ca"
# 解释：例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。

# 提示：
# 1 <= S.length <= 20000
# S 仅由小写英文字母组成。

# 时间复杂度：O(n),空间：O(n)

import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-29 09:54:13（6th）

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            # 如果栈顶字符和当前字符相同，就抵消（弹出）
            if stack and stack[-1] == i:
                stack.pop()
            else:
                # 否则入栈
                stack.append(i)
        return ''.join(stack)

sol = Solution()
res = sol.raads("abbaca")
print(res)