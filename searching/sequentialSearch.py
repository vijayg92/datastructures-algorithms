# Implementation of Sequential Search


def unsorted_array(arr, elem):
    """
    For Unordered List Sorting!
    """

    pos = 0
    found = False

    while pos < len(arr) and not found:

        if arr[pos] == elem:
            found = True
        else:
            pos += 1
    return found


def sorted_array(arr, elem):
    """
    Input Array must be ordered/sorted!
    """

    pos = 0
    found = False
    stopped = False

    while pos < len(arr) and not found and not stopped:

        if arr[pos] == elem:
            found = True
        else:
            if arr[pos] > elem:
                stopped = True
            else:
                pos += 1
    return found


if __name__ == '__main__':
    unSortArr = [6, 9, 3, 14, 2, 11, 5]
    sortArr = [1, 5, 8, 11, 15, 17]

    print(sorted_array(arr=sortArr, elem=11))
    print(unsorted_array(arr=unSortArr, elem=2))