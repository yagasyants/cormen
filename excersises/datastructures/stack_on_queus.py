from collections import deque

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
        
