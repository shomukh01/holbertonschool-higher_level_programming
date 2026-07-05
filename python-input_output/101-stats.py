#!/usr/bin/python3
"""Script that reads stdin and computes metrics."""

import sys

total_size = 0
count = 0
codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}


def print_stats():
    """Print accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(codes.keys()):
        if codes[code]:
            print("{}: {}".format(code, codes[code]))


try:
    for line in sys.stdin:
        count += 1
        parts = line.split()

        try:
            total_size += int(parts[-1])
            status = parts[-2]
            if status in codes:
                codes[status] += 1
        except (IndexError, ValueError):
            pass

        if count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

print_stats()
