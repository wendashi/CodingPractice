import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-22 12:16:08

class Solution():
    def removeduplicate(self, nums: list[int]):
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        
        return slow + 1

sol = Solution()
res = sol.removeduplicate(nums = [0,0,1,1,1,2,2,3,3,4])
print(res)

# 当前时间是: 2023-09-22 12:27:25