from collections import deque

class Mystack():
    def __init__(self) -> None:
        self.queue = deque()

    def push(self, x: int):
        self.queue.append(x)
    
    def pop(self):
        if self.empty():
            return None
        else:
            for i in range(len(self.queue) - 1):
                self.queue.append(self.queue.popleft())
            return self.queue.popleft() 
        
        # for i in range(len(self.queue) - 1):
        #         self.queue.append(self.queue.popleft())
        # return self.queue.popleft()
    
    def top(self):
        if self.empty():
            return None
        else:
            return self.queue[-1]
        
    def empty(self):
        if self.queue:
            return False
        else:
            return True
        # return not self.queue

    def __str__(self) -> str:
        return f'Mystack:{self.queue}'

stack1 = Mystack()

stack1.push(1)
print(stack1)

stack1.push(2)
print(stack1)

res1 = stack1.top()
print(res1)

res2 = stack1.pop()
print(res2)

res3 = stack1.empty()
print(res3)
