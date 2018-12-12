'''
bob_ltf 输出 bobLtf
'''
s='bob_ltf_lsq_fjf'
s1=''
s2=''
arr=s.split('_') #列表
print(arr)
s1=s1.join(arr[1:])
print(s1.capitalize())
s2=s2.join(arr[:1])
s3=s2+s1.capitalize()
print(s3)
'''
输出结果
['bob', 'ltf', 'lsq', 'fjf']
Ltflsqfjf
bobLtflsqfjf
'''
