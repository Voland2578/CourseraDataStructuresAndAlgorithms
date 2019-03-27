import re
import copy
from collections import namedtuple
# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

Result = namedtuple('Result',['max', 'max_ops', 'min', 'min_ops', 'left_idx_pair', 'right_idx_pair'])

cache = []

def printChecking(nums, operators,num_start_idx, num_end_idx):
    data = []
    data.append(nums[num_start_idx])
    if num_end_idx > num_start_idx:
        for i in range(num_start_idx+1, num_end_idx+1):
            data.append(operators[i-1])
            data.append(nums[i])
    print ("Start idx: {}, end_idx: {}. Result: {}".format(num_start_idx, num_end_idx,"".join([str(x) for x in data])))

def unwrap(ds, ns, operators, solution):
    nums = copy.deepcopy(ns)
    dataset = copy.deepcopy(ds)
    sol = solution.max_ops
    for idx in range(len(operators)-1, -1,-1):
        right = "({})".format(dataset[idx+1])
        left = "({})".format(dataset[idx])
        del dataset[idx]
        dataset[idx] = "({}){}({})".format(left, sol[idx],right)


def __getMaxAndMin(nums, operators,num_start_idx, num_end_idx):
    global cache
    printChecking(nums,operators,num_start_idx, num_end_idx)

    if num_start_idx == num_end_idx:
        return Result (nums[num_start_idx],[], nums[num_start_idx], [],(),())

    if num_start_idx == num_end_idx - 1:
        val = evalt(nums[num_start_idx], nums[num_end_idx], operators[num_start_idx])
        result =  Result(val, [num_start_idx], val, [num_start_idx], (num_start_idx, num_end_idx),(num_start_idx, num_end_idx))
        cache[num_start_idx][num_end_idx] = result
        return result



    # 1+5 expression, eval only 1 operator
    for op_idx in range(num_start_idx, num_end_idx):
        operator = operators[op_idx]

        mm1 = __getMaxAndMin(nums, operators, num_start_idx, op_idx)
        mm2 = __getMaxAndMin(nums, operators, op_idx+1, num_end_idx)

        # process the output
        if operator == "+":
            result = Result(evalt(mm1.max, mm2.max, "+"), mm1.max_ops + mm2.max_ops + [op_idx],
                                                          evalt(mm1.min, mm2.min, "+"),
                                                          mm1.min_ops +  mm2.min_ops + [op_idx],
                                                          (num_start_idx, op_idx),
                                                          (op_idx+1, num_end_idx)
                            )
        elif operator == "-":
            result = Result(evalt(mm1.max, mm2.min, "-"), mm1.max_ops + mm2.min_ops  + [op_idx],
                                                       evalt(mm1.min, mm2.max, "-"),
                            mm1.min_ops + mm2.max_ops  + [op_idx],
                            (num_start_idx, op_idx),
                            (op_idx + 1, num_end_idx)
                            )
        else:
            cross_mult = []
            cross_mult.append([evalt(mm1.max, mm2.min,"*"),mm1.max_ops, mm2.min_ops])
            cross_mult.append([evalt(mm1.max, mm2.max,"*"),mm1.max_ops, mm2.max_ops])
            cross_mult.append([evalt(mm1.min, mm2.min,"*"),mm1.min_ops, mm2.min_ops])
            cross_mult.append([evalt(mm1.min, mm2.max,"*"),mm1.min_ops, mm2.max_ops])
            cross_mult.sort(key=lambda x: x[0])
            result = Result( cross_mult[3][0],
                                                        cross_mult[3][1] + cross_mult[3][2] + [op_idx] ,
                                                        cross_mult[0][0],
                                                        cross_mult[0][1] +  cross_mult[0][2]  + [op_idx],
                                                        (num_start_idx, op_idx),
                                                        (op_idx + 1, num_end_idx)
                                    )


        current_result = cache[num_start_idx][num_end_idx]
        if current_result is None:
            cache[num_start_idx][num_end_idx] = result
        else:
            cache[num_start_idx][num_end_idx] = Result(
                result.max if result.max > current_result.max else current_result.max,
                result.max_ops if result.max > current_result.max else current_result.max_ops,
                result.min if result.min < current_result.min else current_result.min,
                result.min_ops if result.min < current_result.min else current_result.min_ops,
               (num_start_idx, op_idx),
               (op_idx + 1, num_end_idx)
            )
    return cache[num_start_idx][num_end_idx]

def get_maximum_value(dataset):
    split_expression = re.split('(\*|\+|\-)',expression)
    nums = []
    ops = []

    for i in range(0, len(split_expression)):
        if i % 2 == 0:
            nums.append(int(split_expression[i]))
        else:
            ops.append(split_expression[i])

    global cache
    cache = [ [None] * len(nums) for i in range(0, len(nums))]
    m = __getMaxAndMin(nums, ops, 0, len(nums)-1 )

    #print(cache)
    #write your code here
    #return m.max
    unwrap(split_expression, nums, ops,m)


    return 0

if __name__ == "__main__":
    #expression = "4+1*7-5*2"
    #expression = "5-8+7*4-8+9"
    #print(get_maximum_value(input()))
    expression = "11*1+2*10"
    print(get_maximum_value(expression))

