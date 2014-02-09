import math 

class MinHeap(object):

    def __init__(self):
        self.arr = []
    
    def insert(self, el):
        self.arr.append(el + 1)
        self.decrease_key(len(self.arr) -1, el)
        
    def minimum(self):
        return self.arr[0]

    def decrease_key(self, index, new_val):
        if new_val > self.arr[index] :
            raise Exception('new_val should be less than element in index')
        self.arr[index] = new_val
        while index > 0 and self.arr[self._parent(index)] > self.arr[index] :
            parent_old_val = self.arr[self._parent(index)]
            self.arr[self._parent(index)] = self.arr[index]
            self.arr[index] = parent_old_val
            index = self._parent(index)
    
    def insert_all(self, list_el):
        for el in list_el :
            self.insert(el)

    def _gen_indent(self, i, last_power):
        indent_size = 2 * (last_power - i - 1) - 1
        indent = ''
        for i in range(0, indent_size) :
            indent += '_'
        return indent

    def _gen_delim(self, i, last_power):
        if i == last_power - 1:
            return '_'
        else:
            return '___'
        
    def print_heap(self):
        last_power = int(math.ceil(math.log(len(self.arr),2)))
        for i in range(0, last_power) :
            min_index =  int(pow(2, i)) - 1
            max_index = min(int(pow(2, i+1)) - 1, len(self.arr))
            line = ''
            indent = self._gen_indent(i, last_power) 
            for j in range(min_index,max_index):             
                line += str( self.arr[j] ) + self._gen_delim(i, last_power)
            
            print(indent + line)

    def _parent(self,i):
        return i // 2
    
    def _left(self, i):
        return 2 * i
    
    def _right(self, i):
        return 2 * i + 1
   
'''    
mh = MinHeap()
mh.insert_all([1,2,3,4,5,6,7,0,9,2,6,7,5,4])

mh.print_heap()
 
1,2,3,4,5,6,7,8,9,10
    1
  2    3
4 5  6 7

8 9 10
'''