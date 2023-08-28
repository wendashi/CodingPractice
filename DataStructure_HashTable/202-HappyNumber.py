class Solution():
    def happynumber(self, n:int):

        record = set()

        while n not in record:
            record.add(n)
            new_n = 0
            n_str = str(n)

            for i in n_str:
                new_n += int(i) ** 2

            if new_n == 1:
                return True
            else:
                n = new_n 

        return False

n1 = 19
n2 = 2    
sol = Solution()
res = sol.happynumber(n2)
print(res)