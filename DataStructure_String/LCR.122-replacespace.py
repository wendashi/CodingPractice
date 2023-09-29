import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-29 15:59:32
class Solution():
    def replacespace(self, path: str):
        res = []
        for i in path:
            if i == '.':
                res.append(' ')
            else:
                res.append(i)

        return ''.join(res)

sol = Solution()
res = sol.replacespace(path = "a.aef.qerf.bb")
print(res)