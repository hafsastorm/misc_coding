from bunny import *
import unittest as test

'''
Test cases for bunny.py
'''
class bunny_test(test.TestCase):
  # Test even rows x odd columns
  def test_even_x_odd(self):
    a = [ [5, 7, 8, 6, 3],
          [0, 0, 7, 0, 4],
          [4, 6, 3, 4, 9],
          [3, 1, 0, 5, 8]
        ]
    self.assertEqual(eat_carrots(a), 27)
  # Test odd rows x even columns
  def test_odd_x_even(self):
    b = [ [5, 7, 8, 6],
          [0, 0, 7, 0],
          [4, 6, 3, 9],
          [3, 0, 5, 8],
          [1, 0, 0, 0]
        ]
    self.assertEqual(eat_carrots(b), 14)
  # Test even rows x even columns
  def test_even_x_even(self):
    c = [ [5, 7, 3, 6],
          [6, 2, 4, 0],
          [1, 6, 3, 9],
          [3, 0, 5, 8]
        ]
    self.assertEqual(eat_carrots(c), 31)
  # Test odd rows x odd columns
  def test_odd_x_odd(self):
    d = [ [5, 2, 4, 0, 9],
          [0, 0, 3, 0, 3],
          [4, 0, 2, 2, 4],
          [3, 1, 2, 5, 2],
          [8, 0, 0, 3, 2]
        ]
    self.assertEqual(eat_carrots(d), 16)
  # Test smallest square possible
  def test_smallest_even_square(self):
    e = [ [1, 0],
          [1, 1]
        ]
    self.assertEqual(eat_carrots(e), 3)
  # Test smallest number of columns possible
  def test_smallest_cols(self):
    f = [ [1], 
          [3] 
        ]
    self.assertEqual(eat_carrots(f), 4)
  # Test smallest number of rows possible
  def test_smallest_rows(self):
    g = [ [8, 3] ]
    self.assertEqual(eat_carrots(g), 11)
  # Test empty field
  def test_empty_field(self):
    h = [ [0, 0],
          [0, 0] 
        ]
    self.assertEqual(eat_carrots(h), 0)

  def test_smallest_field(self):
    i = [ [10] ]
    self.assertEqual(eat_carrots(i), 10)
