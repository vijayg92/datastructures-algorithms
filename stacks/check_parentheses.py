#!/usr/bin/env python3


def main(parentheses):
    start = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    stack = []

    for p in parentheses:
        if p in start.keys():
            stack.append(p)
            continue
        else:
            try:
                marker = stack.pop()
            except IndexError:
                return False
            if p != start[marker]:
                return False
    return len(stack) == 0


if __name__=="__main__":
    p1 = "(((("
    print(main(p1))

    p2 = "][[[]]]"
    print(main(p2))

    p3 = "({[((()))]})"
    print(main(p3))

    p4 = "((({{{[[[}}}}})))"
    print(main(p4))

    p5 = "{{{{{{{{{"
    print(main(p5))
