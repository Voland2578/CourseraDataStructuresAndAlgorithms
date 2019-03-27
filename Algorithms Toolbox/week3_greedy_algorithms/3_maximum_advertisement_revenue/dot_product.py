#Uses python3

import sys

def max_dot_product(a, b):
    a_s = sorted(a, reverse=True)
    b_s = sorted(b, reverse=True)
    max_p = 0
    for i in range(len(a_s)):
        max_p += a_s[i] * b_s[i]
    return max_p
#assert( max_dot_product( [1,3,-5], [-2,4,1] ) == 23)
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
