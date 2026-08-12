# 给定两个数组 nums1 和 nums2 ，返回 它们的 交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。

# 示例 1：
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2]

# 示例 2：
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[9,4]
# 解释：[4,9] 也是可通过的
 

import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 2023-09-29 16:53:50
# 2026-08-12 17:09:33

# dict 是“哈希表里的 键:值”，
# 而 set 是“ 只有键，没有实际值 ”的哈希表，本质上只关心“这个元素在不在”。
class Solution():
    def ita(self, nums1: list[int], nums2: list[int]):
        set1 = set(nums1)
        set2 = set(nums2)
        res = []
        for i in set2:
            if i in set1:
                res.append(i) 

        return res

sol = Solution()
res = sol.ita(nums1 = [4,9,5], nums2 = [9,4,9,8,4])
print(res)
