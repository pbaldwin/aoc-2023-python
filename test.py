import unittest
from src import utils, day1, day2, day3, day4

day1_input = utils.inputlist('../test_input/01.txt')
day1_2_input = utils.inputlist('../test_input/01.2.txt')
day2_input = utils.inputlist('../test_input/02.txt')
day3_input = utils.inputlist('../test_input/03.txt')
day4_input = utils.inputlist('../test_input/04.txt')

class TestSolutions(unittest.TestCase):
  def test_day1_1(self):
    self.assertEqual(day1.part_1(day1_input), 142)

  def test_day1_2(self):
     self.assertEqual(day1.part_2(day1_2_input), 281)

  def test_day2_1(self):
     self.assertEqual(day2.part_1(day2_input), 8)

  def test_day2_2(self):
     self.assertEqual(day2.part_2(day2_input), 2286)

  def test_day3_1(self):
     self.assertEqual(day3.part_1(day3_input), 4361)

  def test_day3_2(self):
     self.assertEqual(day3.part_2(day3_input), 467835)

  def test_day4_1(self):
     self.assertEqual(day4.part_1(day4_input), 13)

  def test_day4_2(self):
     self.assertEqual(day4.part_2(day4_input), 30)

if __name__ == '__main__':
    unittest.main()