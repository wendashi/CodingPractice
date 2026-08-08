import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2026-08-07 23:36:34
# range 是左闭右开

class Solution():
    def removeduplicate(self, nums: list[int]):
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        
        return slow + 1

sol = Solution()
res = sol.removeduplicate(nums = [0,0,1,1,1,2,2,3,3,4])
print(res)