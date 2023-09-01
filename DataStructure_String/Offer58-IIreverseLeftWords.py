class Solution():
    def reverseLeftWords(self, s: str, k: int):
        return s[k:] + s[:k]
    
sol = Solution()
res = sol.reverseLeftWords(s = "abcdefg", k = 2)
print(res)
