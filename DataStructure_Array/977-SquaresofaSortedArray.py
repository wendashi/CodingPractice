# 2023.9.20(9th)
# 2026-08-06 11:40:38 (10th)
import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

class Solution():
    def SquareSortedArray(self, nums: list[int]):
        left = 0 
        right = len(nums) - 1
        result = []
        # corner case nums = [1], 此时 right = 0
        while left < right + 1:
            left_squre = nums[left] ** 2
            right_squre = nums[right] ** 2
            # 两端的平方里， 一定能确定较大的那个
            if left_squre > right_squre:
                result.append(left_squre)
                left += 1
            else:
                result.append(right_squre)
                right -= 1
        
        return result[::-1]

sol = Solution()
result = sol.SquareSortedArray(nums = [-4,-1,0,3,10])
print(result)
