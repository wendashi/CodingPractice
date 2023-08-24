class Solution:
    def PlusOne(self, digits:list[int]):
        string = ''
        for i in digits:
            string += str(i)

        res1 = str(int(string) + 1) 

        return[int(i) for i in res1]
    
solution_instance = Solution()

digits1 = [1,2,3]

result = solution_instance.PlusOne(digits1)

print(result)

