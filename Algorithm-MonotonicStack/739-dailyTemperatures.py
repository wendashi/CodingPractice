import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

class Solution():
    def dT(self, temperatures: list[int]):
        res = [0] * len(temperatures)
        stack = [0]
        for i in range(1, len(temperatures)):
            
            if temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
            
            else:
                while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                    res[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
        
        return res

sol = Solution()
res = sol.dT(temperatures = [73,74,75,71,69,72,76,73])
print(res)