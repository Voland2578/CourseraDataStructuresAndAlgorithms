# Uses python3
import sys
import time

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print ('%r  %2.2f ms' % \
                  (method.__name__, (te - ts) * 1000))
        return result
    return timed

def fib(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current)

    return current
def fibonacci_nth_sum_last_digit(n):
    if n <= 1:
        return n
    # really cool optimization is pasano
    pisano = pisano_length(10)
    required_fib = fib( ( n+2) % pisano)
    sum = required_fib - 1
    return sum % 10

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

def fibonacci_partial_sum(f, t):
    partial_full = fibonacci_nth_sum_last_digit(t)
    partial_prefix = fibonacci_nth_sum_last_digit(max(0,f - 1))
    return ((partial_full + 10) - partial_prefix) % 10

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))
