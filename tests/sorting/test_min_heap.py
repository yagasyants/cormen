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
        
    def test_extract_min_normal(self):
        self.mh.insert_all([2, 100, 10, 1, 7, 8, 16])
        
        min_extracted_1 = self.mh.extract_min()
        min_extracted_2 = self.mh.extract_min()
        min_after = self.mh.minimum()
        
        self.assertEqual(1, min_extracted_1)
        self.assertEqual(2, min_extracted_2)
        self.assertEqual(7, min_after)
        
    def test_extract_min_three_values(self):
        self.mh.insert(10)
        self.mh.insert(400)
        self.mh.insert(15)
        
        min_extracted = self.mh.extract_min()
        self.mh.insert(30)
        min_after = self.mh.minimum()
        
        self.assertEqual(10, min_extracted)
        self.assertEqual(15, min_after)
        
    def test_size(self):
        size_before_insert = self.mh.size()

        self.mh.insert_all([30,20])
        size_after_insert = self.mh.size()

        self.mh.extract_min()
        self.mh.extract_min()
        size_after_extract = self.mh.size()

        self.assertEquals(0, size_before_insert)
        self.assertEquals(2, size_after_insert)
        self.assertEquals(0, size_after_extract)
         
    def test_pair_holder(self):
        pair_holder = min_heap.PairHolder(1, 11)    
        
        self.assertEquals(1, pair_holder.val)
        self.assertEquals(11, pair_holder.holded_val)
             
    def test_pair_holder_lt(self):
        pair_holder_2 = min_heap.PairHolder(2, 3)    
        pair_holder_1 = min_heap.PairHolder(1, 11)    
        
        self.assertTrue(pair_holder_1 < pair_holder_2)

    def test_pair_holder_gt(self):
        pair_holder_2 = min_heap.PairHolder(2, 3)    
        pair_holder_1 = min_heap.PairHolder(1, 11)    
        
        self.assertTrue(pair_holder_2 > pair_holder_1)
             
    def test_heap_of_pair_holders(self):
        self.mh.insert(min_heap.PairHolder(2, 3))    
        
        self.assertEquals(2, self.mh.minimum().val)
        
    def test_print(self):
        self.mh.insert_all([1,2,3,4,5,6,7,0,9,20,8,77,55,44])
                
        self.mh.print_heap()
        
                
    def setUp(self):
        self.mh = min_heap.MinHeap()