import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-22 14:43:26

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sstack = []
        tstack = []
        for i in s:
            if i != '#':
                sstack.append(i)
            elif i == '#' and sstack:
                sstack.pop()

        for i in t:
            if i != '#':
                tstack.append(i)
            elif i == '#' and tstack:
                tstack.pop()
            
        return sstack == tstack
