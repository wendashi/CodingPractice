class Solution():
    def RN(self, ransomNote: str, magazine: str):
        hashtable = {}
        for i in magazine:
            if i not in hashtable:
                hashtable[i] = 1
            else:
                hashtable[i] += 1
        print(hashtable)

        for i in ransomNote:
            if i in hashtable:
                hashtable[i] -= 1
                if hashtable[i] < 0:
                    return False
            else:
                return False
            
        
        return True
    

sol = Solution()
res = sol.RN('aa', 'aab')
print(res)
