l=[1,2,[3,4,[5,6],[7,8],9],10]
l1=[]
#递归函数实现：
def getitem(l):
    for item in l:
        if isinstance(item,list):
            getitem(item)
        else:
            print(item)
            l1.append(item)

getitem(l)
print(l1)
#python利用递归函数输出嵌套列表的每个元素 - lincappu - 博客园  https://www.cnblogs.com/lincappu/p/8146055.html
