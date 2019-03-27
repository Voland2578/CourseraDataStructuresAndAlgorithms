# Uses python3
import sys
import random

def partition3(a, l, r):
    equal_start_idx = equal_end_idx = l
    x = a[l] # we look for dups for this element

    for i in range(l + 1, r + 1):
        if a[i] < x:
            '''
                example:    1,2,9,9,9,34,5
                    step1:  1,2,34,9,9,9,5
                    step2:  1,2,5,9,9,9,34
                example: where first step is skipped
            '''
            # step 1: move the start element forward beyond the end of the duplicates (swap)
            if equal_end_idx + 1 < i:
                a[equal_end_idx+1], a[equal_start_idx] = a[equal_start_idx], a[equal_end_idx+1]

            #step 2, replace.
            a[equal_start_idx],a[i] = a[i], a[equal_start_idx]

            # advance start and end index of the duplicates
            equal_start_idx += 1
            equal_end_idx += 1

        elif a[i] == x:
            equal_end_idx += 1
            a[i], a[equal_end_idx] = a[equal_end_idx], a[i]
        else:
            pass

    result =  ( (l,equal_start_idx-1 if equal_start_idx>l else None),
                (equal_start_idx, equal_end_idx),
                (equal_end_idx+1 if equal_end_idx<=r else None, r))
    return result



def randomized_quick_sort(a, start_idx, end_idx):
    if start_idx >= end_idx:
        return
    # choose random number and put in the first position
    k = random.randint(start_idx, end_idx)
    a[start_idx], a[k] = a[k], a[start_idx]

    m = partition3(a, start_idx, end_idx)
    # mid partition does not need to be sorted.
    if m[0][1] is not None:
        randomized_quick_sort(a, m[0][0], m[0][1])

    if m[2][0] is not None:
        randomized_quick_sort(a, m[2][0], m[2][1])


def test_case(dup_number, num_duplicates, num_non_dups, max_number):
    dups = [dup_number] * num_duplicates

    non_dups = list(map(lambda x: random.randint(1, max_number), range(0, num_non_dups)))
    a = dups + non_dups
    random.shuffle(a)
    return a
if __name__ == '__main__':
    #input = sys.stdin.read()
    #n, *a = list(map(int, input.split()))
    a= test_case(2666, 2000,900,10000)
    testing = False
    if testing:
        import time
        start = time.time()

    randomized_quick_sort(a, 0, len(a) - 1)
    if testing:
        end = time.time()
        print ("Time taken: {} ", (end-start))

    #assert sorted(a) == a
    for x in a:
        print(x, end=' ')
