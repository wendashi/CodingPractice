# from collections import deque

# class Mystack():
#     def __init__(self) -> None:
#         self.queue = deque()

#     def push(self, x: int):
#         self.queue.append(x)
    
#     def pop(self):
#         if self.empty():
#             return None
#         else:
#             for i in range(len(self.queue) - 1):
#                 self.queue.append(self.queue.popleft())
#             return self.queue.popleft() 
#         # else:
#         #    return self.que.pop()
    
#     def top(self):
#         if self.empty():
#             return None
#         else:
#             return self.queue[-1]
        
#     def empty(self):
#         if self.queue:
#             return False
#         else:
#             return True
#         # return not self.queue

#     def __str__(self) -> str:
#         return f'Mystack:{self.queue}'

# stack1 = Mystack()

# stack1.push(1)
# print(stack1)

# stack1.push(2)
# print(stack1)

# res1 = stack1.top()
# print(res1)

# res2 = stack1.pop()
# print(res2)

# res3 = stack1.empty()
# print(res3)

from collections import deque

class Mystack():
    def __init__(self) -> None:
        self.que = deque()

    def push(self, x: int):
        self.que.append(x)
    
    def pop(self):
        if self.empty():
            return None
        else:
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

stack = Mystack()

stack.push(1)
stack.push(2)

res1 = stack.top()
print(res1)

res2 = stack.pop()
print(res2)

res3 = stack.empty()
print(res3)

# 1. 因为deque的pop操作也是常数时间；
# 2. 通过deque来存储元素，空间复杂度不会随着元素数量的增加而线性增加，因为deque是一个动态数组，它会根据需要自动扩展其内部数组的大小。
# 如果用一个固定大小的数组来实现栈，那么空间复杂度可能会是O(n)，因为数组的大小是固定的，会随着元素数量的增加而线性增加。
# 但是在这个特定的实现中，使用了deque，它的内部实现是动态的，因此空间复杂度是恒定的，不会随着元素数量的增加而线性增加。

# - 时间复杂度: 都是O(1)
# - 空间复杂度: 都是O(1)
