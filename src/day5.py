import unittest
from dataclasses import dataclass
from parse import parse, findall

@dataclass
class Converter:
  dest_start: int
  src_start: int
  src_end: int

class ConversionMap:
  def __init__(self, ranges, name):
    self.name = name
    self.converters = []

    for entry in ranges:
      dest_start, src_start, length = [int(i) for i in entry.split()]
      self.converters.append(Converter(dest_start, src_start, src_start + length))

  def get_dest(self, src):
    for con in self.converters:
      if con.src_start <= src < con.src_end:
        return abs(con.src_start - src) + con.dest_start
    
    return src

    
def parse_input(input):
  seeds = parse('seeds: {}', input[0])[0]
  curr_map = []
  map_data = []

  for i, line in enumerate(input[2:]):
    if not line: # If line is empty, start a new map entry
      map_data.append(curr_map)
      curr_map = []
    else:
      curr_map.append(line)
  else:
    map_data.append(curr_map)

  return seeds, map_data

def parse_map(data):
  name = parse('{} map:', data[0])[0]
  ranges = data[1:]
  return ConversionMap(ranges, name)

def part_1(input):
  seeds, map_data = parse_input(input)
  smallest = None
  conv_maps = list(map(parse_map, map_data))

  for seed in seeds.split():
    dest = int(seed)
    for m in conv_maps:
      dest = m.get_dest(dest)
    
    if not smallest or dest < smallest:
      smallest = dest

  return smallest

def part_2(input):
  seed_ranges, map_data = parse_input(input)
  smallest = None
  conv_maps = list(map(parse_map, map_data))
  
  for m in findall('{start:d} {end:d}', seed_ranges):
    start, end = m.named.values()
    for seed in range(start, start + end):
      dest = seed
      for mp in conv_maps:
        dest = mp.get_dest(dest)
      
      if not smallest or dest < smallest:
        smallest = dest

  return smallest


class TestSolutions(unittest.TestCase):
  def test_conversion(self):
    name = 'test'
    ranges = ['50 98 2', '52 50 48']

    test_map = ConversionMap(ranges, name)

    self.assertEqual(test_map.get_dest(98), 50)
    self.assertEqual(test_map.get_dest(99), 51)

  def test_parse_map(self):
    data = ['seed-to-soil map:', '50 98 2', '52 50 48']
    test_map = parse_map(data)

    self.assertEqual(test_map.name, 'seed-to-soil')
    self.assertEqual(test_map.get_dest(98), 50)
    self.assertEqual(test_map.get_dest(99), 51)

if __name__ == '__main__':
  unittest.main()