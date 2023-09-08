# class Solution():
#     def rever(self, s: list[str]):
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         s[:] = [s[i] for i in range(len(s)-1, -1, -1)]
#         # return s[:]
        

# sol = Solution()
# res = sol.rever(s = ["h","e","l","l","o"])
# print(res)

## 2023.9.8 two pointers

class Solution():
    def reverstring(self, s: list[str]):
        l = 0
        r = len(s) - 1
        while l < r:
            # tempr = s[r]
            # templ = s[l]
            # s[l] = tempr
            # s[r] = templ
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
            

        return s[:]
    

sol = Solution()
res = sol.reverstring(s = ["h","e","l","l","o"])
print(res)

