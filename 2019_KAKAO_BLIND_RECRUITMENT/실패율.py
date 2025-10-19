def solution(N, stages):
    nums = [i for i in range(1, N + 1)]
    result = []
    for num in nums:
        cnt1 = 0
        cnt2 = 0
        if num not in stages:
            result.append([num, 0])
            continue
        for stage in stages:
            if stage >= num:
                cnt1 += 1
            if num == stage:
                cnt2 += 1
        result.append([num, cnt2 / cnt1])

    result.sort(key=lambda x: x[1], reverse=True)

    answer = [r[0] for r in result]
    print(answer)

    return answer