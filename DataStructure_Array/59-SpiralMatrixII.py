class Solution():
    def SMII(self, n:int):
        res = [[0] * n for _ in range(n)]
        loop , mid = n // 2, n // 2
        x , y = 0 ,0 
        count = 1
        for offset in range(1, loop+1): 
            for i in range(y, n - offset):
                # print('x',x)
                # print('i',i)
                res[x][i] = count
                count += 1
            # print('---')
            for i in range(x, n - offset):
                # print('i',i)
                # print('n - offset',n - offset)
                res[i][n - offset] = count
                count += 1
            # print('---')
            for i in range(n - offset, y , -1):
                # print('n - offset',n - offset)
                # print('i',i)
                res[n - offset][i] = count
                count += 1
            # print('---')
            for i in range(n - offset, x , -1):
                # print('i',i)
                # print('n - offset',n - offset)
                res[i][y] = count
                count += 1
            # print('---')
            x += 1
            y += 1
        
        if n % 2 != 0:
            res[mid][mid] = count
        
        return res

sol_instance = Solution()
result = sol_instance.SMII(n = 3)
print(result)