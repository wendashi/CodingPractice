import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-10-02 11:56:12

class Solution():
    def climbStairs(self, n: int):
        if n <= 3:
            return n
        
        prev1 = 1
        prev2 = 2
        
        for _ in range(3, n + 1):
            temp = prev1 + prev2
            prev1 = prev2
            prev2 = temp
        
        return prev2

sol = Solution()
res = sol.climbStairs(n=4)
print(res)