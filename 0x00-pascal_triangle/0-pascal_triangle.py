#!/usr/bin/python3
'''
    interview quiz
    complexity -> o(n2)
'''


def pascal_triangle(n: int) -> list[list[int]]:
    res = [[1]]

    for i in range(n-1):
        prevtemp = [0] + res[-1] + [0]
        newrow = []
        for j in range(len(res[-1]) + 1):
            newrow.append(prevtemp[j] + prevtemp[j + 1])
        res.append(newrow)
    return res