class Solution():
    def combin(self, n:int, k:int):
        result = []
        self.backtracking(n, k, 1, [], result)
        return result
    
    def backtracking(self, n, k, startIndex, path, result):
        if len(path) == k:
            result.append(path[:])
            # 注意与 result.append(path)的区别
            return result
        
        for i in range(startIndex, n + 1 - (k - len(path)) + 1):
            print(i)
            path.append(i)
            self.backtracking(n, k , i + 1, path, result)
            path.pop()

n1 = 4
k1 = 2

sol = Solution()
res = sol.combin(n1, k1)

print(res)
