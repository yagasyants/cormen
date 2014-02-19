from collections import deque

'''
10.1-6
Show how to implement a queue using two stacks. Analyze the running time of the queue operations.
'''

class Stack(object):
    
    def __init__(self):
        self.source = deque([])
        self.buffer = deque([])
    
    def push(self, el):
        self.source.append(el)
        
    def pop(self):
        if(len(self.source)==0):
            raise IndexError("Pop from empty stack")
        else:
            lastIn = self._move_to_buffer_ret_lats()
            self._switch_queues()
            return lastIn
            
    def _move_to_buffer_ret_lats(self):
        while(len(self.source) > 1):
            el = self.source.popleft()
            self.buffer.append(el)
        return self.source.popleft()
        
    def _switch_queues(self):
        new_source = self.buffer
        self.buffer = self.source
        self.source = new_source
        
