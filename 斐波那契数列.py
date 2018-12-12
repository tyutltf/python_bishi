#最简单的方法为数组，其次为循环，最垃圾的为递归，到了40就算好久。。日后再琢磨数组

a=[1,1]
def fn(n):
    count=0
    f0=1
    f1=1
    f2=0
    while count<n:
        count+=1
        f2=f1+f0
        f0=f1
        f1=f2
        a.append(f2)
    print('第%s项的项数为:%s'%(b,f2))
    print('斐波那契数列为:')
    print(a)
b=int(input('请输入项数:'))
fn(b-2)
