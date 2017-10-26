def zbox(P,T):

    string = P+"$"+T

    size = len(string)
    sizepattern = len(P)

    l = 0
    r = 0
    z = []
    z.append(0)

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

    for k in range(len(z)):
        aux = z[k]
        if aux == sizepattern:
            index.append(aux-sizepattern+1)
    return index

def z_naive(P,T):

    s = P+"$"+T

    size = len(P)
    Z = [0]
    index = []

    for k in range(1, len(s)):
        n = 0
        while n + k < len(s) and s[n] == s[n + k]:
            n += 1
        Z.append(n)

    for k in range(len(Z)):
        aux = Z[k]
        if aux == size:
            index.append(aux-size+1)

    return index
