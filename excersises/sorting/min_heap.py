from math import * 

class MinHeap(object):

    def __init__(self):
        self.arr = []
        print('initialized')
    
    def insert(self, el):
        self.arr.append(el + 1)
        self.decrease_key(len(self.arr) -1, el)
        
    def minimum(self):
        return self.arr[0]

    def decrease_key(self, index, new_val):
        if new_val > self.arr[index] :
            raise Exception('new_val should be less than element in index')
        self.arr[index] = new_val
        while index > 0 and self.arr[self.__parent(index)] > self.arr[index] :
            parent_old_val = self.arr[self.__parent(index)]
            self.arr[self.__parent(index)] = self.arr[index]
            self.arr[index] = parent_old_val
            index = self.__parent(index)
    
    def insert_all(self, listEl):
        for el in listEl :
            self.insert(el)

    def genIndent(self, i, lastPower):
        indentSize = 2 * (lastPower - i - 1) - 1
        indent = ''
        for i in range(0, indentSize) :
            indent += '_'
        return indent
    def genDelim(self, i, lastPower):
        if i == lastPower - 1:
            return '_'
        else:
            return '___'
        
    def printHeap(self):
        lastPower = int(ceil(log(len(self.arr),2)))
        for i in range(0, lastPower) :
            minIndex =  int(pow(2, i)) - 1
            maxIndex = min(int(pow(2, i+1)) - 1, len(self.arr))
            line = ''
            indent = self.genIndent(i, lastPower) 
            for j in range(minIndex,maxIndex):             
                line += str( self.arr[j] ) + self.genDelim(i, lastPower)
            
            print(indent + line)

    def __parent(self,i):
        return i // 2
    def __left(self, i):
        return 2 * i
    def __right(self, i):
        return 2 * i + 1
   
'''    
mh = MinHeap()
mh.insert_all([1,2,3,4,5,6,7,0,9,2,6,7,5,4])

mh.printHeap()
 
1,2,3,4,5,6,7,8,9,10
    1
  2    3
4 5  6 7

8 9 10
'''