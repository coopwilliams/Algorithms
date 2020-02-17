#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

def eating_cookies(n, cache=[]):
    """Count how many ways Cookie Monster can eat n cookies"""
    def eating_cookies_iter(n):
        # make cache available to nested calls
        nonlocal computed
        if computed[n] != 0:
            # return cached values
            return computed[n]
        # up to 3 cookies can be eaten at once
        capacity = [1, 2, 3]
        count = 0
        for i in capacity[:n-1]:
            # number of ways Monster can continue after eating i in first bite
            endings = eating_cookies_iter(n - i)
            count += endings
        # count cases where all are eaten in the first bite
        if n < 4:
            count += 1
        # write to cache
        if computed[n] == 0:
            computed[n] = count
        return count

    computed = cache or [1, 1]+[0 for x in range(n - 1)]
    return eating_cookies_iter(n)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
