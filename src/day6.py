import unittest
import utils

test_input = utils.inputlist('../test_input/06.txt')
input = utils.inputlist('../input/day6.txt')

def calculate_wins(time, distance):
  total = 0
  for c in range(1, time):
      if c * (time - c) > distance:
        total += 1
  return total

def part_1(input):
  times = [int(i) for i in input[0].split()[1:]]
  distances = [int(i) for i in input[1].split()[1:]]
  total = 1
  
  for t, time in enumerate(times):
    distance = distances[t]
    win_conditions = calculate_wins(time, distance)
    total *= win_conditions

  return total

def part_2(input):
  time = int(''.join(input[0].split()[1:]))
  distance = int(''.join(input[1].split()[1:]))

  return calculate_wins(time, distance)

def main():
  print(f'Part 1: {part_1(input)}')
  print(f'Part 2: {part_2(input)}')
  unittest.main()

class TestSolutions(unittest.TestCase):
  def test_p1(self):
    self.assertEqual(part_1(test_input), 288)

  def test_p2(self):
    self.assertEqual(part_2(test_input), 71503)

if __name__ == '__main__':
  main()