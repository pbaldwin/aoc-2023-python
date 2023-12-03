import re

def part_1(input):
  sum = 0
  
  for line in input:
    nums = re.findall(r'\d', line)
    sum += int(nums[0]+nums[-1])
  
  return sum

def to_num_string(arg):
  try:
    return str(['one','two','three','four','five','six','seven','eight','nine'].index(arg) + 1)
  except:
    return arg

def part_2(input):
  sum = 0

  for line in input:
    nums = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)
    first_last = [to_num_string(nums[0]), to_num_string(nums[-1])]
    sum += int(''.join(first_last))

  return sum