# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的 字母异位词。

# 示例 1:
# 输入: s = "anagram", t = "nagaram"
# 输出: true

# 示例 2:
# 输入: s = "rat", t = "car"
# 输出: false

import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-29 16:47:20(7th)

class Solution():
    def va(self, s: str, t: str):
        hash = {} # 字典
        # 先把 s 里每个字符出现次数记下来，再用 t 去一一抵消
        for i in s:
            # 键存字符，值存字符对应的数量
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
        
        for i in t:
            if i not in hash:
                return False
            else:
                hash[i] -= 1
        
        for i, i_num in hash.items():
            #  i = 键，比如字符 'a'
            #  i_num = 值，比如它对应的计数 2    
            if i_num != 0:
                return False
        
        # for i in s:
        #     if hash[i] != 0:
        #         return False
        
        return True

sol = Solution()
res = sol.va(s = "rat", t = "car")
print(res)
