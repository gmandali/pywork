# https://www.hackerrank.com/challenges/text-wrap/problem
import textwrap


def wrap(strings, max_widths):
    return textwrap.fill(strings, max_widths)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)