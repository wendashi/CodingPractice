# nums1 = [3,2,2,3]
# val1 = 3

# nums2 = [0,1,2,2,3,0,4,2]
# val2 = 2

import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)


class Solution():
    def remove(self, nums: list[int], val: int):
        slow, fast = 0 , 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        return slow

sol = Solution()
res = sol.remove(nums = [3,2,2,3], val = 3)
print(res)

# 当前时间是: 2023-09-26 14:14:54