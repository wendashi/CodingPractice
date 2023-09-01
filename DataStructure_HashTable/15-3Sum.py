class Solution():
    def Sum3(self, nums: list[int]):
        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[i] > 0 :
                return result
            
            if i > 0 and nums[i] == nums[i-1]:
                continue # continue 关键字用于跳过当前循环中的剩余代码，并继续下一次循环的执行

            left = i + 1
            right = len(nums) - 1

            while left < right:

                sum3 = nums[i] + nums[left] + nums[right]

                if sum3 > 0:
                    right -= 1
                elif sum3 < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    right -= 1
                    left += 1
        
        return result
    
sol = Solution()
res = sol.Sum3(nums = [-1,0,1,2,-1,-4])
print(res)

                