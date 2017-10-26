#Tabla de Bad Character. Alfabeto [a-z,A-Z]
def BCTable(P):
    size = len(P)
    table = {}
    for x in range(97,123):
        table[chr(x)] = size
    for x in range(65,91):
        table[chr(x)] = size
    for x in range(size-1):
        table[P[x]] = (size-x-1)
    return table

#Preprocessing GSTable with zbox
def suffix(P):
    string = ''.join(reversed(P))

    size = len(string)

    l = 0
    r = 0
    z = []
    z.append(size)
    index = []
    for k in range (1,size):
        x = 0
        if k > r:
            if string[x] == string[x+k]:
                l = k
                x += 1
            while x+k < size and string[x] == string[x+k]:
                x += 1
            r = k + x - 1
            z.append(x)
        else:
            i = k - l
            if z[i] < r - k + 1:
                z.append(z[i])
            else:
                l = k
                i = k + 1
                while i < size and string[i] == string[i-k]:
                    i += 1
                r = i - 1
                z.append(i-k)
    z.reverse()
    return z

def GSTable(P,suff):
    # suff = suffix(P)
    size = len(P)
    GS = [size for _ in range(size)]

    j = 0
    for x in range(size-1,-1,-1):
        if suff[x] == x + 1:
            for y in range(j,size - 1 - x):
                if GS[y] == size:
                    GS[y] = size - 1 -x

    for x in range(size-1):
        GS[size - 1 - suff[x]] = size - 1 - x

    return GS

def Boyer_Moore(T,*Ps):
    sizet = len(T)
    BM = []

    for P in Ps:
        sizep = len(P)

        bm = []

        #Preprocessing
        BC = BCTable(P)
        suff = suffix(P)
        GS = GSTable(P,suff)

        #Searching
        j = 0
        while j <= sizet - sizep:
            for i in range(sizep-1,-2,-1):
                if P[i] != T[i+j]:
                    break
            if i < 0:
                bm.append(j)
                j += GS[0]
            else:
                j += max(GS[i],BC[T[i+j]] - sizep + 1 + i)

        BM.append(bm)
    return BM
def Apostolico_Giancarlo(T,*Ps):

    AP = []
    sizet = len(T)

    for P in Ps:
        sizep = len(P)
        ap = []

        #Preprocessing
        BC = BCTable(P)
        suff = suffix(P)
        GS = GSTable(P,suff)

        skip = [0 for x in range(sizep)]

        #Searching
        j = 0
        while j <= sizet - sizep:
            i = sizep - 1
            while i >= 0:
                k = skip[i]
                s = suff[i]
                if k > 0:
                    if k > s:
                        if i + 1 == s:
                            i = -1
                        else:
                            i -= s
                        break
                    else:
                        i -= k
                        if k < s:
                            break
                else:
                    if P[i] == T[i+j]:
                        i -= 1
                    else:
                        break

            if i < 0:
                ap.append(j)
                skip[sizep - 1] = sizep
                shift = GS[0]
            else:
                skip[sizep - 1] = sizep - 1 - i
                shift = max(GS[i],BC[T[i+j]] - sizep + 1 + i)

            j += shift

            i = 0
            for x in range(sizep-shift):
                skip[i] = skip[x]
                i += 1
            for x in range(i,sizep):
                skip[i] = 0

        AP.append(ap)
    return AP
