#!/usr/bin/env python3


def bubble_sort(arr):
    if len(arr) == 0:
        raise ValueError("The list is empty")

    for n in range(len(arr)-1,0,-1):
        for m in range(n):
            if arr[m] > arr[m+1]:
                temp = arr[m]
                arr[m] = arr[m+1]
                arr[m+1] = temp
    return arr


if __name__=='__main__':
    arr = [92, 19, 24, 11, 32, 101, 87]
    print(bubble_sort(arr=arr))