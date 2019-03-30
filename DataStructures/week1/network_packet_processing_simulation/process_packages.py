# python3

from collections import namedtuple
import os
Request = namedtuple("Request", ["id", "arrived_at", "time_to_process"])
Response = namedtuple("Response", ["id", "was_dropped", "started_at"])
from collections import deque

class Buffer:
    def __init__(self, size):
        self.size = size
        self.buffer  = deque()
        #self.finish_time = []

    def process(self, request):
        if len(self.buffer) < self.size:
            self.buffer.appendleft(request)
    def canAdd(self):
        return len(self.buffer) < self.size

    def isEmpty(self):
        return len(self.buffer) == 0

    def pop(self):
        return self.buffer.pop()

    def peekTop(self):
        return self.buffer[-1]

# given the arrival time of the next request
# go through the buffer and "execute" everything that is possible
def flushQueue(current_time, up_to_time, buffer, responses):

    while not buffer.isEmpty():
        # if the time right now is before the first packet on the buffer,
        # move the current time to that
        if current_time < buffer.peekTop().arrived_at:
            current_time =  buffer.peekTop().arrived_at

        # this block is used for final flushing of the buffer
        if up_to_time is not None:
            if current_time + buffer.peekTop().time_to_process > up_to_time:
                return current_time

        top_request = buffer.pop()
        responses.append(Response(top_request.id, False, current_time))
        current_time += top_request.time_to_process

    return current_time

def process_requests(requests, buffer):
    # buffer is a queue
    current_time = 0
    responses = []
    for request in requests:
        # peek the buffers top request processing time
        current_time = flushQueue(current_time, request.arrived_at, buffer, responses)
        # try adding the request
        if buffer.canAdd():
            buffer.process(request)
        else:
            # reject the request
            responses.append(Response(request.id, True, -1))

    flushQueue(current_time, None, buffer, responses)
    responses = sorted(responses, key=lambda x: x.id)
    return responses


def loadData(meta_function, row_function ):
    buffer_size , n_requests = meta_function()
    requests = []
    for i in range(n_requests):
        arrived_at, time_to_process = map(int,row_function(i))
        requests.append(Request(i, arrived_at, time_to_process))

    return (buffer_size, requests)

def respToList(responses):
    result = []
    for response in responses:
        result.append ( (response.started_at if not response.was_dropped else -1))
    return result

def compareLists(l1, l2):
    if l1 is None or l2 is None:
        return False
    if len(l1) != len(l2):
        return False

    for i in range(0, len(l1)):
        if l1[i] != l2[i]:
            return False
    return True

def runTestCases():
    for t_num in range(1, 23):
        test = str(t_num).rjust(2, "0")
        path = os.path.join(os.getcwd(), "tests", test)
        print("Running test: {}".format(path))
        a_path = os.path.join(os.getcwd(), "tests", test + ".a")
        f = open(path, "r")

        meta_function = lambda: map(int, f.readline().split())
        row_level_function = lambda x: f.readline().split()
        (buffer_size, requests) = loadData(meta_function, row_level_function)

        buffer = Buffer(buffer_size)
        responses = process_requests(requests, buffer)
        respList = respToList(responses)

        a = open(a_path, "r")
        ans_list = []
        for i in range(len(requests)):
            ans_list.append(int(a.readline()))
        a.close()
        f.close()
        if not compareLists(respList, ans_list):
            print("Testcase {} failed. My answer: {}, Expected: {}".format(path, respList, ans_list))
def main():

    # read from the array
    sample_data = sample_data = [[0, 2], [1, 4], [5, 3]]
    meta_function = lambda: (1, len(sample_data))
    row_level_function = lambda x: sample_data[x]

    if False:
        runTestCases()
    else:
        # read from stdin
        io_meta_function = lambda: map(int, input().split())
        io_row_level_function = lambda x: input().split()
        (buffer_size, requests) = loadData(io_meta_function, io_row_level_function)
        buffer = Buffer(buffer_size)
        responses = process_requests(requests, buffer)
        respList = respToList(responses)
        for i in respList:
            print (i)



if __name__ == "__main__":
    main()



