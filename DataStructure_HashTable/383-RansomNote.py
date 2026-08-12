import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-29 20:35:31（7th）

class Solution():
    def ransomnote(self, ransomNote: str, magazine: str):
        hash = {}
        for i in magazine:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1

        # for i in r:
        #     if i in hash:
        #         hash[i] -= 1
        #         if hash[i] < 0:
        #             return False
        #     else:
        #         return False
        
        for letter in ransomNote:
            if letter not in hash or hash[letter] == 0:
                return False
            else:
                hash[letter] -= 1

        return True

# 时间复杂度 O(m + n),  m = len(magazine) ， n = len(ransomNote)
# 空间复杂度 O(m)

sol = Solution()
res = sol.ransomnote(r = 'aa', m = 'ab')
print(res)