# Uses python3
import sys
import copy
import random


def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    return number_of_inversions

def merge_sort(data, start_idx, end_idx):
    num_inversions = 0
    if start_idx<end_idx:
        mid = start_idx + ((end_idx-start_idx) // 2)

        num_inversions = merge_sort(data, start_idx, mid)
        num_inversions += merge_sort(data, mid+1, end_idx)

        # copy is needed as we can do it in place.
        left_copy = copy.deepcopy(data[start_idx:mid+1])
        left_len = len(left_copy)
        right_copy = copy.deepcopy(data[mid+1:end_idx+1])
        right_len = len(right_copy)

        curr_idx = start_idx
        i = j = 0

        # inversion: how many times do you switch pairs to get the sorted sequence.

        while i < left_len and j< right_len:
            # smallest element on the left
            if left_copy[i] <= right_copy[j]:
                data[curr_idx] = left_copy[i]
                i += 1
            # smallest on the right
            else:
                data[curr_idx] = right_copy[j]
                j += 1
                # if you take something from the right, everything remaining on the left side needs to be inverted.
                '''
                    Example:
                      left         right 
                    2,9,10          3
                    
                      start: 2,9,10,3
                             2,3,10,9
                             2.3,9,10
                            
                      
                '''
                num_inversions += (left_len - i)

            curr_idx +=1


        # now, which array has ended
        while i<left_len:
            data[curr_idx] = left_copy[i]
            i+=1
            curr_idx += 1


        while j<right_len:
            data[curr_idx] = right_copy[j]
            j+=1
            curr_idx += 1


    return num_inversions


if __name__ == '__main__':
    testing = False
    if testing:
        # num_ints = 1000
        # data = [random.randint(0,10000) for x in range(0, num_ints)]
        #
        data = [2,3,9,2,9]
        result = merge_sort(data, 0, len(data)-1)
        assert result == 2

        data = [9, 8, 7, 3, 2, 1]
        result = merge_sort(data, 0, len(data)-1)
        assert result == 15
    else:
        input = sys.stdin.read()
        n, *data = list(map(int, input.split()))

    print (merge_sort(data, 0, len(data)-1))