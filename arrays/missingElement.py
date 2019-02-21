#!/usr/bin/env python3
from collections import defaultdict


def missing_element_method1(list1, list2):

    list1.sort()
    list2.sort()

    for n1, n2 in zip(list1, list2):
        if n1 != n2:
            return n1
    return list1[-1]


def missing_element_method2(list1, list2):

    key_dict = defaultdict(int)

    for num in list2:
        key_dict[num] += 1

    for num in list1:
        if key_dict[num] == 0:
            return num
        else:
            key_dict[num] -= 1


if __name__=='__main__':
    l1 = [5,7,3,9,2]
    l2 = [5,3,9,2]
    print(missing_element_method1(l1, l2))

    l3 = [1,3,2,1,5,8,5,9]
    l4 = [1,3,2,5,5,1,9]
    print(missing_element_method2(l3, l4))
