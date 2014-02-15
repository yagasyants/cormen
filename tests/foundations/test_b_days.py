import unittest
from foundations import b_days

class Test_calc(unittest.TestCase):
    def test_calc_1(self):
        prob = b_days.calc(1)
        self.assertEquals(0, prob)

    def test_calc_2(self):
        prob = b_days.calc(2)
        self.assertAlmostEqual( 1.0/365, prob, 3)

    def test_calc_5(self):
        prob = b_days.calc(5)
        self.assertAlmostEqual(0.027, prob, 3)
        
    def test_calc_23(self):
        prob = b_days.calc(23)
        print("Probability for 23 is " + str(prob))
        self.assertTrue(prob > 0.5)

