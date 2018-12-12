dic=b'{"name":"ltf","school":"tyut"}'
str(dic, encoding="utf-8")
print(dic)
dicBytes = dic.decode('utf-8')
print(dicBytes)
print(eval(dicBytes)) #字符串转换为字典
print(eval(dicBytes).keys())

#修改key
dict = {'a':'ltf','b':'fjf'}
dict.update({'1':dict.pop("a")})
dict.update({'2':dict.pop("b")})
print(dict)
