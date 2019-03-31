#python3
import sys
from collections import  deque

class StackWithMax():
    def __init__(self):
        self.__stack = deque()
        self.max_at_index = deque()

    def Push(self, a):
        if len(self.__stack) == 0:
           self.max_at_index.append(a)
        else:
           self.max_at_index.append( max(self.max_at_index[-1], a))

        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack) > 0)
        self.max_at_index.pop()
        self.__stack.pop()

    def Max(self):
        assert (len(self.__stack) > 0)
        return self.max_at_index[-1]


def getTestCase(data_str):
    data = []
    data_str = data_str.rstrip().rstrip()
    for x in data_str.split('\n'):
        data.append(x.lstrip().rstrip().split(" "))
    return data




if __name__ == '__main__':
    stack = StackWithMax()

    data_str = '''push 2
push 3
push 9
push 7
push 2
max
max
max
pop
max'''

    data = getTestCase(data_str)
    io_num_queries = lambda:int(sys.stdin.readline())
    test_case_num_queries = lambda: len(data)

    read_io = True
    if read_io:
        num_queries_function = lambda:int(sys.stdin.readline())
        read_line_function =  lambda x: sys.stdin.readline().split()
    else:
        num_queries_function = lambda: len(data)
        read_line_function = lambda x: data[x]

    num_queries = num_queries_function()
    for i in range(num_queries):
        query = read_line_function(i)

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
