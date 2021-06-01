import unittest
import random
import list_comprehension as lc


class UnitTests(unittest.TestCase):
  def setUp(self):
    self.x = random.randint(0, 100)
    self.y = random.randint(0, 100)


  def test_simple_list_range(self):
    list = lc.simple_list_range(self.x)
    self.assertEqual(len(list), self.x)
    self.assertEqual(list[self.x - 1], self.x - 1)

  def double_list_comprehension_range(self):
    list = lc.double_list_comprehension_range(self.x, self.y)
    self.assertEqual(len(list), self.x * self.y)
    self.assertEqual(list[self.x - 1], (self.x - 1, self.y - 1))

if __name__ == "__main__":
    unittest.main()