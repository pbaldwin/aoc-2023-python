import re
from dataclasses import dataclass, astuple
from functools import reduce

@dataclass
class Rectangle:
  x: int
  y: int
  w: int
  value: int or str

def parse_nums(input):
  state = []

  for y, line in enumerate(input):
    for m in re.finditer(r'\d+', line):
      x1, x2 = m.span()
      x = x1 if x1 == 0 else x1 - 1
      w = x2 - x1 + 1
      state.append(Rectangle(x, y, w, int(m[0])))
  
  return state

def parse_symbols(input):
  state = []

  for y, line in enumerate(input):
    for m in re.finditer(r'[^.\w\s]', line):
      x1, x2 = m.span()
      x = x1 if x1 == 0 else x1 - 1
      w = x2 - x1 + 1
      state.append(Rectangle(x, y, w, m[0]))
  
  return state

def detect_collision(rect_1, rect_2):
  x1, y1, w1, _1 = astuple(rect_1)
  x2, y2, w2, _2 = astuple(rect_2)

  return (x1 + w1 >= x2 + 1 and # rect_1 right edge past rect_2 left
          x1 <= x2 + w2 - 1 and # rect_1 left edge past rect_2 right
          abs(y1 - y2) <= 1) # rect_1 row within 1 of rect_2 row

def part_1(input):
  nums = parse_nums(input)
  symbols = parse_symbols(input)
  sum = 0

  for num in nums:
    for symbol in symbols:
      if detect_collision(num, symbol):
        sum += num.value
        break
  
  return sum

def part_2(input):
  nums = parse_nums(input)
  symbols = parse_symbols(input)
  sum = 0

  for symbol in symbols:
    ratios = []
    if symbol.value == '*':
      for num in nums:
        if detect_collision(symbol, num):
          ratios.append(num.value)
      
      if len(ratios) == 2:
        sum += reduce(lambda x, y: x * y, ratios)
  
  return sum
