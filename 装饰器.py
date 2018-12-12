#装饰器的应用场景：比如插入日志，性能测试，事务处理，缓存等等场景。
def outer(func):
    def inner(*args,**kwargs):
        print("认证成功！")
        result = func(*args,**kwargs)
        print("日志添加成功")
        return result
    return inner

@outer
def f1(name,age):
    print("%s 正在连接业务部门1数据接口......"%name)

# 调用方法
f1("jack",18)
#装饰器调用方法，其实是把函数 f1 当成 outer的参数 
