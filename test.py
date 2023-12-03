import unittest
from src import utils, day1, day2

day1_input = utils.inputlist('../test_input/01.txt')
day1_2_input = utils.inputlist('../test_input/01.2.txt')
day2_input = utils.inputlist('../test_input/02.txt')

class TestSolutions(unittest.TestCase):
  def test_day1_1(self):
    self.assertEqual(day1.part_1(day1_input), 142)

  def test_day1_2(self):
     self.assertEqual(day1.part_2(day1_2_input), 281)

  def test_day2_1(self):
     self.assertEqual(day2.part_1(day2_input), 8)

  def test_day2_2(self):
     self.assertEqual(day2.part_2(day2_input), 2286)

if __name__ == '__main__':
    unittest.main()