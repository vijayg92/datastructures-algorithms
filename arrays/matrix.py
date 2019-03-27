#!/usr/bin/env python3


def transpose(matrix):
    if len(matrix) == 0:
        return ValueError("Matrix cannot be null or empty")
    result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return result


def addition(matrix1, matrix2):
    if len(matrix1) == 0 or len(matrix2) == 0:
        return ValueError("Matrix cannot be null or empty")
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix2)) ] for i in range(len(matrix1))]
    return result


def multiplication(matrix1, matrix2):
    return


if __name__ == '__main__':
    m1 = [[12,7,3],[4 ,5,6],[7 ,8,9]]
    m2 = [[5,8,1],[6,7,3],[4,5,9]]
    matrix_add = addition(matrix1=m1, matrix2=m2)
    print(matrix_add)

    m3 = [[1,2,3], [4,5,6]]
    print(transpose(m3))

