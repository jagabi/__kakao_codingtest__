import copy


def setting(arr):
    for i in sorted(list(range(len(arr))), reverse=True):
        for j in sorted(list(range(len(arr[0]))), reverse=True):
            if arr[i][j] == 0:
                for k in sorted(list(range(i)), reverse=True):
                    if arr[k][j] != 0:
                        arr[i][j] = arr[k][j]
                        arr[k][j] = 0
                        break
    return arr


def check(arr, i, j):
    if arr[i][j] == arr[i + 1][j] and arr[i][j] == arr[i][j + 1] and arr[i][j] == arr[i + 1][j + 1]:
        return True

    return False


def turn(arr):
    tmp = copy.deepcopy(arr)
    for i in range(len(arr) - 1):
        for j in range(len(arr[0]) - 1):
            if check(arr, i, j):
                tmp[i][j] = 0
                tmp[i + 1][j] = 0
                tmp[i][j + 1] = 0
                tmp[i + 1][j + 1] = 0
    arr = tmp

    return arr


def solution(m, n, board):
    result = 0
    arr = []
    for b in board:
        arr.append(list(b))

    while True:
        if arr == turn(arr):
            break
        arr = turn(arr)
        arr = setting(arr)

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                result += 1

    return result