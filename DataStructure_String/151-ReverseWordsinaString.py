# class Solution():
#     def reverwords(self, s: str):
#         words = s.split()
#         words[:] = words[::-1]

#         return ' '.join(words)
    
# sol = Solution()
# res = sol.reverwords(s = "the sky is blue")
# print(res)

# 时间复杂度分析：

# words = s.split(): 这一行代码使用字符串的 split() 方法将输入字符串 s 拆分成单词列表。拆分操作的时间复杂度取决于字符串中包含的单词数量和单词的平均长度，通常为 O(n)，其中 n 是字符串的长度。

# words[:] = words[::-1]: 这一行代码使用了切片操作来反转单词列表 words 中的元素。切片操作 words[::-1] 的时间复杂度是 O(n)，其中 n 是单词列表的长度。

# 最后，通过 ' '.join(words) 将单词列表中的元素连接成一个字符串。连接操作的时间复杂度也是 O(n)，其中 n 是单词列表中所有单词字符的总数。

# 总体来说，这个函数的时间复杂度主要由拆分操作、切片操作和连接操作决定，都是线性的，因此总时间复杂度为 O(n)。

# 空间复杂度分析：

# words = s.split(): 这一行代码创建了一个单词列表 words，它的空间复杂度取决于字符串中包含的单词数量和单词的平均长度。通常，空间复杂度为 O(n)，其中 n 是字符串的长度。

# words[:] = words[::-1]: 这一行代码并没有创建额外的数据结构，而是原地修改了单词列表 words 的内容，因此没有额外的空间开销。

# join() 方法创建了一个新的字符串，其中包含单词列表 words 中的所有单词字符。这个新字符串的空间复杂度取决于单词列表中所有单词字符的总数，通常也是 O(n)，其中 n 是字符串的长度。

# 总体来说，这个函数的空间复杂度主要由单词列表 words 和新创建的连接后的字符串决定，通常为 O(n)。由于没有创建额外的数据结构，空间复杂度相对较低。


# class Solution():
#     def reverseword(self, s: str):
#         words = s.split()
#         l = 0
#         r = len(words) - 1
#         while l < r:
#             words[l], words[r] = words[r], words[l]
#             l += 1
#             r -= 1
        
#         return ' '.join(words) 
    
# sol = Solution()
# res = sol.reverseword(s = "a good   example")
# print(res)

# 时间复杂度分析：

# words = s.split(): 这一行代码使用字符串的 split() 方法将输入字符串 s 拆分成单词列表。拆分操作的时间复杂度取决于字符串中包含的单词数量和单词的平均长度，通常为 O(n)，其中 n 是字符串的长度。

# 然后，通过 l 和 r 两个指针，使用循环将单词列表中的元素反转。这个循环的时间复杂度是 O(n/2)，因为它只需要遍历一半的单词列表。

# 最后，通过 ' '.join(words) 将单词列表中的元素连接成一个字符串。连接操作的时间复杂度也是 O(n)，其中 n 是单词列表中所有单词字符的总数。

# 因此，总体来说，这个函数的时间复杂度主要由拆分操作和连接操作决定，都是线性的，因此总时间复杂度为 O(n)。

# 空间复杂度分析：

# words = s.split(): 这一行代码创建了一个单词列表 words，它的空间复杂度取决于字符串中包含的单词数量和单词的平均长度。通常，空间复杂度为 O(n)，其中 n 是字符串的长度。

# l 和 r 两个指针以及循环中的其他变量只占用常量级别的额外空间，不随输入字符串大小而变化。

# 因此，总体来说，这个函数的空间复杂度主要由单词列表 words 决定，通常为 O(n)。

# 2023.9.16(6th)

class Solution():
    def reverseword(self, s: str):
        sl = s.split()
        res = sl[::-1]
        return ' '.join(res)

sol = Solution()
res = sol.reverseword(s = "the sky is blue")
print(res)