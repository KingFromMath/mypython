# -*- coding: utf-8 -*-
"""
create at:17-3-6 下午1:35
create by:duanyuping
create for:
  ┏┓   ┏┓
 ┏┛┻━━━┛┻┓
 ┃   ☃  ┃
 ┃ ┳┛ ┗┳ ┃
 ┃   ┻   ┃
 ┗━┓   ┏━┛
   ┃   ┗━━━┓
   ┃ 神兽保佑 ┣┓
   ┃ 永无BUG！ ┏┛
   ┗┓┓┏━┳┓┏┛
    ┃┫┫  ┃┫┫
    ┗┻┛  ┗┻┛
"""
'''
*argv/*kwargs
标准参数，*args，**kwargs混合使用的顺序： Function(标准参赛, *args, **kwargs)
'''
# *argv用于发送一个非键值对的可变数量的参数列表给一个函数

#在函数中使用 *argv作为参数
def testArgs(*argv):
    for arg in argv:
        print(arg)

# testArgs('a', 'b', 'c', 'd')

#使用 *argv作为参数调用单数
def testArgsOne(arg1, arg2, arg3):
    print(arg1)
    print(arg2)
    print(arg3)

# args = (1,2,3)
# testArgsOne(*args)

# **kwargs允许你将不定长度的键值对,作为参数传递给一个函数
def testArgsTwo(**kwargs):
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))

# testArgsTwo(name='duanyuping')

# kwargs = {"arg1":11, "arg2":12, "arg3":13}
# testArgsOne(**kwargs)



'''
Generators
Iteratoes迭代器：一个可以遍历每一个成员的容器对象，生成器是一种在运行时生成迭代值的迭代器，
也就是不会一次把所有的值存放到内存中，而是需要时在去取。
'''
def generator():
    for i in range(10):
        yield i

# for item in generator():
#     print(item)

def fibon(n):
    a = b = 1
    for i in range(n):
        yield a

        a, b = b, a+b

# for x in fibon(100):
#     print(x)

#字符串对象是可迭代的，但是不是迭代器，需要借助iter函数转换为可迭代对象
testString = 'duanyuping'
testIter = iter(testString)
# for i in testIter:
#     print(i)


'''
Map/Filter
'''
#map将一个函数映射到输入列表的所有元素上
items = [1,2,3,4,5,6]
squared = list(map(lambda x: x**2, items))
# print(squared)

#Filter能创建一个列表,其中每个元素都是对一个函数能返回True
filterList = range(-5, 5)
filterList_ = list(filter(lambda x: x<0, filterList))
# print(filterList_)

'''
Set
'''
#检测重复值
someList = [1,2,3,4,2,3,4,3,54,34,3,3,2,1,3,3,2]
duplicates = set([x for x in someList if someList.count(x)>1])    #list.count(somevalue) 表示somevalue在list中的个数
# print(duplicates)

#交集
setOne = set([1,2,3,4,4])        #等价于setOne = {1,2,3,4}
setTwo = set([2,4,3,5,6])

# print(setOne.intersection(setTwo))

#补集
setThree = set([3,2])
# print(setOne.difference(setThree))


'''
三元运算符
'''
fat = True
state = "fat" if fat else "not fat"
# print(state)


'''
装饰器/闭包
装饰器让你在执行一个函数的前后去执行代码
在python中一切皆对象
'''
#函数与变量，函数可以传递给变量
def func(name="boy"):
    return name
# print(func())

greet= func    #把函数作为变量赋值给greet，所以这里没有小括号
# print(greet())

#在函数中定义函数
def funcOne(name="boy"):
    print(name)

    def greet():
        return "123"

    print(greet())

# funcOne()    #只要调用母函数，子函数就会被调用

#从函数中返回函数
def funcTwo(name="yarn"):
    def greet():
        return "123"
    def welcome():
        return "345"

    # if name == "yarn":
    #     return greet
    # else:
    #     return welcome

    return greet if name == "yarn" else welcome

# result = funcTwo()
# print(result)    #<function funcTwo.<locals>.greet at 0x7fcd5823ff28>
# print(result())


#将函数作为参数传递给另一个对象
def funcThree():
    return "hi boy!"

def doSomethingBeforeFunc(args):
    print(args())

# doSomethingBeforeFunc(funcThree)

#装饰器(一)
def aNewDecorator(args):
    def wrapTheFunction():
        print("123456")

        args()
        print("7898")
    return wrapTheFunction

def aFunctionRequireDecoretion():
    print('duanyuping')

#把函数aFunctionRequireDecoretion作为参数传递给aNewDecorator，aNewDecorator返回一个内置的函数，testParam()执行这个返回的函数
# testParam = aNewDecorator(aFunctionRequireDecoretion)
# testParam()

#装饰器(二)
from functools import wraps

def aNewDecorator(args):
    @wraps(args)
    def wrapTheFunction():
        print("123456123")

        args()
        print("7898a")
    return wrapTheFunction

@aNewDecorator
def aFunctionRequireDecoretion():
    print('duanyuping')

#功能同上，也就是在执行aFunctionRequireDecoretion前，先调用aNewDecorator
# print(aFunctionRequireDecoretion.__name__)
# aFunctionRequireDecoretion()

#装饰器(三)
def logit(func):
    @wraps(func)
    def withLogging(*args, **kwargs):
        print(func.__name__+"was colled")

        return func(*args, **kwargs)
    return withLogging

@logit
def addtionFunc(x):
    return x+x

# result = addtionFunc(4)
# print(result)




