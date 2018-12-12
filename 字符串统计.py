str='mynameisbobiamfromchina嘿嘿嘿嘿'
str=','.join(str) #以逗号分隔字符串
print(str)
li=str.split(',')
print(li) #变成列表了
#统计每一个字符出现的次数:
for i in set(li):
    if li.count(i) >= 1:
        print('%s 出现了%d 次!'%(i, li.count(i)))

print('*'*50)
#方式二
from collections import Counter
res = Counter(li)
print(res)
