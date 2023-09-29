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

# class Solution():
#     def ransom(self, ransomNote: str, magazine: str):
#         hash = {}
#         for i in magazine:
#             if i in hash:
#                 hash[i] += 1
#             else:
#                 hash[i] = 1
        
#         for i in ransomNote:
#             if i in hash:
#                 hash[i] -= 1
#                 if hash[i] < 0:
#                     return False
            
#             else:
#                 return False
            
        
#         return True
    
# sol = Solution()
# res = sol.ransom(ransomNote = "ab", magazine = "ba")
# print(res)

# 时间复杂度： O(n) ，具体为 O(len(magazine) + len(ransomNote)),
# 空间复杂度：O(n) ，具体主要由哈希表的大小决定，为O(len(magazine))。

# 2023.9.17(6th)

# class Solution():
#     def ransomnote(self, rans: str, maga: str):
#         hash = {}
#         for i in maga:
#             if i in hash:
#                 hash[i] += 1
#             else:
#                 hash[i] = 1

#         for i in rans:
#             if i not in hash:
#                 return False
#             if i in hash:
#                 hash[i] -= 1
#                 if hash[i] < 0:
#                     return False
                
#         return True

# sol = Solution()
# res = sol.ransomnote(rans = 'aa', maga = 'ab')
# print(res)

import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-29 20:35:31（7th）

class Solution():
    def ransomnote(self, r: str, m: str):
        hash = {}
        for i in m:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1

        for i in r:
            if i in hash:
                hash[i] -= 1
                if hash[i] < 0:
                    return False
            else:
                return False
        
        return True

sol = Solution()
res = sol.ransomnote(r = 'aa', m = 'ab')
print(res)