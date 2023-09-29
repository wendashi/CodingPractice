# class Solution():
#     def VA(self, s:str, t:str):
#         rec = [0] * 26
#         for i in s:
#             rec[ord(i) - ord('a')] += 1
#         for i in t:
#             rec[ord(i) - ord('a')] -= 1
        
#         for i in range(26):
#             if rec[i] != 0:
#                 return False
        
#         return True

# s1 = "anagram"
# t1 = "nagaram"

# s2 = "rat"
# t2 = "car"

# sol = Solution()
# res1 = sol.VA(s1, t1)

# res2 = sol.VA(s2, t2)
# print('1:', res1)

# print('2:', res2)

#2023.9.17(6th)

# way2
# class Solution():
#     def valid(self, s: str, t: str):
#         sn = len(s)
#         tn = len(t)
#         if sn != tn:
#             return False
#         hash = {}
#         for i in s:
#             if i in hash:
#                 hash[i] += 1
#             else:
#                 hash[i] = 1
        
#         for j in t:
#             if j in hash:
#                 hash[j] -= 1
#                 if hash[j] < 0:
#                     return False
#             else:
#                 return False
            
#         return True

# sol = Solution()
# res = sol.valid(s = "anagram", t = "nagaraam")
# print(res)

# #way1
# class Solution():
#     def valid(self, s: str, t: str):
#         rec = 26 * [0]
#         for i in s:
#             rec[ord(i) - ord('a')] += 1
        
#         for i in t:
#             rec[ord(i) - ord('a')] -= 1
        
#         for i in range(26):
#             if rec[i] != 0:
#                 return False

#         return True


# sol = Solution()
# res = sol.valid(s = "anagram", t = "nagaraam")
# print(res)

import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-29 16:47:20(7th)

class Solution():
    def va(self, s: str, t: str):
        hash = {}
        for i in s:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
        
        for i in t:
            if i not in hash:
                return False
            else:
                hash[i] -= 1
        
        for i, i_num in hash.items():
            if i_num != 0:
                return False
        
        return True

sol = Solution()
res = sol.va(s = "rat", t = "car")
print(res)

# 当前时间是: 2023-09-29 16:51:21