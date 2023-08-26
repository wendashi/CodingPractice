class Solution():
    def VA(self, s:str, t:str):
        rec = [0] * 26
        for i in s:
            rec[ord(i) - ord('a')] += 1
        for i in t:
            rec[ord(i) - ord('a')] -= 1
        
        for i in range(26):
            if rec[i] != 0:
                return False
        
        return True

s1 = "anagram"
t1 = "nagaram"

s2 = "rat"
t2 = "car"

sol = Solution()
res1 = sol.VA(s1, t1)

res2 = sol.VA(s2, t2)
print('1:', res1)

print('2:', res2)