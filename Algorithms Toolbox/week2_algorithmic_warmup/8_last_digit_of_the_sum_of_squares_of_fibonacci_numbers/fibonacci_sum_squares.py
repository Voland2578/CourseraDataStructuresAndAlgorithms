# Uses python3
from sys import stdin

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





def fibonacci_sum_squares(n):
    if n <= 1:
        return n

    # first fib is fib(n)
    # second fib is fib(n+1)
    pisano = pisano_length(10)
    f1 = fib(n % pisano)
    f2 = fib((n+1) % pisano)
    return (f1*f2) % 10

#assert fibonacci_sum_squares(7) == 3
#assert fibonacci_sum_squares(73) == 1

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares(n))
