from parse import compile, search, with_pattern

@with_pattern(r'(red|green|blue)')
def parse_color(text):
  return text

p = compile('{number:d} {color:Color}', { 'Color': parse_color })

def part_1(input):
  sum = 0
  max = {
    'red' : 12,
    'green' : 13,
    'blue' : 14,
  }
  
  for game in input:
    possible = True
    id = search('Game {:d}:', game)[0]
    
    for r in p.findall(game):
      if r['number'] > max[r['color']]:
        possible = False
        break
    
    if possible:
      sum += id
  
  return sum

def part_2(input):
  sum = 0

  for game in input:
    power = 1
    min = {
      'red': 0,
      'blue': 0,
      'green': 0,
    }

    for r in p.findall(game):
      if r['number'] > min[r['color']]:
        min[r['color']] = r['number']
    
    for _, value in min.items():
      power *= value

    sum += power
    
  return sum