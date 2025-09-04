class Stack:
    def __init__(self):
        self.stack = []
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack.pop()
    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
        
myStack = Stack()
myStack.push('a')
myStack.push('b')
myStack.push('c')
myStack.push('d')
myStack.push('e')

print("Stack :", myStack.stack)
print("Pop", myStack.pop())
print("Stack after pop", myStack.stack)
print("Peek", myStack.peek())
print("Stack after peek:", myStack.peek())
print("isEmpty", myStack.isEmpty())
print("Size", myStack.size())