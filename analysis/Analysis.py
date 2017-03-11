# -*- coding: utf-8 -*-
"""
create at:17-3-9 下午4:13
create by:duanyuping
create for: PostgreSQL开窗函数API
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
import json

def readJson(jsonFile):
    print(type(jsonFile))
    with open(jsonFile) as jsonString:
        data = json.loads(jsonString)
        print(data)


def main():
    readJson("/home/hadoop/PycharmProjects/mypython/analysis/elements.json")

if __name__ == '__main__':
    main()