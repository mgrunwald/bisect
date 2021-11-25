#!/usr/bin/env python3
"""Main application for the bisect tool"""

import argparse
from bisect.bisect import Bisect

parser = argparse.ArgumentParser(
    description="Bisect a sequence of low/high numbers")
parser.add_argument(
    'numbers',
    metavar='N',
    type=float,
    nargs='+',
    help=
    'two numbers: start bisecting in that range. One number: start by finding a range, then bisect'
)

args = parser.parse_args()

if len(args.numbers) == 1:
    bisect = Bisect(current=args.numbers[0])
elif len(args.numbers) == 2:
    bisect = Bisect(lower=args.numbers[0], upper=args.numbers[1])
else:
    parser.print_help()
    exit(1)


def big_or_small(number: float):
    while "the answer is invalid":
        reply = input(
            f"Is {number} too big or too small? (b/s): ").lower().strip()
        if reply[:1] == 'b':
            return True
        if reply[:1] == 's':
            return False


while True:

    if big_or_small(bisect.Suggestion()):
        bisect.TooBig()
    else:
        bisect.TooSmall()
