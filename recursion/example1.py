#!/usr/bin/env python3

'''
def factorial(num):    # Factorial using Recursion
    if num <= 1:
        return 1
    else:
        print("Echo {}".format(num))
        print("{}".format(num-1))
        return num*factorial(num-1)


def fab(num):
    if num <= 1:
        return 1
    else:
        print()
        print("{} {} {}".format(num, num-1, num-2
                                ))
        return num + fab(num-1) + fab(num-2)


if __name__=='__main__':
    #print(factorial(14))
    print(fab(10))
'''


def main(l, r):
    for n in range(l, r):
        if n%2 != 0:
            print(n)

if __name__=="__main__":
    main(2,5)