# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
from collections import deque

class TreeHeight:
        def _read(self, nodes):
                self.table = [ deque() for _ in range(0, len(nodes))]


                children_idx = range(0, len(nodes))
                self.root = None
                # indices are parents, nodes are children
                for (child_idx, parent_idx) in zip(children_idx, nodes):
                    if parent_idx == -1:
                        self.root = child_idx
                    else:
                        self.table[parent_idx].append(child_idx)

                    if parent_idx == -1:
                        self.root = child_idx


        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
                self._read(self.parent)

        def __compute(self, node_id):
                children = self.table[node_id]
                # leaf node, height one
                if len(children) == 0:
                    return 1

                max_height = 0
                for c in children:
                    max_height = max(max_height, self.__compute(c))

                return 1+max_height

        def compute_height(self):
                 return self.__compute(self.root)


        # breadth first non-recursive
        def computeNonRecursively(self, root):
                level = 1

                # roots children
                process_queue = deque()
                process_queue.extend(self.table[root])
                num_children_at_level = len(self.table[root])

                while num_children_at_level > 0 :
                        # pop this level, push next level.
                        children = deque()
                        for _ in range(0, num_children_at_level):
                                next_child = process_queue.pop()
                                children.extend(self.table[next_child])
                        process_queue.extend(children)
                        num_children_at_level = len(children)
                        level += 1

                return level



def testCase(num_elements):
    import  random
    data = []

    for _ in range(0, num_elements):
        data.append(random.randint(0,num_elements))
    data.append(-1)
    return data

def main():
  tree = TreeHeight()
  #l = [ -1,0,4,0,3]
  l = [4,-1,4,1,1]
  #l = [-1]
  #tree._read(l)
  #tree.read()
  #l = testCase(100000)
  tree._read(l)
  #print(sorted(tree.depth, reverse=True)[0])
  print(tree.compute_height())
  print (tree.computeNonRecursively(tree.root))

threading.Thread(target=main).start()
