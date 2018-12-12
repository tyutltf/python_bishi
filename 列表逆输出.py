a=[0,1,2,3,4,5,6,7,8,9,10]
b=[]
print(a[::-1]) #逆输出

#手写代码
count=len(a)
for i in range(len(a),0,-1):
    count-=1
    b.append(a[count])
print(b)
