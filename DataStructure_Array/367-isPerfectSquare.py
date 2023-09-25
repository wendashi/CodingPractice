import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-22 11:55:50

class Solution():
    def perfectsquare(self, num: int):
        if num == 1:
            return True
        
        l = 0
        r = num
        while l < r:
            mid = (l + r) // 2
            if mid * mid > num:
                r = mid
            elif mid * mid < num:
                l = mid + 1
            else:
                return True
        
        return False

sol = Solution()
res = sol.perfectsquare(num = 16)
print(res)

# 当前时间是: 2023-09-22 12:09:21