class Solution():
    def rever(self, s: str, k: int):
        res = ''
        n = len(s)
        flip = -1
        for i in range(0, n, k):
            a = s[i: i+k ]
            res += a[::flip]
            flip = -flip

        return res
    
sol = Solution()
res = sol.rever(s = "abcdefg", k = 2)
print(res)