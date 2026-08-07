# 题目：分解质因数
# 给定一个正整数 n，返回它的所有质因数。
# 需要按照从小到大的顺序返回；如果某个质因数出现多次，需要重复记录。
# 例如：50 = 2 * 5 * 5，返回 [2, 5, 5]。
# sample 1:
# input: n = 12
# result: [2, 2, 3]
# sample 2:
# input: n = 18
# result: [2, 3, 3]
# sample 3:
# input: n = 37
# result: [37]
# sample 4:
# input: n = 100
# result: [2, 2, 5, 5]

# class Solution():
#     def prime_factors(self, n: int):
        
#         res = []
#         i = 2
#         while i * i <= n: # 首先需要找出所有的质数
#             if n % i != 0: # n % i 是 取余数 ，看 n 能不能被 i 整除；
#                 i += 1
#             else:
#                 n //= i # # n //= i 是整除后再赋值给自己, 即 n = n // i 
#                 res.append(i)

#         if n > 1:
#             res.append(n)

#         return res

# sol = Solution()
# result = sol.prime_factors(n = 50)
# print(result)

import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-10-04 15:40:22

# 其中一种是使用质数筛法来对数字进行分解。
# 首先需要找出所有的质数，然后不断地除以质数，直到该数字变成 1 为止。
# 每次除以质数都会得到一个新的因数，并且这个因数一定是一个质数。

# 50 = 2 * 5 * 5，返回 [2, 5, 5]。

class Solution():
    def prime_factors(self, n: int):
        
        res = []
        i = 2
        while i ** 2 <= n:
            if n % i != 0:
                i += 1        
            else:
                n //= i
                res.append(i)

        if n > 1:
            res.append(n)

        return res

sol = Solution()
results = sol.prime_factors(108)
print('results:', results)