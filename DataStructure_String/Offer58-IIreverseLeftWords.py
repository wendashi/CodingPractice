# class Solution():
#     def reverseLeftWords(self, s: str, k: int):
#         return s[k:] + s[:k]
    
# sol = Solution()
# res = sol.reverseLeftWords(s = "abcdefg", k = 2)
# print(res)

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        new_s = ''
        for i in range(len(s)):
            j = (i + n) % len(s)
            new_s = new_s + s[j]
        
        return ''.join(new_s)

sol = Solution()
res = sol.reverseLeftWords(s = "abcdefg", n = 2)
print(res)

# 时间复杂度分析：O(n)

# 主要的时间消耗来自于循环中的迭代，循环遍历了字符串s的每个字符，共执行了len(s)次迭代。
# 在每次迭代中，进行了一些常数时间的操作，如索引计算、字符串拼接。
# 所以总体时间复杂度可以表示为O(len(s))，其中len(s)是输入字符串s的长度。

# 空间复杂度分析：O(n)

# 主要的空间消耗来自于创建了一个名为new_s的新字符串，它的长度等于输入字符串s的长度。
# 此外，还有一些常数级的辅助空间消耗，如循环变量i、j等。
# 所以总体空间复杂度可以表示为O(len(s))，其中len(s)是输入字符串s的长度。