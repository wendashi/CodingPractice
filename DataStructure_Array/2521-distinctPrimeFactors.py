import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-10-04 15:51:45

# class Solution(): # 直觉的做法
#     def dPF(self, nums: list[int]):
#         nums_res = 1 # 乘积
#         for num in nums:
#             nums_res *= num
        
#         factors = [] # 乘积的质因数

#         i = 2
#         while i * i <= nums_res: # 可能的质数，从 2 开始
#             if nums_res % i != 0:
#                 i += 1
#             else:
#                 nums_res //= i
#                 factors.append(i)
        
#         if nums_res > 1:
#             factors.append(nums_res)
        
#         factors_set = set(factors)
        
#         res = len(factors_set)

#         return res

class Solution: # 每一个数的质因数
    def distinctPrimeFactors(self, nums: list[int]) -> int:
        factors = set()
        for num in nums:
            i = 2
            while i * i <= num:
                if num % i != 0:
                    i += 1
                else:
                    num //= i
                    factors.add(i)
            if num > 1:
                factors.add(num)
        
        return len(factors)



