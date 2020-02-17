#!/usr/bin/python

import argparse

def find_max_profit(prices):
    # set starting max to a profit that's at least possible (max may be < 0)
    max_profit = prices[1] - prices[0]
    # for every possible selling point, find the biggest spread
    reversal = list(reversed(prices))
    for pos, i in enumerate(reversal[:-1]): # can't sell at the first price
        max_for_pair = i - min(reversal[pos + 1:]) # can't sell right after buying 
        max_profit = max(max_profit, max_for_pair)
    return max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
