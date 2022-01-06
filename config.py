import datetime

# 数据库配置--本地测试环境
# 查询的数据库
host="127.0.0.1"
user="root"
password="123456"
database="private"
port=3306 # sqlserver1433 mysql3306
# # 数据库配置-- bpm生产环境
# # # 查询的数据库
# host="10.10.15.26"
# user="sa"
# password="xdFW@SQL2021"
# database="BPM_FormData"
# port=1433 # sqlserver1433 mysql3306

#########################

token='d1591232-63a0-46d5-b9e5-38ad19e63e8e'
url_HrPerson = 'http://139.224.219.5:8965/person-service/HrPerson/selectHrPerson'
url_HrPersonExtend ='http://139.224.219.5:8965/person-service/HrPersonExtend/selectHrPersonExtend'
url_HR_Organozation = 'http://139.224.219.5:8965/person-service/HrOrganization/selectHrOrganization'
url_HR_Post = 'http://139.224.219.5:8965/person-service/HrPost/selectHrPost'
url_C_BANK_INFO = 'http://139.224.219.5:8965/person-service/CBankInfo/selectCBankInfo'
pageSize = 1000

"""create  table Hr_Person(
personcode	 	varchar(50)	,
personname	 	nvarchar(50)	,
ad	 	varchar(50)	,
employmentrelationship	 	nvarchar(50)	,
usertypename	 	nvarchar(50)	,
mobilephone	 	varchar(50)	,
officephone	 	varchar(50)	,
email	 	varchar(100)	,
dateofbirth	 	datetime	,
gender	 	nvarchar(10)	,
maritalstatus	 	nvarchar(50)	,
educationlevel	 	nvarchar(50)	,
nationality	 	nvarchar(50)	,
nation	 	nvarchar(50)	,
certificatestype	 	nvarchar(50)	,
idnumber	 	nvarchar(50)	,
entrydate	 	datetime	,
leavedate	 	datetime	,
isenable	 	nvarchar(50)	,
rank	 	nvarchar(50)	,
lastmodifydatetime	 	datetime	,
genderCode	 	varchar(50)	,
systemcode	 	varchar(50)	,
shutdt	 	datetime	,
notOpenOa	 	varchar(50)	,
nationalityCode	 	varchar(50)	,
dimensionCode	 	varchar(50)	,
educationCode	 	varchar(50)	,
paperTypeCode	 	varchar(50)	,
nationCode	 	varchar(50)	,
maritalStatusCode	 	varchar(50)	,
bussinessSysCode	 	varchar(50)	
)"""

"""create  table Hr_PersonExtend(
personid	 	varchar(50)	,
employeeid	 	varchar(50)	,
personcode	 	varchar(50)	primary key ,
psPostcode	 	nvarchar(50)	,
psPostname	 	varchar(50)	,
corepostcode	 	nvarchar(50)	,
corepostname	 	varchar(50)	,
employeestatus	 	int	,
isentryagain	 	nvarchar(50)	,
psEmployeetype	 	nvarchar(50)	,
isinsystem	 	varchar(50)	,
orgid	 	varchar(50)	,
buorgid	 	varchar(50)	,
regionalcompanyorgid	 	varchar(50)	,
regionalgrouporgid	 	varchar(50)	,
managerpercode	 	varchar(50)	,
oldemployeeid	 	varchar(50)	,
firstleveldept	 	nvarchar(50)	,
legalcompany	 	nvarchar(50)	,
legalcompanydescr	 	nvarchar(50)	,
accountdept	 	nvarchar(50)	,
accountdeptdescr	 	nvarchar(50)	,
accounttype	 	nvarchar(50)	,
accounttypedescr	 	nvarchar(50)	,
psSystem	 	nvarchar(50)	,
leavereason	 	nvarchar(200)	,
deptname	 	varchar(200)	,
isenable	 	varchar(50)	,
alliancecenterorgid	 	varchar(50)	,
systemcode	 	varchar(50)	,
notopending	 	varchar(50)	,
ishide	 	varchar(200)	,
dateofbirth	 	varchar(200)	,
psStripline	 	varchar(200)	,
notOpenOa	 	nvarchar(50)	,
supervisorCode	 	nvarchar(64)	,
effdt	 	varchar(50)	,
businessUnit	 	varchar(100)	,
businessDescr	 	varchar(200)	,
gpBpmFlag	 	varchar(64)	,
FIRST_LEVEL_DEPT_NAME	 	varchar(50)	
)"""

"""create table HR_Organozation(
orgid	 	varchar(50)	 primary key ,
orgcode	 	varchar(50)	not null unique,
orgname	 	nvarchar(50)	,
orglevel	 	nvarchar(50)	,
orgadminpost	 	varchar(50)	,
companytype	 	nvarchar(50)	,
suporgid	 	varchar(50)	,
displayindex	 	int	,
sealup	 	int	,
createdatetime	 	datetime	,
isenable	 	int	,
lastmodifydatetime	 	datetime	,
cityname	 	nvarchar(50)	,
psorglevel	 	nvarchar(50)	,
orgtype	 	nvarchar(50)	,
orgtypedescr	 	nvarchar(50)	,
changestatus	 	nvarchar(50)	,
superorgunitcode	 	varchar(50)	,
superorgunitname	 	varchar(200)	,
systemcode	 	varchar(200)	,
isshow	 	varchar(50)	,
orgleveldescr	 	varchar(50)	,
cbuOrgName	 	varchar(50)	,
cbuOrgId	 	varchar(50)	,
cbuOrgCode	 	varchar(50)	
)"""

"""create table HR_Post(
postid	 	varchar(50) primary key 	,
postcode	 	varchar(50)	,
postname	 	nvarchar(50)	,
suppostid	 	varchar(50)	,
isenable	 	int	,
lastmodifydatetime	 	datetime	,
isdm	 	int	,
superpositioncode	 	int	,
superpositionname	 	nvarchar(50)	,
systemcode	 	varchar(50)	
)"""