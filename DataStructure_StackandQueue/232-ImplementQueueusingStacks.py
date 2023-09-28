# class Queue():
#     def __init__(self):
#         self.stack_in = []
#         self.stack_out = []

#     def push(self, x:int):
#         self.stack_in.append(x)
    
#     def pop(self):
#         if self.empty():
#             return None
#         if self.stack_out:
#             return self.stack_out.pop()
#         else:
#             for i in range(len(self.stack_in)):
#                 self.stack_out.append(self.stack_in.pop())
#             return self.stack_out.pop()

#     def peek(self):
#         ans = self.pop()
#         self.stack_out.append(ans)
#         return ans

#     def empty(self):
#         if len(self.stack_in) == 0 and len(self.stack_out) == 0:
#             return True
#         else:
#             return False
    
#     def __str__(self) -> str:
#         return f'StackIn:{self.stack_in}, StackOut:{self.stack_out}'
    
# queue = Queue()

# queue.push(1)
# print(queue)

# queue.push(2)
# print(queue)
# param_2 = queue.peek()
# print(param_2)
# param_3 = queue.pop()

# print(param_3)
# param_4 = queue.empty()

# print(param_4)

# # 2023.9.12(10:41:16)
# class Solution():
#     def __init__(self) -> None:
#         self.stack_in = []
#         self.stack_out = []

#     def push(self, x: int):
#         self.stack_in.append(x)
    
#     def pop(self):
#         if self.empty():
#             return None
#         if self.stack_out:
#             return self.stack_out.pop()
#         else:
#             for _ in range(len(self.stack_in)):
#                 self.stack_out.append(self.stack_in.pop())
#             return self.stack_out.pop()
            
#     def peek(self):
#         ans = self.pop()
#         self.stack_out.append(ans)
#         return ans
    
#     def empty(self):
#         return not (self.stack_in or self.stack_out)
    
# sol = Solution()
# res1 = sol.push(1)

# res2 = sol.push(2)
# print(res2)

# res3 = sol.peek()
# print(res3)

# res4 = sol.pop()
# print(res4)

# res5 = sol.empty()
# print(res5)

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