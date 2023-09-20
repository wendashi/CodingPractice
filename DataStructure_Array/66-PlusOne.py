# class Solution:
#     def PlusOne(self, digits:list[int]):
#         string = ''
#         for i in digits:
#             string += str(i)

#         res1 = str(int(string) + 1) 

#         return[int(i) for i in res1]
    
# solution_instance = Solution()

# digits1 = [1,2,3]

# result = solution_instance.PlusOne(digits1)

# print(result)


#2023.9.20(7th)

class Solution():
    def plusone(self, digits: list[int]):
        digi = ''
        for i in digits:
            digi += str(i)
        
        i_digi = int(digi) + 1

        res = []
        for i in str(i_digi):
            res.append(int(i))
        
        return res
    
sol = Solution()
res = sol.plusone(digits = [1, 2, 3])
print(res)
