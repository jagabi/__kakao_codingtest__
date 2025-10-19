def solution(record):
    dic = {}
    records = []
    for rec in record:
        records.append(list(map(str, rec.split())))

    for rec in records:
        if rec[0] != 'Leave':
            dic[rec[1]] = rec[2]

    result = []
    for rec in records:
        if rec[0] == 'Enter':
            result.append(f'{dic[rec[1]]}님이 들어왔습니다.')
        elif rec[0] == 'Leave':
            result.append(f'{dic[rec[1]]}님이 나갔습니다.')
        else:
            continue

    return result