# class Solution():
#     def SMII(self, n:int):
#         res = [[0] * n for _ in range(n)]
#         loop , mid = n // 2, n // 2
#         x , y = 0 ,0 
#         count = 1
#         for offset in range(1, loop+1): 
#             for i in range(y, n - offset):
#                 # print('x',x)
#                 # print('i',i)
#                 res[x][i] = count
#                 count += 1
#             # print('---')
#             for i in range(x, n - offset):
#                 # print('i',i)
#                 # print('n - offset',n - offset)
#                 res[i][n - offset] = count
#                 count += 1
#             # print('---')
#             for i in range(n - offset, y , -1):
#                 # print('n - offset',n - offset)
#                 # print('i',i)
#                 res[n - offset][i] = count
#                 count += 1
#             # print('---')
#             for i in range(n - offset, x , -1):
#                 # print('i',i)
#                 # print('n - offset',n - offset)
#                 res[i][y] = count
#                 count += 1
#             # print('---')
#             x += 1
#             y += 1
        
#         if n % 2 != 0:
#             res[mid][mid] = count
        
#         return res

# sol_instance = Solution()
# result = sol_instance.SMII(n = 3)
# print(result)


# 2023.9.20(7th)

# class Solution():
#     def smii(self, n: int):
#         nums = [[0] * n for _ in range(n)]
#         loop, mid = n //2, n//2
#         count = 1
#         startx, starty = 0, 0

#         for offset in range(1, loop + 1):
#             for i in range(starty , n - offset):
#                 nums[startx][i] = count
#                 count += 1
#             for i in range(startx, n - offset):
#                 nums[i][n - offset] = count
#                 count += 1
#             for i in range(n - offset, starty, -1):
#                 nums[n - offset][i] = count
#                 count += 1
#             for i in range(n - offset, startx, -1):
#                 nums[i][starty] = count
#                 count += 1
#             startx += 1
#             starty += 1
        
#         if n % 2 != 0:
#             nums[mid][mid] = count
        
#         return nums

import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-21 15:05:48(8th)

class Solution():
    def smii(self, n: int):
        nums = [[0] * n for _ in range(n)]
        loop, mid = n // 2, n // 2
        startx, starty = 0, 0
        count = 1

        for offset in range(1, loop + 1):
            print(startx, starty)
            for i in range(starty, n - offset):
                nums[startx][i] = count
                count += 1
            for i in range(startx, n - offset):
                nums[i][n - offset] = count
                count += 1
            for i in range(n - offset, starty, -1):
                nums[n - offset][i] = count
                count += 1
            for i in range(n - offset, startx, -1):
                nums[i][starty] = count
                count += 1
            startx += 1
            starty += 1
        
        if n % 2 != 0:
            nums[mid][mid] = count
        
        return nums

sol = Solution()
res = sol.smii( n = 4)
print(res)

# 当前时间是: 2023-09-21 15:26:30