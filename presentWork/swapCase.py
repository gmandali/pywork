# https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
def swap_case(var):
    i = var.swapcase()
    return i


s = input()
result = swap_case(s)
print(result)
