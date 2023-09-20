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

class Solution():
    def happynum(self, n: int):
        seen = set()

        while n not in seen:
            seen.add(n)
            print('n', n)
            new_n = 0 # 每次算完后，再等于 0 、清空
            for i in str(n):
                new_n += int(i) ** 2
            
            print('new_n', new_n)
            if new_n == 1:
                return True
            
            else:
                n = new_n

        return False


sol = Solution()
res = sol.happynum(n = 3)
print(res)
