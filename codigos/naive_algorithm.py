def naive_algorithm (P,T):
    sizep = len(P)
    sizet = len(T)
    cantcm = 0
    index = []

    for x in range (sizet - sizep + 1):
        for y in range (sizep):
            if P[y] == T[x+y]:
                cantcm = cantcm + 1
            else:
                continue

        if cantcm == sizep:
            index.append(x)
        cantcm = 0

    return index
