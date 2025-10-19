def solution(str1, str2):
    string1 = []
    string2 = []

    for char in str1:
        if ord(char) >= 65 and ord(char) <= 90:
            string1.append(chr(ord(char) + 32))
        else:
            string1.append(char)
    for char in str2:
        if ord(char) >= 65 and ord(char) <= 90:
            string2.append(chr(ord(char) + 32))
        else:
            string2.append(char)

    set1 = []
    set2 = []
    for i in range(len(string1) - 1):
        set1.append(string1[i:i + 2])
    for i in range(len(string2) - 1):
        set2.append(string2[i:i + 2])

    # print(set1)
    # print(set2)

    possible = []
    for i in range(65, 91): possible.append(chr(i))
    for i in range(97, 123): possible.append(chr(i))

    # print(possible)

    set1_clean = []
    set2_clean = []

    for s in set1:
        if s[0] not in possible or s[1] not in possible:
            continue
        else:
            set1_clean.append(s)
    for s in set2:
        if s[0] not in possible or s[1] not in possible:
            continue
        else:
            set2_clean.append(s)

    set1_clean_str = []
    set2_clean_str = []

    for s1 in set1_clean: set1_clean_str.append(s1[0] + s1[1])
    for s2 in set2_clean: set2_clean_str.append(s2[0] + s2[1])

    set1 = set1_clean_str
    set2 = set2_clean_str

    tmp = set2[:]

    mix = []
    union = []

    for s1 in set1:
        for s2 in set2:
            if s1 == s2:
                mix.append(s2)
                set2.remove(s2)
                break

    for s1 in set1:
        union.append(s1)
    for s2 in tmp:
        union.append(s2)

    for m in mix:
        if m in union:
            union.remove(m)

    if len(mix) == 0 and len(union) == 0:
        return 65536

    result = 0

    result = len(mix) / len(union)
    print(int(result * 65536))
    return int(result * 65536)

# 65~90 대
# 97~122 소