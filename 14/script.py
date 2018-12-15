n = 1000000

seqList = [1]
seqSet = set(seqList)

i = 2
while i < n:
    temp = [i]
    while temp[-1] not in seqSet:
        if temp[-1] % 2 == 0:
            temp += [int(temp[-1] / 2)]
        else:
            temp += [int(3 * temp[-1] + 1)]

    l = seqList.index(temp[-1]) + 1
    if (len(temp) > l):
        seqList = temp + seqList[l:]
        seqSet = set(seqList)

    i += 1
