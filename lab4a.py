#!/usr/bin/env python3


def join_sets(s1, s2):
    sec1 = s1 | s2
    return sec1

def match_sets(s1, s2):
    sec2 = s1 & s2
    return sec2

def diff_sets(s1, s2):
    sec3 = s1 ^ s2
    return sec3



if __name__ == '__main__':
    set1 = set(range(1,10))
    set2 = set(range(5, 15))
    print('set1: ', set1)
    print('set2: ', set2)
    print('join: ', join_sets(set1, set2))
    print('match: ', match_sets(set1, set2))
    print('diff: ', diff_sets(set1, set2))



