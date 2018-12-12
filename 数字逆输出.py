# num=input('请输入一个数:')
# a=[]
# li=list(num)
# print(li)
# count=len(li)
# for i in range(len(li),0,-1):
#     count-=1
#     a.append(li[count])
# print(a)

num=input('请输入一个数:')
a=[]
str=''
print(num)
count=len(num)
for i in range(len(num),0,-1):
    count-=1
    a.append(num[count])
b=str.join(a)
print(int(b))


