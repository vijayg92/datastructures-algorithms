#!/usr/bin/env python3

def shell_sort(arr):

    gap = int(len(arr)/2)

    while gap > 0:
        for start in range(gap):
            gap_insertion_sort(arr, start,gap)
        gap = gap/2

def gap_insertion_sort(arr, start, gap):

    for i in range(start+gap, len(arr), gap):

        currentValue = arr[i]
        position = i

        while position >= gap and arr[position-gap] > currentValue:
            arr[position] = arr[position-gap]
            position = position-gap
        arr[position] = currentValue
    return arr


if __name__=='__main__':
    arr = [92, 19, 24, 11, 32, 101, 87]
    print(shell_sort(arr=arr))