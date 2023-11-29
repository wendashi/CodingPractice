import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# print current time
print("current time is:", formatted_time)

class Solution:

    def backtracking(self, candidates, target, total, startIndex, used, path, result):
        if total > target:
            return []
        
        if total == target:
            result.append(path[:])
            return
        
        for i in range(startIndex, len(candidates)):
            # 对于相同的数字，只选择第一个未被使用的数字，跳过其他相同数字
            # used 是一个数组，表示对应位置的数是否被用过。其中 1 表示用过、0 表示没用过
            if i > startIndex and candidates[i] == candidates[i - 1] and used[i - 1] == 0:
                continue

            if total + candidates[i] > target:
                break

            total += candidates[i]
            path.append(candidates[i])
            used[i] = True
            self.backtracking(candidates, target, total, i + 1, used, path, result)
            used[i] = False
            total -= candidates[i]
            path.pop()


    def combinationSum2(self, candidates, target):
        used = [False] * len(candidates)
        result = []
        path = []
        candidates.sort()
        self.backtracking(candidates, target, 0, 0, used, path, result)
        return result

sol = Solution()
# candidates = [10,1,2,7,6,1,5]
# target = 8

candidates = [2,5,2,1,2]
target = 5

res = sol.combinationSum2(candidates, target)

print(res)

# current time is: 2023-11-29 11:34:11