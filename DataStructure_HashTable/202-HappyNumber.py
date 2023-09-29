# class Solution():
#     def happynumber(self, n:int):

#         record = set()

#         while n not in record:
#             record.add(n)
#             new_n = 0
#             n_str = str(n)

#             for i in n_str:
#                 new_n += int(i) ** 2

#             if new_n == 1:
#                 return True
#             else:
#                 n = new_n 

#         return False

# n1 = 19
# n2 = 2    
# sol = Solution()
# res = sol.happynumber(n2)
# print(res)

#2023.9.17（6th）

# class Solution():
#     def happynum(self, n: int):
#         nset = set()

#         while n not in nset:
#             nset.add(n)
#             new_n = 0

#             for i in str(n):
#                 new_n += int(i) ** 2
            
#             if new_n == 1:
#                 return True
#             else:
#                 n = new_n
            
#         return False

# sol = Solution()
# res = sol.happynum(n = 19)
# print(res)

# 2023.9.18 (7th)

# class Solution():
#     def happynum(self, n: int):
#         seen = set()
#         # new_n = 0

#         while n not in seen:
#             seen.add(n)
#             new_n = 0 #每次都需要从 0 开始，因为

#             for i in str(n):
#                 new_n += int(i) ** 2
            
#             print(new_n)
#             # 算出来结果之后再判断
#             if new_n == 1:
#                 return True
#             else:
#                 n = new_n
    
#         return False

# sol = Solution()
# res = sol.happynum( n = 7)
# print(res)

# 2023.9.19(8th)

# class Solution():
#     def happynum(self, n: int):
#         seen = set()

#         while n not in seen:
#             seen.add(n)
#             print('n', n)
#             new_n = 0 # 每次算完后，再等于 0 、清空
#             for i in str(n):
#                 new_n += int(i) ** 2
            
#             print('new_n', new_n)
#             if new_n == 1:
#                 return True
            
#             else:
#                 n = new_n

#         return False


# sol = Solution()
# res = sol.happynum(n = 3)
# print(res)

import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-29 19:47:00（9th）    
class Solution():
    def hn(self, n: int):
        res = []
        while n != 1:
            print('n', n )
            new_n = 0
            for i in str(n):
                print('i', i)
                new_n += int(i) ** 2
            if new_n not in res:
                res.append(new_n)
            elif new_n != 1 and new_n in res:
                return False   
            n = new_n

        return True

sol = Solution()
res = sol.hn( n = 100 )
print(res)
