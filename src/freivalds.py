# -*- coding: utf-8 -*-

import sys
from random import randint


def readint():
    return int(sys.stdin.readline())


def readarray(typ):
    return list(map(typ, sys.stdin.readline().split()))


def readmatrix(n, typ):
    M = []
    for _ in range(n):
        row = readarray(typ)
        assert len(row) == n
        M.append(row)
    return M


def mul(M, v):
    n = len(M)
    return [sum(M[i][j]*v[j] for j in range(n)) for i in range(n)]


def freivalds(A, B, C):
    n = len(A)
    x = [randint(0, 1000000) for _ in range(n)]
    return mul(A, mul(B, x)) == mul(C, x)


if __name__ == "__main__":
    print("请输入矩阵的维度n：")
    n = readint()
    print("请输入矩阵A：")
    A = readmatrix(n, int)
    print("请输入矩阵B：")
    B = readmatrix(n, int)
    print("请输入矩阵C：")
    C = readmatrix(n, int)
    print("AB=C" if freivalds(A, B, C) else "AB!=C")
