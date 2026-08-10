# 给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。

# 单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。

# 示例 1：
# 输入：s = "Hello World"
# 输出：5
# 解释：最后一个单词是“World”，长度为 5。

# 示例 2：
# 输入：s = "   fly me   to   the moon  "
# 输出：4
# 解释：最后一个单词是“moon”，长度为 4。

# 示例 3：
# 输入：s = "luffy is still joyboy"
# 输出：6
# 解释：最后一个单词是长度为 6 的“joyboy”。
# https://leetcode.cn/problems/length-of-last-word/description/

from collections import defaultdict
import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 2026-08-09 13:22:49 58-1st

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1 # 最后一个单词的最后一个字符位置
        while s[i] == ' ': # 把末尾空格都跳过去
            i -= 1

        j = i # 从最后一个单词的右边开始
        while j >= 0 and s[j] != ' ':
            j -= 1

        return i - j

s = "Hello World"
print(len(s))