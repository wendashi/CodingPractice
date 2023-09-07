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

import heapq

class Solution():
    def topk(self, nums:list[int], k:int):
        freq_map = {}

        for i in nums:
            if i in freq_map:
                freq_map[i] += 1
            else:
                freq_map[i] = 1
        
        max_heap = []
        
        for num, freq in freq_map.items():
            heapq.heappush(max_heap, (-freq, num))
        
        ans = []

        for i in range(k):
            freq, num = heapq.heappop(max_heap)
            ans.append(num)
        
        return ans

sol = Solution()
res = sol.topk(nums = [1,1,1,2,2,3], k = 2)
print(res)