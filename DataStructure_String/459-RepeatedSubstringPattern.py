# 给定一个非空的字符串 s ，检查是否可以通过由它的一个子串重复多次构成。

# 示例 1:
# 输入: s = "abab"
# 输出: true
# 解释: 可由子串 "ab" 重复两次构成。

# 示例 2:
# 输入: s = "aba"
# 输出: false

# 示例 3:
# 输入: s = "abcabcabcabc"
# 输出: true
# 解释: 可由子串 "abc" 重复四次构成。 (或子串 "abcabc" 重复两次构成。)

# 时间复杂度分析：
# 循环从 i = 1 到 (n // 2) + 1 进行迭代，其中 n 表示输入字符串 s 的长度。
# 在每次迭代中，进行了一些常数时间的操作，包括整数除法，字符串切片，字符串乘法和字符串比较。
# 循环的迭代次数取决于 n 的大小，但是它不会遍历整个字符串 s。
# 因为循环的迭代次数与输入规模 n 相关，所以该算法的时间复杂度是 O(n)。

# 空间复杂度分析：
# 除了循环变量 i 和输入参数 s 之外，代码没有使用额外的数据结构或内存空间。
# 字符串切片和乘法操作不会显式创建新的字符串，因此它们不会显著增加空间复杂度。
# 因此，该算法的空间复杂度是 O(1)，即它的空间消耗是常数级的，与输入规模无关。

# 2023.9.17(6th)


import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-29 16:21:32(7th)
class Solution():
    def rsp(self, s: str):
        n = len(s)
        s_i = ''
        for i in range(1, (n // 2) + 1):
            # 试每一种可能的子串长度，看能不能整除并完整拼回原串。
            s_i = s[:i]
            # print(s_i, i)
            # 完整拼回原串: 长度刚好整除, 且重复 n//i 次后刚好一致
            if n % i == 0 and s == s_i * (n // i):
                return True
        
        return False

sol = Solution()
res = sol.rsp(s = "abcabcabcabc")
print(res)