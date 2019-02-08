# Implementation of Binary Search


def binary_search(inputList, searchElem):

    firstIndex = 0
    lastIndex = len(inputList) - 1

    while firstIndex <= lastIndex:

        midIndex = int((firstIndex + lastIndex) / 2)

        if inputList[midIndex] == searchElem:
            return "Found Element at {} position".format(midIndex)
        elif inputList[midIndex] < searchElem:
            firstIndex = midIndex + 1
        else:
            lastIndex = midIndex - 1
    return "Element doesn't exist!!"


if __name__ == '__main__':
    mylist = [1, 3, 9, 11, 15, 19, 29]
    # 1st Test
    value1 = 15
    print(binary_search(inputList=mylist, searchElem=value1))
    ## 2nd Test
    value2 = 35
    print(binary_search(inputList=mylist, searchElem=value2))