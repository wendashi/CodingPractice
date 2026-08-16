# 请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：

# 实现 MyQueue 类：

# void push(int x) 将元素 x 推到队列的末尾
# int pop() 从队列的开头移除并返回元素
# int peek() 返回队列开头的元素
# boolean empty() 如果队列为空，返回 true ；否则，返回 false
# 说明：

# 你 只能 使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
# 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
 


# 时间复杂度： push，empty：O(1); pop(),peek() : O(n)
# 空间复杂度： O(n)

import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-26 16:15:52


class MyQueue():
    def __init__(self) -> None:
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int):
        self.stack_in.append(x)

    def pop(self):
        if self.empty():
            return None
        
        if self.stack_out:
            return self.stack_out.pop()
        else:
            while self.stack_in:
                ans = self.stack_in.pop()
                self.stack_out.append(ans)
            return self.stack_out.pop() 

    def peek(self):
        if self.empty():
            return None
        
        ans = self.pop()
        self.stack_out.append(ans)
        
        return ans

    def empty(self):
        return not(self.stack_in or self.stack_out)
    
mq = MyQueue()

a1 = mq.push(1)
a2 = mq.push(2)
a3 = mq.peek()
a4 = mq.pop()
a5 = mq.empty()

print(a1, a2, a3, a4, a5)