class Solution():
    def rever(self, s: list[str]):
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = [s[i] for i in range(len(s)-1, -1, -1)]
        # return s[:]
        

sol = Solution()
res = sol.rever(s = ["h","e","l","l","o"])
print(res)