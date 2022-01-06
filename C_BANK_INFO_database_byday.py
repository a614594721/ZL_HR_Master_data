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
    url = config.url_C_BANK_INFO + '?token=' + config.token + '&pageSize='+str(config.pageSize)+'&pageNum='+str(pageNum)
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
    emplcd = formDetail["emplcd"]  # OA账号
    cAccountNature = formDetail["cAccountNature"]  # 账户类型
    bankNm = formDetail["bankNm"]  # 银行类别名称
    bankCd = formDetail["bankCd"]  # 银行类别编码
    cBranchNm = formDetail["cBranchNm"]  # 银行档案名称
    branchEcCd = formDetail["branchEcCd"]  # 银行档案编码
    accountEcId = formDetail["accountEcId"]  # 银行账号
    indSpecialChar = formDetail["indSpecialChar"]  # 身份证
    name = formDetail["name"]  # 员工姓名
    combineaccnum = formDetail["combineaccnum"]  # 人行联行号
    combineaccname = formDetail["combineaccname"]  # 人行联行号名称
    combinenum = formDetail["combinenum"]  # 联行号
    areacode = formDetail["areacode"]  # 地区代码
    bankarea = formDetail["bankarea"]  # 开户地区
    orgnumber = formDetail["orgnumber"]  # 机构号/分行号
    province = formDetail["province"]  # 省份
    city = formDetail["city"]  # 城市
    customernumber = formDetail["customernumber"]  # 客户编码
    accountproperty = formDetail["accountproperty"]  # 账户性质
    nidSpecialChar = formDetail["nidSpecialChar"]  # 身份证

   # 打开数据库连接
    db = pymysql.connect(host=host, user=user,
                         password=password, database=database, port=port)

    # 使用cursor()方法获取操作游标
    cur = db.cursor()

    sql_insert = """insert into C_BANK_INFO (
            emplcd	,
            cAccountNature	,
            bankNm	,
            bankCd	,
            cBranchNm	,
            branchEcCd	,
            accountEcId	,
            indSpecialChar	,
            name	,
            combineaccnum	,
            combineaccname	,
            combinenum	,
            areacode	,
            bankarea	,
            orgnumber	,
            province	,
            city	,
            customernumber	,
            accountproperty	,
            nidSpecialChar		
           ) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    # print(sql_insert)

    try:
        cur.execute(sql_insert, (emplcd	,
        cAccountNature	,
        bankNm	,
        bankCd	,
        cBranchNm	,
        branchEcCd	,
        accountEcId	,
        indSpecialChar	,
        name	,
        combineaccnum	,
        combineaccname	,
        combinenum	,
        areacode	,
        bankarea	,
        orgnumber	,
        province	,
        city	,
        customernumber	,
        accountproperty	,
        nidSpecialChar
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
