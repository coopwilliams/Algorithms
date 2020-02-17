#!/usr/bin/python

import sys

def making_change(amount, n_coins):
    def cc(amount, n_coins=5):
        """Count ways to make change with up to 5 coins"""
        if amount == 0: return 1
        elif (amount < 0) or (n_coins == 0): return 0
        else:
            return  cc(amount, n_coins - 1) + \
                    cc(amount - first_denomination[n_coins], n_coins)

    def cc_missing_denominations(amount, n_coins):
        """Count ways to make change with gaps in the denominations.
                E.g. pennies and dimes only (no nickels).
        """
        if amount == 0: return 1
        elif (amount < 0) or (len(n_coins) == 0): return 0
        else:
            return  cc_missing_denominations(amount, sorted(n_coins)[:-1]) + \
                    cc_missing_denominations(amount - max(n_coins), n_coins)

    first_denomination = {1:1, 2:5, 3:10, 4:25, 5:50}
    # check there are no gaps in the denominations
    if n_coins == list(first_denomination.values())[:len(n_coins) - 1]:
        n_coins = len(n_coins)
        return cc(amount, n_coins)
    else:
        return cc_missing_denominations(amount, n_coins)

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    # extra arguments can be passed to specify arbitrary denominations
    denominations = [int(x) for x in sys.argv[2:len(sys.argv)]] \
                    or [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents with denominations {denominations}.".format(ways=making_change(amount, denominations), amount=amount, denominations=denominations))
  else:
    print("Usage: making_change.py [amount]")
