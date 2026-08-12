# 给你四个整数数组 nums1、nums2、nums3 和 nums4 ，数组长度都是 n ，请你计算有多少个元组 (i, j, k, l) 能满足：

# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
 

# 示例 1：
# 输入：nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
# 输出：2
# 解释：
# 两个元组如下：
# 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

# 示例 2：
# 输入：nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
# 输出：1


import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-29 20:27:59

class Solution():
    def foursum(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]):
        hash = {}
        # hash table 键存 num，值存下标
        for i in nums1:
            for j in nums2:
                # 前两个数、每个和出现了多少次
                if i + j not in hash:
                    hash[i + j] = 1
                else:
                    hash[i + j] += 1
        
        count = 0
        for k in nums3:
            for l in nums4:
                # target '相反数(-k-l +k+l =0)' 在不在字典里
                if - k - l in hash:
                    # 后面两个只要凑出来 1 种，就得加前面 2 个和的总次数
                    count += hash[- k - l]

        return count 
    
#  时间复杂度： O(n^2)
#  空间复杂度： O(n^2), hash 在存 nums1 和 nums2 的两两和，所以最多会存到 n^2

sol = Solution()
res = sol.foursum(nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0])
print(res)