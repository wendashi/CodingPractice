# class Solution():
#     def RN(self, ransomNote: str, magazine: str):
#         hashtable = {}
#         for i in magazine:
#             if i not in hashtable:
#                 hashtable[i] = 1
#             else:
#                 hashtable[i] += 1
#         print(hashtable)

#         for i in ransomNote:
#             if i in hashtable:
#                 hashtable[i] -= 1
#                 if hashtable[i] < 0:
#                     return False
#             else:
#                 return False
            
        
#         return True
    

# sol = Solution()
# res = sol.RN('aa', 'aab')
# print(res)

class Solution():
    def ransom(self, ransomNote: str, magazine: str):
        hash = {}
        for i in magazine:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1
        
        for i in ransomNote:
            if i in hash:
                hash[i] -= 1
                if hash[i] < 0:
                    return False
            
            else:
                return False
            
        
        return True
    
sol = Solution()
res = sol.ransom(ransomNote = "ab", magazine = "ba")
print(res)

# 时间复杂度： O(n) ，具体为 O(len(magazine) + len(ransomNote)),
# 空间复杂度：O(n) ，具体主要由哈希表的大小决定，为O(len(magazine))。