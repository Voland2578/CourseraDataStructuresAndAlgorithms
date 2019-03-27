# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    ratios = []
    for (idx,weight) in enumerate(weights):
        ratios.append((idx, values[idx] / weight))
    # sort
    ratios = sorted(ratios, key=lambda x: x[1], reverse=True)
    max_value = 0.0
    while capacity > 0:
         if len(ratios) == 0:
             break

         (idx, ratio) = ratios[0]
         (weight, value) = (weights[idx], values[idx])
         if capacity >= weight:
             max_value += value
             capacity -= weight
         else:
             max_value += (capacity / weight) * value
             capacity = 0
         ratios.pop(0)
         # we can either take the


    return max_value

if __name__ == "__main__":
   data = list(map(int, sys.stdin.read().split()))
   n, capacity = data[0:2]
   values = data[2:(2 * n + 2):2]
   weights = data[3:(2 * n + 2):2]
   opt_value = get_optimal_value(capacity, weights, values)
   print("{:.10f}".format(opt_value))
