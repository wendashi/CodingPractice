class Queue():
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x:int):
        self.stack_in.append(x)
    
    def pop(self):
        if self.empty():
            return None
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self):
        ans = self.pop()
        self.stack_out.append(ans)
        return ans

    def empty(self):
        if len(self.stack_in) == 0 and len(self.stack_out) == 0:
            return True
        else:
            return False
    
    def __str__(self) -> str:
        return f'StackIn:{self.stack_in}, StackOut:{self.stack_out}'
    
queue = Queue()

queue.push(1)
print(queue)

queue.push(2)
print(queue)
param_2 = queue.peek()
print(param_2)
param_3 = queue.pop()

print(param_3)
param_4 = queue.empty()

print(param_4)