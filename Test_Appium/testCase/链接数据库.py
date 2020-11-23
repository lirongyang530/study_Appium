#
#
# import sys
# import pymysql
# # 打开数据库连接
# db = pymysql.connect("10.37.49.245","mod_all","mod_all","chaoscloud_monitor" ,charset='utf8')
#
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
#
# # SQL 查询语句
# sql = "SELECT * FROM data_command WHERE meter_code='PUB0001'"
#
# # 执行SQL语句
# cursor.execute(sql)
# # 获取所有记录列表
# results = cursor.fetchall()
# print(results)
#
#
# # 关闭数据库连接
# db.close()




import sys
import pymysql
# 打开数据库连接
db = pymysql.connect(
    "10.240.0.103",
    "read_only",
    "read_only",
    "chaoscloud_monitor" ,
    charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM data_command"

# 执行SQL语句
cursor.execute(sql)
# 获取所有记录列表
results = cursor.fetchall()
print(results)


# 关闭数据库连接
db.close()