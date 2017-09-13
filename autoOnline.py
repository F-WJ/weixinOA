import pymysql
import re
import sys


class shortInputEx(Exception):
  def __init__(self,ip):
   self.ip=ip


db=pymysql.connect("localhost",'root','kumanxuan@gzitcast','xingzheng',charset='utf8')
mysql = db.cursor(pymysql.cursors.DictCursor)
print("this py is about autoOnline when get a new ip address")

ipAddressInfo = input("请输入你要设置上网的ip地址:")
print(ipAddressInfo)

##set a 正则匹配
matchInfo = re.search(r"^192\.168\.([1-9][0-9]?|1[0-9][0-9]|2[0-4][0-9]|25[0-4])\.(?:(?:1[0-9][0-9])|(?:2[0-4][0-9])|(?:25[0-5])|(?:[1-9][0-9])|(?:[0-9]))$",ipAddressInfo)


try:
  if(not matchInfo):
     raise shortInputEx(ipAddressInfo)
except  shortInputEx as BB:
     print('你输入的ip地址有误，这是你刚刚输入的ip地址%s' %(BB.ip))
else:
     print('check it out,OK')

if(matchInfo):
  print("got it")
else:
  print("ERROR,you input a wrong IP")
  sys.exit()
#print(matchInfo)
ipInfo = matchInfo.group(0)
#ipInfo = re.search(r"(?<=192\.168\.)\d+",matchInfo)
#print(ipInfo)
ipRange = re.split(r'\.',ipInfo)
print(ipRange)
sql = "select * from classroom where ipAddress = '%s'" %(ipRange[2])

try:
  mysql.execute(sql)
  result = mysql.fetchall()
  if(result):
    print(result)
  else:
    print("error,404 not found")
  

except:
  print("error")

if(not result):
  print("bye bye!!")
  sys.exit



