#!/usr/bin/env python3


def selection_sort(arr):
    if len(arr) == 0:
        raise ValueError("The list is empty")

    for i in range(len(arr)):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[minIndex] > arr[j]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr


if __name__=='__main__':
    arr = [92, 19, 24, 11, 32, 101, 87]
    print(selection_sort(arr=arr))