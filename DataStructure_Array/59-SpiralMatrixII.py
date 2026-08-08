import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-28 09:27:38(9th)

# 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

# 示例：
# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]
# nums[0][0] = 1
# nums[0][1] = 2
# nums[0][2] = 3

# nums[1][0] = 8
# nums[1][1] = 9
# nums[1][2] = 4

# nums[2][0] = 7
# nums[2][1] = 6
# nums[2][2] = 5
# --------------
# nums[0][0] = 1
# nums[0][1] = 2

# nums[0][2] = 3
# nums[1][2] = 4

# nums[2][2] = 5
# nums[2][1] = 6

# nums[2][0] = 7
# nums[1][0] = 8

# nums[1][1] = 9

# 输入：n = 1
# 输出：[[1]]

class Solution():
    def matrixii(self, n: int):
        # 目标: 按一圈一圈地填矩阵
        nums = [[0] * n for _ in range(n)]  # 初始化全 0 n*n 矩阵
        startx, starty = 0, 0               # 起始点
        loop, mid = n // 2, n // 2          # loop - 迭代次数(绕几圈)、mid-n为奇数时，矩阵的中心点
        count = 1                           # count - 当前该填进去的数字是几

        for offset in range(1, loop + 1) :  # offset 是这一圈的右边界和下边界要往里缩多少 
            for i in range(starty, n - offset) :    # 这一行要填到哪一列为止？所以要看矩阵的总大小。从左至右，左闭右开
                nums[startx][i] = count
                count += 1
            for i in range(startx, n - offset) :    # 从上至下
                nums[i][n - offset] = count
                count += 1
            for i in range(n - offset, starty, -1) : # 从右至左
                nums[n - offset][i] = count
                count += 1
            for i in range(n - offset, startx, -1) : # 从下至上
                nums[i][starty] = count
                count += 1
            # 更新每圈(loop)的起始点                
            startx += 1         
            starty += 1
        
        # 因为奇数矩阵一层层缩进去，最后会剩 1 x 1
        if n % 2 != 0 :			# n为奇数时，填充中心点
            nums[mid][mid] = count 
        return nums

sol = Solution()
res = sol.matrixii(n = 3)
print(res)