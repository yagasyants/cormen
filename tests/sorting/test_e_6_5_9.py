import unittest
from sorting import e_6_5_9

class TestE659(unittest.TestCase):
    def test_merge_two(self):
        l1 = [1, 4, 10]
        l2 =  [5, 8, 15]
        
        merged = e_6_5_9.merge_sorted([l1, l2])
        
        self.assertEqual([1, 4, 5, 8, 10, 15], merged)
        
    def test_merge_three(self):
        l1 = [1, 4, 10, 30]
        l2 =  [5, 8, 15]
        l3 =  [200, 300, 400]
        
        merged = e_6_5_9.merge_sorted([l3, l1, l2])
        
        self.assertEqual([1, 4, 5, 8, 10, 15, 30, 200, 300, 400], merged) 
    
