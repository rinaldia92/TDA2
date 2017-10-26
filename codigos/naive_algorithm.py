import time

def naive_algorithm(P,T):
    start_time = time.time()
    sizep = len(P)
    sizet = len(T)
    cantcm = 0
    index = []
    for x in range(sizet - sizep + 1):
        for y in range (sizep):
            if P[y] == T[x+y]:
                cantcm = cantcm + 1
            else:
                continue
        if cantcm == sizep:
            index.append(x)
        cantcm = 0
    print ("My program took", time.time() - start_time, "to run")
    return index


#Precondicion: todos los patrones tienen la misma logitud m
def multi_naive_algorithm(P_set, T, m):
    start_time = time.time()
    sizep = m
    sizet = len(T)
    cantcm = 0
    index = []
    for sub in P_set:
        for x in range(sizet - sizep + 1):
            for y in range (sizep):
                if sub[y] == T[x+y]:
                    cantcm = cantcm + 1
                else:
                    continue
            if cantcm == sizep:
                index.append(x)
            cantcm = 0
    print ("My program took", time.time() - start_time, "to run")
    return index
