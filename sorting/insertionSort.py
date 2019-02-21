#!/usr/bin/env python3


def insertion_sort(arr):
    if len(arr) == 0:
        raise ValueError("The list is empty")

    for i in range(1, len(arr)):
        currentValue  = arr[i]
        position = i

        while position > 0 and arr[position-1] > currentValue:
            arr[position] = arr[position-1]
            position = position-1
        arr[position] = currentValue
    return arr


if __name__=='__main__':
    arr = [92, 19, 24, 11, 32, 101, 87]
    print(insertion_sort(arr=arr))