#!/usr/bin/env python3

def anagram(str1, str2):
    s1 = str1.replace(' ', '').lower()
    s2 = str2.replace(' ', '').lower()
    count = {}
    
    if len(s1) != len(s2):
        return False

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for letter in count:
        if count[letter] != 0:
            return False
    
    return True


if __name__ == '__main__':
    problem1 = anagram('dog','god')
    print(problem1)
    problem2 = anagram('clint eastwood','olsd west action')
    print(problem2)
    problem3 = anagram('clint eastwood','old west action')
    print(problem3)
