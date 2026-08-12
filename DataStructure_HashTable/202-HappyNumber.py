# 编写一个算法来判断一个数 n 是不是快乐数。

# 「快乐数」 定义为：

# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
# 如果这个过程 结果为 1，那么这个数就是快乐数。
# 如果 n 是 快乐数 就返回 true ；不是，则返回 false 。

# 示例 1：

# 输入：n = 19
# 输出：true

# 解释：
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

# 示例 2：
# 输入：n = 2
# 输出：false


from typing import Any


import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-29 19:47:00（9th）    
class Solution():
    def hn(self, n: int):
        # 记录出现过的结果；一旦重复，就说明进环了
        seen = set()
        # list 查找是 顺着一个个比 ，最坏要把整个列表看完；
        # 而 set 底层是 哈希表 ，可以根据值直接快速定位。
        while n != 1:
            new_n = 0
            for i in str(n):
                new_n += int(i) ** 2
            if new_n in seen:
                return False
            seen.add(new_n)
            n = new_n

        return True

sol = Solution()
res = sol.hn( n = 100 )
print(res)
