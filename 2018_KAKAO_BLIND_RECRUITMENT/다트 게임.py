def solution(dartResult):
    lst = [0, 'S']
    result = []
    resultList1 = ['S', 'D', 'T']
    resultList2 = ['*', '#']
    dartResult = list(dartResult)
    tmp = 0
    for idx, dart in enumerate(dartResult):
        if dart in resultList1 or dart in resultList2:
            lst.append(dart)
        else:
            lst.append(int(dart))

    dartResult = lst

    for i, l in enumerate(lst):
        if l == 1:
            if lst[i + 1] == 0:
                lst.pop(i + 1)
                lst[i] = 10

    print(dartResult)
    for idx, dart in enumerate(dartResult):

        # SDT 처리
        if dart in resultList1:
            if dart == 'S':
                result.append(dartResult[idx - 1])
            elif dart == 'D':
                result.append(dartResult[idx - 1] * dartResult[idx - 1])
            elif dart == 'T':
                result.append(dartResult[idx - 1] * dartResult[idx - 1] * dartResult[idx - 1])

        # * # 처리
        elif dart in resultList2:
            if dart == '*':
                result[-1] = result[-1] * 2
                result[-2] = result[-2] * 2
            elif dart == '#':
                result[-1] = result[-1] * (-1)


        else:
            continue

    return sum(result)
