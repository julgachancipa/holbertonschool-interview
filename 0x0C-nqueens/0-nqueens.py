#!/usr/bin/python3
"""
N queens
"""
import sys


if len(sys.argv) > 2:
    print('Usage: nqueens N')
    exit(1)
N = sys.argv[-1]
if not str.isdigit(N):
    print('N must be a number')
    exit(1)
N = int(N)
if N < 4:
    print('N must be at least 4')
    exit(1)

ld = [0] * N * 10
rd = [0] * N * 10
cl = [0] * N * 10


def getSolution(board):
    """
    Print the indexes in the board
    :param board: board
    :return: nothing
    """
    solution = []
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                solution.append([i, j])
    print(solution)


def solveNQUtil(board, col):
    """
    Solves the N queens problem
    :param board:
    :param col:
    :return:
    """
    if col >= N:
        getSolution(board)
        return False

    for i in range(N):
        if ((ld[i - col + N - 1] != 1 and
             rd[i + col] != 1) and cl[i] != 1):

            board[i][col] = 1
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 1

            if solveNQUtil(board, col + 1):
                return True

            board[i][col] = 0  # BACKTRACK
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 0

    return False


board = [[0 for j in range(N)] for i in range(N)]
solveNQUtil(board, 0)
