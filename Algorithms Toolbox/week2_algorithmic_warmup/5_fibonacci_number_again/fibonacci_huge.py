# Uses python3
import sys
# pisano cycle starts with 01 and goes on and on for a while
#
def pisano_length(m):
    # 011011
    next = fib(2)
    for x in range(2, m**2+1):
        next_fib = fib(x+1)
        (a,b) = ( next, next_fib )
        (m_a, m_b) = (a % m, b % m)
        if m_a == 0 and m_b == 1:
            return x
        next = next_fib

def fib(n):
    if n <= 1:
        return n
    previous = 0
    current = 1

    for _ in range(n-1):
        previous, current = current, previous + current
    return current

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    m_pisano = pisano_length(m)
    if n <= m_pisano:
        return fib(n) % m
    else:
        remainder = n % m_pisano
        return fib(remainder) % m
# assert (fib(0) == 0)
# assert (fib(2) == 1)
# assert (fib(10) == 55)
# assert pisano_length(2) == 3
# assert pisano_length(3)  ==8
if __name__ == '__main__':
    input = input()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
