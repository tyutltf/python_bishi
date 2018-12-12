ids = [1,2,3,3,4,2,3,4,5,6,1,6,4,3,2,3,]
news_ids = []
for id in ids:
    if id not in news_ids:
        news_ids.append(id)
print (news_ids)
#python 列表去重(数组)的几种方法 - 朝阳的向日葵 - 博客园  https://www.cnblogs.com/zknublx/p/6042295.html
ids = list(set(ids))
print(ids)  #一句话列表去重

#lambda 一句话列表去重
a=(lambda x,y:x if y in x else x + [y], [[],] + ids)
print(a)
