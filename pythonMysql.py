import pymysql

db = pymysql.connect("localhost",'root','kumanxuan@gzitcast','xingzheng',charset='utf8')

mysql = db.cursor(pymysql.cursors.DictCursor)

sql = "select * from classroom"

try:
  mysql.execute(sql)
  result = mysql.fetchall()
  for x in result:
    print(x)

except:
  print("error")

mysql.close()
