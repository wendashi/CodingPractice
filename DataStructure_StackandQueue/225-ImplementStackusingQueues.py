# https://leetcode.cn/problems/implement-stack-using-queues/description/
# 请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）。

# 实现 MyStack 类：

# void push(int x) 将元素 x 压入栈顶。
# int pop() 移除并返回栈顶元素。
# int top() 返回栈顶元素。
# boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。
 

# 注意：

# 你只能使用队列的标准操作 —— 也就是 push to back、peek/pop from front、size 和 is empty 这些操作。
# 你所使用的语言也许不支持队列。 你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。


# 1. 因为deque的pop操作也是常数时间；
# 2. 通过deque来存储元素，空间复杂度不会随着元素数量的增加而线性增加，因为deque是一个动态数组，它会根据需要自动扩展其内部数组的大小。
# 如果用一个固定大小的数组来实现栈，那么空间复杂度可能会是O(n)，因为数组的大小是固定的，会随着元素数量的增加而线性增加。
# 但是在这个特定的实现中，使用了deque，它的内部实现是动态的，因此空间复杂度是恒定的，不会随着元素数量的增加而线性增加。

# - 时间复杂度: 都是O(1)
# - 空间复杂度: 都是O(1)


import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

from collections import deque
# 当前时间是: 2023-09-28 14:15:59

class MyStack():
    def __init__(self) -> None:
        self.que = deque()
    
    def push(self, x: int):
        self.que.append(x)
    
    def pop(self):
        if self.empty():
            return None
        
        return self.que.pop()
    
    def top(self):
        if self.empty():
            return None
        else:
            ans = self.que.pop()
            self.que.append(ans)
            return ans

    def empty(self):
        return not self.que

myStack1 = MyStack()

res1 = myStack1.push(1)
res2 = myStack1.push(2)
res3 = myStack1.top()
res4 = myStack1.pop()
res5 = myStack1.empty()

print(res1, '\n', res2, '\n', res3, '\n', res4, '\n', res5)