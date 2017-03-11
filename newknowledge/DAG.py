# -*- coding: utf-8 -*-
"""
create at:17-3-10 下午1:54
create by:duanyuping
create for: 获取DAG的拓扑序列
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

def indegree0(v, e):
    '''
    移除起始点和从他出发的有向线段
    :param v: v表示顶点：v=['a','b','c','d','e']
    :param e: e表示有向边：e=[('a','b'),('a','d'),('b','c'),('d','c'),('d','e'),('e','c')]
    :return:
    '''
    if v == []:
        return None

    tmp = v[:]    #获取全部元素

    # 遍历有向边，移除有向边终点在v中对应的元素，找到整个DAG的起始点------>找到起始点
    for i in e:
        if i[1] in tmp:
            tmp.remove(i[1])

    if tmp == []:
        return -1

    # 标记从起始点出发的有向线段------->找到从起始点出发的有向线段
    for t in tmp:
        for i in range(len(e)):
            if t in e[i]:
                e[i] = 'toDel'  # 占位，之后删掉

    '''下面这两步移除操作是针对全局变量的'''
    # 移除从起始点出发的有向线段
    if e:
        eset = set(e)
        eset.remove('toDel')
        e[:] = list(eset)

    # 移除v中的起始点
    if v:
        for t in tmp:
            v.remove(t)

    return tmp


def topoSort(v, e):
    '''
    作为驱动引擎，不停地调用indegree0函数，直到v中还有顶点却找不到指向他的起始点（说明不是有向无环图）
    :param v:
    :param e:
    :return:
    '''
    result = []
    while True:
        nodes = indegree0(v, e)
        # print(nodes)
        if nodes == None:
            break
        if nodes == -1:
            print('there\'s a circle.')
            return None
        result.extend(nodes)
    return result


v = ['a', 'c', 'b', 'd', 'e']
e = [('a', 'b'), ('a', 'd'), ('b', 'c'), ('d', 'c'), ('d', 'e'), ('e', 'c')]
res = topoSort(v, e)
print(res)



