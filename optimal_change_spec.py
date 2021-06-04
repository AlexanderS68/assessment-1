import unittest
from optimal_change import optimal_change

class OptimalChange(unittest.TestCase):

  #Test that correct format is returned
  def test_return_a_str(self):
    self.assertEqual(type(optimal_change(1, 6)), str)
    self.assertEqual(type(optimal_change(10, 45.57)), str)
  
  #Test correct change is given
  def test_return_value(self):
    self.assertTrue(optimal_change(62.13, 100), 'The optimal change for an item that costs $62.13 with an amount paid of $100 is, 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 $0.25 cents, 1 $0.1 cent, 1 $0.01 cent.')
    self.assertTrue(optimal_change(23.45, 51.89), 'The optimal change for an item that costs $23.45 with an amount paid of $51.89 is, 1 $20 bill, 1 $5 bill, 3 $1 bills, 1 $0.25 cent, 1 $0.1 cent, 1 $0.05 cent, 4 $0.01 cents.')
  

  def test_edge_case(self):
    self.assertEqual(optimal_change(100, 10), 'Insufficent funds')


if __name__ == '__main__':
  unittest.main()