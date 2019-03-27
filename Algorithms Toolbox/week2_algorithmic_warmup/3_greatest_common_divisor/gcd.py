# Uses python3


def gcd(a,b):
    (a,b) = (b, a) if b > a else (a, b)
    if b == 1:
        return 1
    remainder = a % b

    if remainder == 0:
        return b
    return gcd(b, remainder)

# assert gcd(10,4) == 2
# assert gcd(10,3) == 1
# assert gcd(1,1) == 1
# assert gcd(20,10) == 10
# assert gcd(10,20) == 10

if __name__ == "__main__":
    input = input()
    a, b = map(int, input.split())
    print(gcd(a, b))
