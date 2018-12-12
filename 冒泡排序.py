'''
冒泡排序（Bubble Sort），是一种计算机科学领域的较简单的排序算法。
它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
这个算法的名字由来是因为越大的元素会经由交换慢慢“浮”到数列的顶端，故名“冒泡排序”。
'''

import random
# 步骤2：创建一个空列表，用于存放待排序随机数据集
data = [random.randint(0, 100) for i in range(10)]
print('待排序的随机数列: {0}'.format(data))
# 步骤3：使用嵌套循环实现冒泡排序
# 外层循环控制排序的次数
for i in range(10):
    # 内层循环控制每次对比的次数
    for j in range(len(data)-1-i):
        # 如果前项值大于后项值则对位交换，将大的在列表中后移1位
        if data[j] > data[j+1]:
            temp = data[j]
            data[j] = data[j+1]
            data[j+1] = temp
            pass
# 步骤4：输出排序后的结果
print('排序后的有序序列: {0}'.format(data))


#交换排序.冒泡排序
L = [1, 3, 2, 32, 5, 4]
def Bubble_sort(L):
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if L[i]>L[j]:
                # temp = L[j]
                # L[j] = L[i]
                # L[i] = temp
                L[i], L[j] = L[j], L[i]#交换顺序

    print (L)
Bubble_sort(L)
