class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,element):
        self.queue.append(element)
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.queue.pop(0)
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.queue[0]
    def isEmpty(self):
        return len(self.queue)==0
    def size(self):
        return len(self.queue)
myQueue = Queue()

myQueue.enqueue('a')
myQueue.enqueue('b')
myQueue.enqueue('c')
myQueue.enqueue('d')
print("Queue is", myQueue.queue)
print("Peek is", myQueue.peek())
print("Dequeue is", myQueue.dequeue())
print("After Dequeue is",myQueue.queue)
print("isEmpty ", myQueue.isEmpty())
print("Size of Queue is",myQueue.size())