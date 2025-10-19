def solution(n, arr1, arr2):
    result_arr1 = []
    result_arr2 = []
    for a in arr1:
        tmp = n
        tmplst = []
        while tmp > 0:
            if a >= 2 ** (tmp - 1):
                a -= (2 ** (tmp - 1))
                tmplst.append(True)
                tmp -= 1
            else:
                tmplst.append(False)
                tmp -= 1
        result_arr1.append(tmplst)

    for a in arr2:
        tmp = n
        tmplst = []
        while tmp > 0:
            if a >= 2 ** (tmp - 1):
                a -= (2 ** (tmp - 1))
                tmplst.append(True)
                tmp -= 1
            else:
                tmplst.append(False)
                tmp -= 1
        result_arr2.append(tmplst)

    # print(result_arr1)
    # print(result_arr2)

    arr = []

    for i in range(len(result_arr1)):
        tmp = []
        for j in range(len(result_arr1[0])):
            if result_arr1[i][j] or result_arr2[i][j]:
                tmp.append(True)
            else:
                tmp.append(False)
        arr.append(tmp)

    result = []
    for i in range(len(arr)):
        tmp = ""
        for j in range(len(arr[0])):
            if arr[i][j]:
                tmp += "#"
            else:
                tmp += " "
        result.append(tmp)

    print(result)

    return result