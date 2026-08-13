# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。

# 示例 1：
# 输入：haystack = "sadbutsad", needle = "sad"
# 输出：0
# 解释："sad" 在下标 0 和 6 处匹配。
# 第一个匹配项的下标是 0 ，所以返回 0 。

# 示例 2：
# 输入：haystack = "leetcode", needle = "leeto"
# 输出：-1
# 解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。
 

# class Solution:
#     def strStr(self, haystack: str, needle: str):
#         return haystack.find(needle)
#         # 时间复杂度： O(n * m)， find() 底层本质是在主串里找子串；面试/算法题里通常按朴素匹配上界记成 O(nm) 
#         # 空间复杂度： O(1)


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # haystack 中遍历 needle 长度的串，来做匹配
        for i in range(len(haystack)-len(needle)+1):
            # Python 切片是左闭右开
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

# 时间复杂度：O(n * m)，其中 n 是字符串 haystack 的长度，m 是字符串 needle 的长度。最坏情况下我们需要将字符串 needle 与字符串 haystack 的所有长度为 m 的子串均匹配一次。

# 空间复杂度：O(1)。我们只需要常数的空间保存若干变量


# KMP
# 时间复杂度： O(n + m)
# 空间复杂度： O(m)
class Solution:
    # 先给 needle 做一个 next 数组，记录：
    # 到当前位置为止，最长相等前后缀的长度是多少。 
    def getNext(self, next: List[int], s: str) -> None:
        j = 0
        next[0] = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = next[j - 1]
            if s[i] == s[j]:
                j += 1
            next[i] = j
    
    #  匹配失败时，不回退 haystack ，只回退 needle 到“前后缀相等”的位置继续比。
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        next = [0] * len(needle)
        self.getNext(next, needle)
        j = 0
        # 用 i 扫描主串，用 j 扫描模式串。
        # 如果失配，就令 j = next[j - 1] ，相当于把模式串滑到“还能接着试的位置”，不用从头再比。
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                # 上一步匹配过的信息
                j = next[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - len(needle) + 1
        return -1


sol = Solution()
results = sol.strStr(haystack = "abcsadbutsad", needle = "sad")
print(results)