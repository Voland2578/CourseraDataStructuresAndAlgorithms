# Uses python3
import sys

result_map = {}
def optimal_summands(n):

    data = [ [0] for _ in range(0,n+1)]
    data[0] = [ 0 for _ in  range(0,n+1)]

    for next_sum in range(1, n + 1):
        for next_maximum in range(1, n + 1):

            print ("next sum:{} current_max:{}". format(next_sum, next_maximum))
            # ----------------- Not Take section ------------------
            #not_take = None
            #take_it = None
            prev_maximum_value = next_maximum - 1

            # When we process 1,
            if prev_maximum_value == 0:
                not_take = 0
            # If the value we are checking is larger than the sum, we obviously cannot take it.
            elif (next_maximum>next_sum):
                not_take = data[next_sum][prev_maximum_value]
            else:
                # If we did not take "this" element, the result is the value of the same sum with the previous maximum
                not_take = data[next_sum][prev_maximum_value]

            # Cannot attempt to "take" the element if:
            #   * If the number we checking is greater than current sum
            #   * Or, if we took the element, the remaining sum cannot be constructed
            if (next_maximum>next_sum) or  ((next_maximum != next_sum) and data[next_sum - next_maximum][next_maximum-1] == 0):
                take_it = 0
            else:
                take_it = 1 + data[next_sum - next_maximum][next_maximum-1]

            # dummy number
            result = max(take_it, not_take)
            data[next_sum].append(result)

            if result>0:
                result_map[next_sum] = result
                data[next_sum].extend([result for _ in range(n-len(data[next_sum])+1)])
                break;

    return data
def get_results(data, n):
    final_result = []
    current_sum = n
    while ( current_sum > 0):
        v = result_map.get(current_sum, 0)
        final_result.append(v)
        current_sum  = current_sum - v

    return final_result;











    summands = []
    #write your code here
    return summands

num = 9
data = optimal_summands(num)
print (get_results( data, num))
# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n = int(input)
#     summands = optimal_summands(n)
#     print(len(summands))
#     for x in summands:
#         print(x, end=' ')
