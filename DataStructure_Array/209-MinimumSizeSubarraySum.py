import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 2023-09-26 14:54:38 (8th)
# 2026-08-06 12:20:30 (9th)

class Solution():
    def mmsss(self, target: int, nums: list[int]):
        res = float('inf')
        i = 0
        sum = 0
        for j in range(len(nums)):
            sum += nums[j]
            while sum >= target: # = target 时，还要继续优化 res 看有没有办法更小
                sum -= nums[i]
                res = min(res, j - i + 1)
                i += 1
        
        return res if res != float('inf') else 0

sol = Solution()
res = sol.mmsss(target = 11, nums = [1,1,1,1,1,1,1,1])
print(res)
