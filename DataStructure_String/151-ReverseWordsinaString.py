class Solution():
    def reverwords(self, s: str):
        words = s.split()
        words[:] = words[::-1]

        return ' '.join(words)
    
sol = Solution()
res = sol.reverwords(s = "the sky is blue")
print(res)