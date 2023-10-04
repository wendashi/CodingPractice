import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-10-04 15:03:27

class Solution():
    def romanToInt(self, s: str):
        hash = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        sum = 0
        for i, c in enumerate(s): #最后一个数
            if i + 1 < len(s) and hash[s[i]] < hash[s[i + 1]]:
                sum -= hash[c]
            elif i + 1 < len(s) and hash[s[i]] >= hash[s[i + 1]]:
                sum += hash[c]
        sum += hash[c]

        return sum

sol = Solution()
res = sol.romanToInt(s = 'III')
print(res)