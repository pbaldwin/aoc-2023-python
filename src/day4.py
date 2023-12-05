from parse import compile

def parse_list(nums):
  return nums.strip().split()

p = compile('Card{}:{part1:List}|{part2:List}', {'List': parse_list})

def get_matches(line):
  parts = p.parse(line)
  un, do = parts.named.values()
  total_len = len(un + do)
  
  return total_len - len(set(un + do))

def double_recursive(n):
  if n <= 1:
    return n
  
  return 2 * double_recursive(n - 1)

def part_1(input):
  scores = []

  for line in input:
    matches = get_matches(line)
    scores.append(double_recursive(matches))

  return sum(scores)

def part_2(input):
  cards = [1] * len(input)

  for li, line in enumerate(input):
    instances = cards[li]
    matches = get_matches(line)

    if matches:
      next = li + 1
      for i in range(next, next + matches):
        cards[i] += instances

  return sum(cards)