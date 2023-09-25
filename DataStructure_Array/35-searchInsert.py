import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-21 15:56:12 (1st)

class Solution():
    def searchinsert(self, nums: list[int], target: int):
        l = 0
        r = len(nums)

        # if target > nums[r - 1]:
        #     return r
        # if target < nums[l]:
        #     return l

        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        
        return r if nums[mid] > target else l

