# Uses python3
import sys
import math

# start_idx always corresponds to the first element of the array we are searching
# note, the grading was particular about using max memory so copying array does not really work
def binary_search_step(element, array, start_idx, end_idx):
    if start_idx>end_idx:
        return -1
    if start_idx == end_idx:
        return start_idx if element == array[start_idx] else -1
    else:
        mid = math.floor(start_idx + ((end_idx-start_idx) / 2))

        # midpoint is the element.
        if element == array[mid]:
            return mid
        # start idx remains the same because we are not advancing the first element of the search array
        elif element<array[mid]:
            return binary_search_step(element, array, start_idx, mid-1)
        else:
            return binary_search_step(element, array, mid+1, end_idx)

def binary_search(a, x):
    return binary_search_step(x,a, 0, len(a)-1)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    test_mode = False
    if not test_mode:
        input = sys.stdin.read()
        data = list(map(int, input.split()))
        n = data[0]
        m = data[n + 1]
        a = data[1 : n + 1]
        for x in data[n + 2:]:
            # replace with the call to binary_search when implemented
            print(binary_search(a, x), end = ' ')

    if test_mode:
        data = [1, 5, 8, 12, 13,23,11]
        search_key = [8,1,23,1,11,13]
        for x in search_key:
            # replace with the call to binary_search when implemented
            print(binary_search(data, x), end=' ')
