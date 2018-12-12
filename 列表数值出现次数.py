a=[1,2,3,3,3,3,7,7,8,8,10]
print(a)
news_ids = []
for id in a:
    if id not in news_ids:
        news_ids.append(id)
print (news_ids)
for i in news_ids:
    if a.count(i) >= 1:
        print('%s 出现了%d 次!'%(i, a.count(i)))

#纯手写
