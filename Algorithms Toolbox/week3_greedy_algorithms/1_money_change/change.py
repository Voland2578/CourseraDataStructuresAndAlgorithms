# Uses python3
import sys

coins = [10, 5, 1]
def calc(m, chosen_coins):
    for c in coins:
        if m>=c:
            chosen_coins.append(c)
            return calc(m-c, chosen_coins)
    # here we have reached 0 so nothing to do

def get_change(m):
    chosen = []
    calc(m, chosen)
    return len(chosen)

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
