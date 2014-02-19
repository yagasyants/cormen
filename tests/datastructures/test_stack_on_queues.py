import unittest
from datastructures import stack_on_queus

class Test(unittest.TestCase):


    def testPushPopOneElement(self):
        stack = stack_on_queus.Stack()
        stack.push(1)
        
        el = stack.pop()
        
        self.assertEqual(1, el)

    def testPushPopTwoElement(self):
        stack = stack_on_queus.Stack()
        stack.push(1)
        stack.push(2)
        
        el1 = stack.pop()
        el2 = stack.pop()
        
        self.assertEqual(2, el1)
        self.assertEqual(1, el2)

    def testPopEmpty(self):
        stack = stack_on_queus.Stack()
        with self.assertRaises(IndexError):
            stack.pop()
            
    def testPushPopDiffOrder(self):
        stack = stack_on_queus.Stack()
        stack.push(1)
        stack.push(2)
        
        el1 = stack.pop()
        stack.push(3)
        el2 = stack.pop()
        stack.push(4)
        el3 = stack.pop()
        el4 = stack.pop()
        
        self.assertEqual(2, el1)
        self.assertEqual(3, el2)
        self.assertEqual(4, el3)
        self.assertEqual(1, el4)
