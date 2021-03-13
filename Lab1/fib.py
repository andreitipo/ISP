#!/usr/bin/env python3
import logging


logging.basicConfig(level=logging.INFO)
 
 
def fibonaccy(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonaccy(n-1) + fibonaccy(n-2)


def main():
    logging.info(fibonaccy(11))


if __name__ == "__main__":
    main()
