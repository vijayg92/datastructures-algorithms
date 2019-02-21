#!/usr/bin/env python3


def pair_sum(array, num):

    if len(array) < 2:
        return

    seen = set()
    output = set()

    for n in array:
        target = num-n
        if target not in seen:
            seen.add(n)
        else:
            output.add((min(n, target), max(n, target)))
    return output


if __name__=='__main__':
    array = [1,3,2,2]
    print(pair_sum(array, 4))

    array1 = [1, 3, 4, 2]
    print(pair_sum(array1, 4))