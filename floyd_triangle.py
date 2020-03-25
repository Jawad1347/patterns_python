#!/usr/bin/python
""" floyd triangles """
N = int(input("NUMBER of yoour choice "))


def simple():
    """ prints right triangle of numbers """
    num = 1
    for row in range(1, N + 1):
        for col in range(1, row + 1):
            print(num, end=" ")
            num += 1
        print()


simple()
