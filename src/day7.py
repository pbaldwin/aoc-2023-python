import unittest
import utils
from dataclasses import dataclass
from functools import reduce

class Hand:
  hands = {
    '11111': 0, # high card
    '2111': 1,  # one pair
    '221': 2,   # two pair
    '311': 3,   # three of a kind
    '32': 4,    # full house
    '41': 5,    # 4 of a kind
    '5': 6,     # five of a kind
  }

  def __init__(self, cards, bid):
    self.cards = cards
    self.bid = int(bid)
    self.value = ''.join(str(c) for c in cards)
    self.type = Hand.parse_hand(cards)

  # returns hand type value
  @classmethod
  def parse_hand(cls, cards):
    cards_d = {}
    for card in cards:
      cards_d[card] = cards_d.get(card, 0) + 1

    # Check for jokers
    if cards_d.get('01'):
      mod = cards_d['01']
      del cards_d['01']
      
      if mod == 5: # Five of a kind jokers
        cards_d['14'] = 5
      else:
        highest = sorted(cards_d.items(), key= lambda c: c[1])[-1][0]
        cards_d[highest] += mod
    
    return Hand.hands[''.join(str(i) for i in sorted(cards_d.values(), reverse=True))]

class CardValue(dict):
  def __init__(self):
    self['T'] = '10'
    self['J'] = '11'
    self['Q'] = '12'
    self['K'] = '13'
    self['A'] = '14'
  def __missing__(self, key):
    self[key] = f'0{key}' # leftpad
    return self[key]
  
class JokersValue(CardValue):
  def __init__(self):
    super().__init__()
    self['J'] = '01'

def parse_hands(data, values):
  hands = [[] for __ in range(7)]

  for line in data:
    cards, bid = line.split()
    cards = [values[c] for c in cards]
    hand = Hand(cards, bid)
    hands[hand.type].append(hand)

  return hands

def part_1(input):
  values = CardValue()
  hands = parse_hands(input, values)
  total = 0

  hands_s = [hand for sub_hands in hands for hand in sorted(sub_hands, key=lambda h: h.value)]

  for rank, hand in enumerate(hands_s):
    total += (rank + 1) * hand.bid

  return total

def part_2(input):
  values = JokersValue()
  hands = parse_hands(input, values)
  total = 0

  hands_s = [hand for sub_hands in hands for hand in sorted(sub_hands, key=lambda h: h.value)]

  for rank, hand in enumerate(hands_s):
    total += (rank + 1) * hand.bid

  return total

class Day7Tests(unittest.TestCase):
  def test_p1(self):
    test_input = utils.inputlist('../test_input/07.txt')
    self.assertEqual(part_1(test_input), 6440)

  def test_p2(self):
    test_input = utils.inputlist('../test_input/07.txt')
    self.assertEqual(part_2(test_input), 5905)

def main():
  input = utils.inputlist('../input/day7.txt')

  print(f'Day 7 Part 1: {part_1(input)}')
  print(f'Day 7 Part 2: {part_2(input)}')
  unittest.main()

if __name__ == '__main__':
  main()