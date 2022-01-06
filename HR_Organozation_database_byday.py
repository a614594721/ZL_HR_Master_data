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
    url = config.url_HR_Organozation + '?token=' + config.token + '&pageSize='+str(config.pageSize)+'&pageNum='+str(pageNum)
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
    orgid = formDetail["orgid"]  # 组织ID
    orgcode = formDetail["orgcode"]  # 组织编码
    orgname = formDetail["orgname"]  # 组织名称
    orglevel = formDetail["orglevel"]  # 组织层级
    orgadminpost = formDetail["orgadminpost"]  # 组织单位负责岗位
    companytype = formDetail["companytype"]  # 公司类型
    suporgid = formDetail["suporgid"]  # 上级组织ID
    displayindex = formDetail["displayindex"]  # 显示顺序
    sealup = formDetail["sealup"]  # 是否叶节点
    createdatetime = formDetail["createdatetime"]  # 创建时间
    isenable = formDetail["isenable"]  # 有效状态
    lastmodifydatetime = formDetail["lastmodifydatetime"]  # 最后修改时间
    cityname = formDetail["cityname"]  # 城市名称
    psorglevel = formDetail["psorglevel"]  # Ps层级
    orgtype = formDetail["orgtype"]  # 组织类型
    orgtypedescr = formDetail["orgtypedescr"]  # PS原始组织层级描述
    changestatus = formDetail["changestatus"]  # 组织变动状态
    superorgunitcode = formDetail["superorgunitcode"]  # 上级组织编码
    superorgunitname = formDetail["superorgunitname"]  # 上级组织名称
    systemcode = formDetail["systemcode"]  # 来源
    isshow = formDetail["isshow"]  # 钉钉显示部门信息
    orgleveldescr = formDetail["orgleveldescr"]  # 组织层级描述
    cbuOrgName = formDetail["cbuOrgName"]  # 业务名称
    cbuOrgId = formDetail["cbuOrgId"]  # 业务ID
    cbuOrgCode = formDetail["cbuOrgCode"]  # 业务编码


   # 打开数据库连接
    db = pymysql.connect(host=host, user=user,
                         password=password, database=database, port=port)

    # 使用cursor()方法获取操作游标
    cur = db.cursor()

    sql_insert = """insert into HR_Organozation (
            orgid	 ,
            orgcode	 ,
            orgname	 ,
            orglevel	 ,
            orgadminpost	 ,
            companytype	 ,
            suporgid	 ,
            displayindex	 ,
            sealup	 ,
            createdatetime	 ,
            isenable	 ,
            lastmodifydatetime	 ,
            cityname	 ,
            psorglevel	 ,
            orgtype	 ,
            orgtypedescr	 ,
            changestatus	 ,
            superorgunitcode	 ,
            superorgunitname	 ,
            systemcode	 ,
            isshow	 ,
            orgleveldescr	 ,
            cbuOrgName	 ,
            cbuOrgId	 ,
            cbuOrgCode	 
           ) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    # print(sql_insert)

    try:
        cur.execute(sql_insert, (orgid	 ,
            orgcode	 ,
            orgname	 ,
            orglevel	 ,
            orgadminpost	 ,
            companytype	 ,
            suporgid	 ,
            displayindex	 ,
            sealup	 ,
            createdatetime	 ,
            isenable	 ,
            lastmodifydatetime	 ,
            cityname	 ,
            psorglevel	 ,
            orgtype	 ,
            orgtypedescr	 ,
            changestatus	 ,
            superorgunitcode	 ,
            superorgunitname	 ,
            systemcode	 ,
            isshow	 ,
            orgleveldescr	 ,
            cbuOrgName	 ,
            cbuOrgId	 ,
            cbuOrgCode))
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
