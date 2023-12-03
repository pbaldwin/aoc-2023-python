import os

dir = os.path.dirname(__file__)

def inputlist(filename):
  path = os.path.join(dir, filename)
  with open(path) as f:
    lines = [ line.strip() for line in f ]

  return lines