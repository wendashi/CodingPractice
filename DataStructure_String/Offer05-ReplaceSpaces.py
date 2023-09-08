# class Solution():
#     def replaceSpace(self, s: str):
#         n = len(s)
#         ans = [ ]
#         for i in range(n):
#             if s[i] == ' ':
#                 ans.append('%20')
#             else:
#                 ans.append(s[i])

#         return ''.join(ans)
    
# sol = Solution()
# res = sol.replaceSpace(s = "We are happy.")
# print(res)
# 2023.9.8【9:14-】双指针

class Solution():
    def replacespace(self, s:str):
        counter = s.count(' ')
        res = list(s)
        # extend() 是对原 list 直接操作

        res.extend([' '] * counter * 2)
        l = len(s) - 1
        r = len(res) - 1
        # 原始字符串的末尾，拓展后的末尾

        while l >= 0:
            if res[l] != ' ':
                res[r] = res[l]
                r -= 1
            else:
                # [right - 2, right), 左闭右开！
                res[r - 2: r + 1] = '%20'
                r -= 3
            l -= 1

        return ''.join(res)
                
    
sol = Solution()
res = sol.replacespace(s = "We are happy.")

print(res)
