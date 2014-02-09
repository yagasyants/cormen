import unittest
from  sorting import min_heap

class Test(unittest.TestCase):

    def test_insert_min(self):
        self.mh.insert(1)
        
        minEl = self.mh.minimum()
        
        self.assertEqual(1, minEl)
    
    def test_decrease_key_simple(self):
        self.mh.insert(10)
        self.mh.decrease_key(0,9)

        minEl = self.mh.minimum()
        self.assertEqual(9, minEl)

    def test_insert_several_check_min(self):
        self.mh.insert_all([2, 100, 10, 1, 7, 8, 16])
        
        minEl = self.mh.minimum()
        
        self.assertEqual(1, minEl)
        
    def test_print(self):
        self.mh.insert_all([1,2,3,4,5,6,7,0,9,20,8,77,55,44])
                
        self.mh.printHeap()        
             
    def setUp(self):
        self.mh = min_heap.MinHeap()