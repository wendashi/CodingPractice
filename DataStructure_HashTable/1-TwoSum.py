# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

# 你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

# 你可以按任意顺序返回答案。

# 示例 1：
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

# 示例 2：
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]

# 示例 3：
# 输入：nums = [3,3], target = 6
# 输出：[0,1]

import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-29 20:05:33（8th）    

class Solution():
    def twosum(self, nums: list[int], target: int):
        # 先用字典把 '值(作为键) -> 下标(作为值)' 记下来
        hash = {}
        for i, num in enumerate(nums):
            hash[num] = i
        
        # 然后再遍历一遍数组，对每个 nums[j] 去找 target - nums[j] 在不在字典里；
        # 如果在，而且不是同一个下标，就找到答案了。        
        for j in range(len(nums)):
            # 两个加起来和是 target
            left = target - nums[j]
            # 不能拿同一个位置的元素用两遍
            if left in hash and hash[left] != j:
                return [j, hash[left]]

# 时间复杂度： O(n)
# 空间复杂度： O(n), 因为额外用了一个字典来存 值 -> 下标 。

sol = Solution()
res = sol.twosum(nums = [3,7,8,3], target = 6)
print(res)