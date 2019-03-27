# Uses python3
def gcd(a,b):
    (a,b) = (b, a) if b > a else (a, b)
    if b == 1:
        return 1
    remainder = a % b

    if remainder == 0:
        return b
    return gcd(b, remainder)


def lcm(a, b):
    g = gcd(a,b)
    #return int(g * a / g * b / g)
    return g * int(a/g) * int(b/g)

lcm(226553150,1023473145)
assert lcm(6,8) == 24
assert lcm(1,2) == 2
assert lcm(20,30) == 60
assert lcm(7,5) == 35

if __name__ == '__main__':
    input = input()
    a, b = map(int, input.split())
    print(lcm(a, b))

