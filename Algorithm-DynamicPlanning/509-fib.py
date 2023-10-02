import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-10-01 21:49:13

class Solution():
    def fib(self, n: int):
        if n <= 1:
            return n
        
        dp = [0, 1]

        while n - 1:
            temp = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = temp
            n -= 1

        return dp[1]
    
sol = Solution()
res = sol.fib(n = 4)
print(res)