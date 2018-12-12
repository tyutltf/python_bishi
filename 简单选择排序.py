
L = [6, 3, 2, 32, 5, 4]
def Select_sort(L):
    for i in range(0,len(L)):
        for j in range(i,len(L)):
            if L[i] > L[j]:         #打擂台的形式
                # temp = L[i]
                # L[i] = L[j]
                # L[j] = temp
                L[i],L[j] = L[j],L[i]
    return  L
print (Select_sort(L))
