import random

def selection(pop, popsize):
#selection
    newpop = []
    pop.reverse()
    for j in range(popsize):
        p = len(pop)
        if p == 0:
            break
        rank = []
        for i in range(p):
            rank.append(2*(i+1))
        batas_atas = []
        for i in range(p):
            batas_atas.append(sum(rank[0:i+1]))
        batas_bawah = [1]
        for i in range(p-1):
            batas_bawah.append(batas_atas[i]+1)
        pilih = random.randint(1, p*(p+1))
        for i in range(p):
            if (pilih >= batas_bawah[i]) and (pilih <= batas_atas[i]):
                newpop.append(pop[i])
                pop.remove(pop[i])
    return newpop