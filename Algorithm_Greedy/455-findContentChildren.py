import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

class Solution():
    def findContentChildren(self, g: list[int], s: list[int]):
        g.sort()
        s.sort()

        index = 0
        for i in range(len(s)):
            if index < len(g) and g[index] <= s[i]:
                index += 1

        return index

sol = Solution()
res = sol.findContentChildren(g = [1,2], s = [1, 2, 3]) 
print(res)