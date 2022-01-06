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
    url = config.url_HrPersonExtend + '?token=' + config.token + '&pageSize='+str(config.pageSize)+'&pageNum='+str(pageNum)
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
    personid = formDetail["personid"]  # id
    employeeid = formDetail["employeeid"]  # 员工ID
    personcode = formDetail["personcode"]  # 员工编码
    psPostcode = formDetail["psPostcode"]  # PS岗位编码
    psPostname = formDetail["psPostname"]  # PS岗位名称
    corepostcode = formDetail["corepostcode"]  # 核心岗位编码
    corepostname = formDetail["corepostname"]  # 核心岗位名称
    employeestatus = formDetail["employeestatus"]  # 试用/正式
    isentryagain = formDetail["isentryagain"]  # 是否重复入职
    psEmployeetype = formDetail["psEmployeetype"]  # PS员工类型
    isinsystem = formDetail["isinsystem"]  # 编内/编外
    orgid = formDetail["orgid"]  # 直属组织ID
    buorgid = formDetail["buorgid"]  # 所在事业部ID
    regionalcompanyorgid = formDetail["regionalcompanyorgid"]  # 所在区域公司ID
    regionalgrouporgid = formDetail["regionalgrouporgid"]  # 所在区域集团ID
    managerpercode = formDetail["managerpercode"]  # 所在部门负责人
    oldemployeeid = formDetail["oldemployeeid"]  # 员工ID
    firstleveldept = formDetail["firstleveldept"]  # 直属一级部门
    legalcompany = formDetail["legalcompany"]  # 法人公司
    legalcompanydescr = formDetail["legalcompanydescr"]  # 法人公司描述
    accountdept = formDetail["accountdept"]  # 入账部门
    accountdeptdescr = formDetail["accountdeptdescr"]  # 入账部门描述
    accounttype = formDetail["accounttype"]  # 入账类型
    accounttypedescr = formDetail["accounttypedescr"]  # 入账类型描述
    psSystem = formDetail["psSystem"]  # 体系
    leavereason = formDetail["leavereason"]  # 离职原因
    deptname = formDetail["deptname"]  # 部门全称
    isenable = formDetail["isenable"]  # 有效状态
    alliancecenterorgid = formDetail["alliancecenterorgid"]  # 联盟中心id
    systemcode = formDetail["systemcode"]  # 来源系统
    notopending = formDetail["notopending"]  # 是否开通钉钉
    ishide = formDetail["ishide"]  # 是否隐藏手机号
    dateofbirth = formDetail["dateofbirth"]  # 生日
    psStripline = formDetail["psStripline"]  # 体系
    notOpenOa = formDetail["notOpenOa"]  # 是否开通OA
    supervisorCode = formDetail["supervisorCode"]  # 直属上级
    effdt = ''  # 异动时间
    businessUnit = formDetail["businessUnit"]  # 业务单位编码
    businessDescr = formDetail["businessDescr"]  # 业务单位描述
    gpBpmFlag = formDetail["gpBpmFlag"]  # 是否有BPM薪酬权限
    FIRST_LEVEL_DEPT_NAME = ''  # 直属一级部门名称


   # 打开数据库连接
    db = pymysql.connect(host=host, user=user,
                         password=password, database=database, port=port)

    # 使用cursor()方法获取操作游标
    cur = db.cursor()

    sql_insert = """insert into Hr_PersonExtend (
            personid	,
            employeeid	,
            personcode	,
            psPostcode	,
            psPostname	,
            corepostcode	,
            corepostname	,
            employeestatus	,
            isentryagain	,
            psEmployeetype	,
            isinsystem	,
            orgid	,
            buorgid	,
            regionalcompanyorgid	,
            regionalgrouporgid	,
            managerpercode	,
            oldemployeeid	,
            firstleveldept	,
            legalcompany	,
            legalcompanydescr	,
            accountdept	,
            accountdeptdescr	,
            accounttype	,
            accounttypedescr	,
            psSystem	,
            leavereason	,
            deptname	,
            isenable	,
            alliancecenterorgid	,
            systemcode	,
            notopending	,
            ishide	,
            dateofbirth	,
            psStripline	,
            notOpenOa	,
            supervisorCode	,
            effdt	,
            businessUnit	,
            businessDescr	,
            gpBpmFlag	,
            FIRST_LEVEL_DEPT_NAME
           ) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    # print(sql_insert)

    try:
        cur.execute(sql_insert, (personid	,
            employeeid	,
            personcode	,
            psPostcode	,
            psPostname	,
            corepostcode	,
            corepostname	,
            employeestatus	,
            isentryagain	,
            psEmployeetype	,
            isinsystem	,
            orgid	,
            buorgid	,
            regionalcompanyorgid	,
            regionalgrouporgid	,
            managerpercode	,
            oldemployeeid	,
            firstleveldept	,
            legalcompany	,
            legalcompanydescr	,
            accountdept	,
            accountdeptdescr	,
            accounttype	,
            accounttypedescr	,
            psSystem	,
            leavereason	,
            deptname	,
            isenable	,
            alliancecenterorgid	,
            systemcode	,
            notopending	,
            ishide	,
            dateofbirth	,
            psStripline	,
            notOpenOa	,
            supervisorCode	,
            effdt	,
            businessUnit	,
            businessDescr	,
            gpBpmFlag	,
            FIRST_LEVEL_DEPT_NAME))
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
