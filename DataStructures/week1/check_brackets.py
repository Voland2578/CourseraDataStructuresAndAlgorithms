# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    stack = []

    for i, next in enumerate(text):
        if next in "([{":
            stack.append((i,next))
        if next in ")]}":
            if len(stack) == 0:
                return 1+ i
            idx, matching_bracket = stack.pop()
            if not are_matching(matching_bracket,next):
                return 1+ i
    # if there are elements on the stack, this is a failure
    if len(stack) > 0:
        idx, v = stack.pop()
        return 1 + idx

    return "Success"

def main():
    text = input()
    #text = "foo(bar);"
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print (mismatch)

if __name__ == "__main__":
    main()
