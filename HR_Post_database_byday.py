# -*- coding: utf-8 -*-
# appSecret需要通过每刻申请
# 生产：
import json
import time
import config
import pymysql
import requests

host = config.host
user = config.user
password = config.password
database = config.database
port = config.port
pageSize = config.pageSize


def time_to_stampms(time_str):
    time_stamp = time.mktime(time.strptime(time_str, '%Y-%m-%d %H:%M:%S'))
    time_stampms = int(time_stamp * 1000)
    return time_stampms




def get_pageInfo(pageNum):
    url = config.url_HR_Post + '?token=' + config.token + '&pageSize='+str(config.pageSize)+'&pageNum='+str(pageNum)
    print(url)
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.get(url=url, headers=headers)  # param 可以用在get、post 请求中；data 只用在 post请求中
    return response.json()['pageInfo']




def insert_database(formDetail):
   # formDetail = str(formDetail).replace("'None',", "null,").replace("None,", "null,")
    # 数据解析
    # print(formDetail)
    # 表单详情
    postid = formDetail["postid"]  # 岗位ID
    postcode = formDetail["postcode"]  # 岗位编码
    postname = formDetail["postname"]  # 岗位名称
    suppostid = formDetail["suppostid"]  # 上级岗位
    isenable = formDetail["isenable"]  # 是否有效
    lastmodifydatetime = formDetail["lastmodifydatetime"]  # 最后修改时间
    isdm = formDetail["isdm"]  # 是否部门负责岗
    superpositioncode = formDetail["superpositioncode"]  # 上级岗位编码
    superpositionname = formDetail["superpositionname"]  # 上级岗位名称
    systemcode = formDetail["systemcode"]  # 来源系统

   # 打开数据库连接
    db = pymysql.connect(host=host, user=user,
                         password=password, database=database, port=port)

    # 使用cursor()方法获取操作游标
    cur = db.cursor()

    sql_insert = """insert into HR_Post (
            postid	,
            postcode	,
            postname	,
            suppostid	,
            isenable	,
            lastmodifydatetime	,
            isdm	,
            superpositioncode	,
            superpositionname	,
            systemcode	
           ) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    # print(sql_insert)

    try:
        cur.execute(sql_insert, (postid	,
            postcode	,
            postname	,
            suppostid	,
            isenable	,
            lastmodifydatetime	,
            isdm	,
            superpositioncode	,
            superpositionname	,
            systemcode
            ))
        # 提交
        db.commit()
    except Exception as e:
        # 错误回滚
        # print('错误信息：',e)
        with open("feikong_database.txt", "a", encoding='utf-8') as f:
            f.write('【' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "】未写入数据库的单据号："+ '  【错误信息为：' + str(e) + '】\n')
        db.rollback()
    finally:
        db.close()


if __name__ == '__main__':
    pageNum = 1
    pages = get_pageInfo(pageNum)['pages']
    # 获取单据列表

    while pageNum <= pages:
        print('pages:', pages, 'pageNum:', pageNum, 'pageSize:', config.pageSize)
        print('-'*30)
        pageInfo_list = get_pageInfo(pageNum)['list']
        # 获取单据详情
        for formDetail in pageInfo_list:
            insert_database(formDetail)
        pageNum += 1
