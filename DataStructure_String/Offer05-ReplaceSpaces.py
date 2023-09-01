class Solution():
    def replaceSpace(self, s: str):
        n = len(s)
        ans = [ ]
        for i in range(n):
            if s[i] == ' ':
                ans.append('%20')
            else:
                ans.append(s[i])

        return ''.join(ans)
    
sol = Solution()
res = sol.replaceSpace(s = "We are happy.")
print(res)
