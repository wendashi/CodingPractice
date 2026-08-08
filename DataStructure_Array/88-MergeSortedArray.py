import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

# 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

# 注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。


# class Solution():
#     def merge(self, nums1: list[int], m: int, nums2: list[int], n: int):
#         i = m - 1 # nums1 有效部分末尾
#         j = n - 1 # nums2 末尾
#         write = m + n - 1  # 指向 nums1 实际末尾，这里就是放 nums1[i] 和 nums2[j] 中最大的
        # 🔥如果是 nums1 先完、还要继续比 nums2
        # 如果是 nums2 先完，说明 nums1 的本来就小、不用动
#         while j >= 0: 
#             if i >= 0 and nums1[i] > nums2[j]:
#                 nums1[write] = nums1[i]
#                 i -= 1
#             else:
#                 nums1[write] = nums2[j]
#                 j -= 1
#             write -= 1

#         return nums1

# sol = Solution()
# res = sol.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
# print(res)


class Solution():
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int):
        i = m - 1 # nums1 非0的实际末尾
        j = n - 1 # nums2 末尾
        k = m + n - 1 # nums1 的 0 末尾

        # 如果 nums2 走完, nums1 没走完，说明nums1的本来就更小
        # ❌ 如果 nums1 走完，nums2 没走完
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        return nums1



sol = Solution()
res = sol.merge(nums1 = [2,0], m = 1, nums2 = [1], n = 1)
print(res)
