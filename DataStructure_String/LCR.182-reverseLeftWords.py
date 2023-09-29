import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-29 16:17:20
class Solution():
    def rlw(self, password: str, target: int):
        return password[target:] + password[:target]
    
sol = Solution()
res = sol.rlw(password = "s3cur1tyC0d3", target = 4)
print(res)