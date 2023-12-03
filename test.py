import unittest
from src import utils
from src import day1

day1_input = utils.inputlist('../test_input/01.txt')
day1_2_input = utils.inputlist('../test_input/01.2.txt')

class TestSolutions(unittest.TestCase):
  def test_day1_01(self):
    self.assertEqual(day1.part_1(day1_input), 142)

  def test_day1_02(self):
     self.assertEqual(day1.part_2(day1_2_input), 281)

if __name__ == '__main__':
    unittest.main()