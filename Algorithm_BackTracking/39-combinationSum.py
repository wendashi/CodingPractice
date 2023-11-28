import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# print current time
print("current time is:", formatted_time)

class Solution:

    def backtracking(self, candidates, target, total, startIndex, path, result):
        if total > target:
            return
        if total == target:
            result.append(path[:])
            return
        
        #  取每一个元素的
        for i in range(startIndex, len(candidates)):
            total += candidates[i]
            path.append(candidates[i])
            self.backtracking(candidates, target, total, i, path, result)
            total -= candidates[i]
            path.pop()

    def combinationSum(self, candidates, target):
        result = [] # 终止条件
        self.backtracking(candidates, target, 0, 0, [], result)
        return result

candidates = [2,3,6,7]
target = 7

sol = Solution()
result = sol.combinationSum(candidates, target)
print(result)

# current time is: 2023-11-28 14:58:44