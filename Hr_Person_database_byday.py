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
    url = config.url_HrPerson + '?token=' + config.token + '&pageSize='+str(config.pageSize)+'&pageNum='+str(pageNum)
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
    personcode = formDetail["personcode"]  # 员工编码
    personname = formDetail["personname"]  # 员工姓名
    ad = formDetail["ad"]  # AD账号
    employmentrelationship = formDetail["employmentrelationship"]  # 用工关系
    usertypename = formDetail["usertypename"]  # 员工类型
    mobilephone = formDetail["mobilephone"]  # 手机号码
    officephone = formDetail["officephone"]  # 办公电话
    email = formDetail["email"]  # 邮件地址
    dateofbirth = formDetail["dateofbirth"]  # 出生日期
    gender = formDetail["gender"]  # 性别
    maritalstatus = formDetail["maritalstatus"]  # 婚姻状况
    educationlevel = formDetail["educationlevel"]  # 教育程度
    nationality = formDetail["nationality"]  # 国籍
    nation = formDetail["nation"]  # 民族
    certificatestype = formDetail["certificatestype"]  # 证件类型
    idnumber = formDetail["idnumber"]  # 证件号码
    entrydate = formDetail["entrydate"]  # 入职日期
    leavedate = formDetail["leavedate"]  # 离职日期
    isenable = formDetail["isenable"]  # 在职状态（是否有效）
    rank = formDetail["rank"]  # 职级
    lastmodifydatetime = formDetail["lastmodifydatetime"]  # 最后修改时间
    genderCode = formDetail["genderCode"]  # genderCode
    systemcode = formDetail["systemcode"]  # 系统来源
    shutdt = formDetail["shutdt"]  # 账户关闭时间
    notOpenOa = formDetail["notOpenOa"]  # 是否开通OA
    nationalityCode = formDetail["nationalityCode"]  # nationalityCode
    dimensionCode = formDetail["dimensionCode"]  # dimensionCode
    educationCode = formDetail["educationCode"]  # educationCode
    paperTypeCode = formDetail["paperTypeCode"]  # paperTypeCode
    nationCode = formDetail["nationCode"]  # 城市编码
    maritalStatusCode = formDetail["maritalStatusCode"]  # maritalStatusCode
    bussinessSysCode = formDetail["bussinessSysCode"]  # bussinessSysCode

    # 打开数据库连接
    db = pymysql.connect(host=host, user=user,
                         password=password, database=database, port=port)

    # 使用cursor()方法获取操作游标
    cur = db.cursor()

    sql_insert = """insert into Hr_Person (
            personcode	,
            personname	,
            ad	,
            employmentrelationship	,
            usertypename	,
            mobilephone	,
            officephone	,
            email	,
            dateofbirth	,
            gender	,
            maritalstatus	,
            educationlevel	,
            nationality	,
            nation	,
            certificatestype	,
            idnumber	,
            entrydate	,
            leavedate	,
            isenable	,
            rank	,
            lastmodifydatetime	,
            genderCode	,
            systemcode	,
            shutdt	,
            notOpenOa	,
            nationalityCode	,
            dimensionCode	,
            educationCode	,
            paperTypeCode	,
            nationCode	,
            maritalStatusCode	,
            bussinessSysCode	
           ) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    # print(sql_insert)

    try:
        cur.execute(sql_insert, (personcode	,
            personname	,
            ad	,
            employmentrelationship	,
            usertypename	,
            mobilephone	,
            officephone	,
            email	,
            dateofbirth	,
            gender	,
            maritalstatus	,
            educationlevel	,
            nationality	,
            nation	,
            certificatestype	,
            idnumber	,
            entrydate	,
            leavedate	,
            isenable	,
            rank	,
            lastmodifydatetime	,
            genderCode	,
            systemcode	,
            shutdt	,
            notOpenOa	,
            nationalityCode	,
            dimensionCode	,
            educationCode	,
            paperTypeCode	,
            nationCode	,
            maritalStatusCode	,
            bussinessSysCode))
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
