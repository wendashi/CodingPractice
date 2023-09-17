# class Solutioin():
#     def repeat(self, s: str):
#         n = len(s)
#         for i in range(1, n//2 + 1):
#             if n % i == 0 and s[:i] * (n//i) == s[:] :
#                 return True
        
#         return False

# sol = Solutioin()
# res = sol.repeat(s = "abab")
# print(res)


# class Solution():
#     def repeatedsp(self, s: str):
#         n = len(s)
#         if n <= 1:
#             return False
        
#         for i in range(1, (n // 2) + 1):
#             if n % i == 0 and s[:i] * (n//i) == s:
#                 return True

#         return False

# sol = Solution()
# res = sol.repeatedsp(s = "ababb")
# print(res)

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
class Solution():
    def repeated(self, s: str):
        new_s = ''
        for i in range(len(s) // 2):
            new_s = new_s + s[i]
            if new_s * (len(s) // (i+1) ) == s:
                return True
        
        return False

sol = Solution()
res = sol.repeated(s = 'ababb')
print(res)
# 时间、空间都是 O(n)