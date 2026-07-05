#!/usr/bin/python3
"""Script that reads stdin and computes metrics."""

import sys


def print_stats(total_size, codes):
    """Print accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(codes):
        if codes[code]:
            print("{}: {}".format(code, codes[code]))


if __name__ == "__main__":
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

    try:
        for line in sys.stdin:
            count += 1
            parts = line.split()

            try:
                total_size += int(parts[-1])
                if parts[-2] in codes:
                    codes[parts[-2]] += 1
            except (IndexError, ValueError):
                pass

            if count % 10 == 0:
                print_stats(total_size, codes)

    except KeyboardInterrupt:
        print_stats(total_size, codes)
        raise

    print_stats(total_size, codes)
