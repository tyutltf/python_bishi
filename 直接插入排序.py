#1.直接插入排序
L = [1, 3, 2, 32, 15, 5, 4]
def Insert_sort(L):
    for i in range(1,len(L)):
        for j in range(0,i):#这里面其实也是从前向后比较
            if L[i]<L[j]:
                L.insert(j,L[i])#在不大于的位置插入L[i],这个时候，列表加长了1位,L[i]插入到指定位置了，但它的值也向后移动了一位
                L.pop(i+1)#把原来L[i]的值删除。
    print(L)
    #空间复杂度为O（1），时间复杂度为O（n*n）
Insert_sort(L)
# print sorted(L)#自带的两种排序
# L.sort()
# print L
