num=[1,2,3,4,5,6,7,8,9,0]
cn=['壹','贰','叁','肆','伍','陆','柒','捌','玖','零']
dw=['元','十','百','千','万','十','百','千']
n=str(input('请输入数字:'))
c=len(n)-1
# print c
ln=''
c1=0
for i in n:
    nb = int(i) - 1
    if i=='0' and c1==0:
        c1=1
        pass
    else:
        if c1==1:
           c1=0
        ln=ln+ cn[nb]+dw[c]
        print(ln)
    c=c-1
print(ln)
