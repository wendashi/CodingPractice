# import heapq

# class Solution():
#     def topk(self, nums: list[int], k: int):
#         freq_map = {}
#         for num in nums:
#             if num not in freq_map:
#                 freq_map[num] = 1
#             else:
#                 freq_map[num] += 1
        
#         max_heap = []

#         for num, freq in freq_map.items():
#             heapq.heappush(max_heap, (-freq, num))
        
#         ans = []
#         for i in range(k):
#             freq, num = (heapq.heappop(max_heap))
#             ans.append(num)

#         return ans


# sol = Solution()
# res = sol.topk(nums = [1,1,1,2,2,3], k = 2)

# print(res)
#2023.9.7(5th)

# import heapq

# class Solution():
#     def topk(self, nums:list[int], k:int):
#         freq_map = {}

#         for i in nums:
#             if i in freq_map:
#                 freq_map[i] += 1
#             else:
#                 freq_map[i] = 1
        
#         max_heap = []
        
#         for num, freq in freq_map.items():
#             heapq.heappush(max_heap, (-freq, num))
        
#         ans = []

#         for i in range(k):
#             freq, num = heapq.heappop(max_heap)
#             ans.append(num)
        
#         return ans

# sol = Solution()
# res = sol.topk(nums = [1,1,1,2,2,3], k = 2)
# print(res)

# 2023.9.12（6th）

import heapq

class Solution():
    def topk(self, nums: list[int], k: int):
        hash = {}

        for i in nums:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1
        
        
        heap = []
        for num, freq in hash.items():
            heapq.heappush(heap, (-freq, num))

        result = []
        for _ in range(k):
            freq, num = heapq.heappop(heap)
            result.append(num)
        
        return result

sol = Solution()
res = sol.topk(nums = [1,1,1,2,2,3], k = 2)
print(res)

# 时间复杂度分析：

# 1. 首先，代码使用一个循环遍历输入列表 **`nums`**，并将每个元素的频率存储在 **`freq_map`** 字典中。这个循环的时间复杂度是 O(n)，其中 n 是  列表的长度。
# 2. 然后，代码将元素和频率添加到一个大顶堆 **`max_heap`** 中。这个操作需要遍历 **`freq_map`** 字典，所以时间复杂度也是 O(n)。
# 3. 接下来，代码从大顶堆中弹出前 **`k`** 个元素。在每次弹出操作中，最坏情况下，堆中需要进行一次调整操作，因此总共需要进行 **`k`** 次调整。**每次调整的时间复杂度为 O(log n)（堆的高度是由元素的数量决定的，堆的高度不会超过log₂(n)，其中n是堆中的元素数量）**因此，这一部分的时间复杂度是 O(k * log n)。
# 4. 综合起来，总体时间复杂度是 O(n + k * log n)。

# 空间复杂度分析：

# 1. 首先，代码使用了一个字典 **`freq_map`** 来存储每个元素的频率。字典中的键是元素值，值是频率。在最坏情况下，所有元素都不相同，所以字典  的空间复杂度是 O(n)。
# 2. 然后，代码使用了一个大顶堆 **`max_heap`** 来存储元素和频率。堆的大小最多为 **`n`**，因此堆的空间复杂度也是 O(n)。
# 3. 最后，代码返回了一个列表 **`result`**，其中包含前 **`k`** 个高频元素。这个列表的空间复杂度是 O(k)。

# 综合起来，总体空间复杂度是 O(n + k)。



