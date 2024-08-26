class Stack:
    def __init__(self) -> None:
        self.stack = []
    
    def check_empty(self):
        return (len(self.stack) == 0)
    
    def push(self, item):
        self.stack.append(item)
        print(f'Pushed item: {item}')
    
    def pop(self):
        if self.check_empty():
            return 'stack is empty'
        
        return self.stack.pop()
    
stack = Stack()
stack.push(str(1))
stack.push(str(2))
stack.push(str(3))
stack.push(str(4))
stack.push(str(5))

print(f'Popped item: {stack.pop()}')
print(f'Stack after popping of an item: {stack.stack}')
