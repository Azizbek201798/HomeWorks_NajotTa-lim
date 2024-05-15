# Task - 2; || 232 - Implement-queue-using-stacks;

# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.

class MyQueue(object):

    def __init__(self):
        self.queue = []
        self.tmp = []

    def push(self, x):
        while not len(self.queue) == 0:
            self.tmp.append(self.queue.pop())
        self.queue.append(x)
        while not len(self.tmp) == 0:
            self.queue.append(self.tmp.pop())

    def pop(self):
        return self.queue.pop()
        
    def peek(self):
        return self.queue[len(self.queue)-1]
        
    def empty(self):
        return len(self.queue) == 0