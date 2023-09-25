from collections import defaultdict
import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-22 15:34:46

class Solution():
    def totalfruit(self, fruits: list[int]):
        i = 0
        bucket = 0
        classmap = defaultdict(int)
        res = 0

        for j in range(len(fruits)):
            print(classmap)
            if classmap[fruits[j]] == 0:
                bucket += 1
            classmap[fruits[j]] += 1

            # 若不满足条件，移动i
            while bucket > 2:
                if classmap[fruits[i]] == 1:
                    bucket -= 1
                classmap[fruits[i]] -= 1
                i += 1

            # 一旦满足条件，更新结果
            res = max(res, j - i + 1)
            j += 1
        return res    

sol = Solution()
res = sol.totalfruit(fruits = [3,3,3,1,2,1,1,2,3,3,4])
print(res)