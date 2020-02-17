#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    list_length_n = {0:[[]], 1:[['rock'], ['paper'], ['scissors']]}
    options = ['rock', 'paper', 'scissors']
    def rock_paper_scissors_iter(n):
        nonlocal list_length_n, options
        # use cache if list already calculated
        if n in list_length_n.keys():
            return list_length_n[n]
        new_list = []
        # each play from n - 1 can now start with one of three options
        for i in options:
            new_list.extend([[i] + x for x in rock_paper_scissors_iter(n - 1)])
        # update cache
        list_length_n[n] = new_list
        return new_list
    return rock_paper_scissors_iter(n)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
