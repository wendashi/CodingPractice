from collections import defaultdict
import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-25 11:46:59

class Solution():
    def sa(self, array: [[int]]):
        n = len(array)
        mid, loop = len(array) // 2, len(array) // 2
        startx, starty = 0, 0
        res = []

        for offset in range(1, loop + 1):
            for i in range(starty, n - offset):
                res.append(array[startx][i])

            for i in range(startx, n - offset):
                res.append(array[i][n - offset])

            for i in range(n - offset, starty, -1):
                res.append(array[n - offset][i])

            for i in range(n - offset, startx, -1):
                res.append(array[i][starty])

            startx += 1
            starty += 1

        if n % 2 != 0:
            res.append(array[mid][mid])
        
        return res

sol = Solution()
result = sol.sa(array = [[1,2,3],[4,5,6],[7,8,9]])
print(result)

