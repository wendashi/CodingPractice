# # 时间复杂度 O(n), 空间复杂度 O(n)


import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-29 15:48:50(7th)

class Solution():
    def reverses(self, s: str, k: int):
        flip = -1
        new_s = ''

        for i in range(0, len(s), k):
            a = s[i : i + k]
            new_s += a[::flip]
            flip = -flip
        
        return new_s


sol = Solution()
res = sol.reverses(s = "abcd", k = 2)
print(res)

# 当前时间是: 2023-09-29 15:56:37