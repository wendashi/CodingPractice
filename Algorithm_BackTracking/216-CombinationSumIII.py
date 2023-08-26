class Solution():
    def CombinSum(self, k:int, n:int):
        result = []
        path = []
        self.backtracking(n, 0, 1, k, path, result)
        
        return result
    
    def backtracking(self, tarSum, curSum, startIndex, k, path, result):
        if curSum > tarSum:
            return 
        
        if len(path) == k:
            if curSum == tarSum:
                result.append(path[:])
            else: #?
                return 
        
        for i in range(startIndex, 9 - (k - len(path)) + 2):
            path.append(i)#append() 区别是啥？list 没法 push
            curSum += i
            self.backtracking(tarSum, curSum, i+1, k, path, result)
            path.pop()
            curSum -= i


k1 = 3
n1 = 7

sol = Solution()
res = sol.CombinSum(k1, n1)
print(res)