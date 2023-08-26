class Solution():
    def __init__(self):
        self.letterMap = [
            '',
            '',
            'abc',
            'def',
            'ghi',
            'jkl',
            'mno',
            'pqrs',
            'tuv',
            'wxyz'    
        ]
        self.result = []
        self.s = ''
    
        
    def LetterCom(self, digits):
        if len(digits) == 0:
            return self.result
    
        self.backtracking(digits, 0)

        return self.result
    
    def backtracking(self, digits, index):
        if index == len(digits):
            self.result.append(self.s)
            return 
        
        digit = int(digits[index])
        letters = self.letterMap[digit]

        for i in range(len(letters)):
            self.s += letters[i]
            self.backtracking(digits, index + 1)
            self.s = self.s[:-1]

digits = "23"
            
sol = Solution()
res = sol.LetterCom(digits)
print(res)
            



