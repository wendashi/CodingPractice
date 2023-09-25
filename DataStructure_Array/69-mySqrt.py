import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-21 20:32:36

class Solution():
    def sqart(self, x: int):
        l = 0
        r = x
        while l < r:
            mid = (l + r) // 2 + 1
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                r = mid - 1 
            else:
                l = mid
        
        return l