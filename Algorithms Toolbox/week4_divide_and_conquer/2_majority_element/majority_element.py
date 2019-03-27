# Uses python3
import sys

def get_majority_element(a):
    a.sort()

    max_appearances = 0
    prev_element = None
    counter = 0
    for x in a:
        if x != prev_element:
            counter = 1
            prev_element = x
        else:
            counter += 1

        if counter > max_appearances:
            max_appearances = counter
    return 1 if max_appearances > len(a)/2 else -1

if __name__ == '__main__':
    #data = [2, 3 ,9, 2, 2]
    input = sys.stdin.read()
    n, *data = list(map(int, input.split()))
    if get_majority_element(data) != -1:
         print(1)
    else:
         print(0)
