from collections import defaultdict
import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-25 14:19:09
# class Solution():
#     def so(self, matrix: list[list[int]]):
#         top, left = 0, 0 
#         bottom = len(matrix) - 1
#         right = len(matrix[0]) - 1
#         res = []

#         while top <= bottom and left <= right:
#             for i in range(left , right + 1):
#                 res.append(matrix[top][i])
#             top += 1

#             for i in range(top, bottom + 1):
#                 res.append(matrix[i][right])
#             right -= 1

#             if top <= bottom:
#                 for i in range(right, left - 1, -1):
#                     res.append(matrix[bottom][i])
#                 bottom -= 1
            
#             if left <= right:
#                 for i in range(bottom, top - 1, -1):
#                     res.append(matrix[i][left])
#                 left += 1
            
        
#         return res

# sol = Solution()
# result = sol.so(matrix = [[1,2,3],[4,5,6],[7,8,9]]) 
# print(result)

# 当前时间是: 2023-09-28 09:46:13(2nd)

class Solution():
    def so(self, matrix: list[list[int]]):
        top, left = 0, 0
        bottom, right = len(matrix) - 1, len(matrix[0]) - 1
        res = []
        if not matrix:
            return res

        while top <= bottom and left <= right:
            
            for i in range(left, right + 1):
                print('➡️',top, i)
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                print('⬇️',i, right)
                res.append(matrix[i][right])
            right -= 1

            # if top <= bottom:
            for i in range(right, left - 1, -1):
                print('⬅️',bottom, i,'top:',top)
                res.append(matrix[bottom][i])
            bottom -= 1

            # if left <= right:
            for i in range(bottom, top - 1, -1):
                print('⬆️',i, left)
                res.append(matrix[i][left])
            left += 1

        return res

sol = Solution()
result = sol.so(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(result)

