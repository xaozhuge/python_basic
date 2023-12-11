import mysql.connector
from dotenv import load_dotenv
import os

# 加载 .env 文件
load_dotenv()

# 获取环境变量
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_database = os.getenv("DB_DATABASE")

# 连接到 MySQL 数据库
conn = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_database
)

# 创建一个游标对象
cursor = conn.cursor()

# 执行 SQL 查询语句
cursor.execute('SELECT id, event, lunar_date, solar_date FROM remind_date')

# 获取查询结果
results = cursor.fetchall()

# 遍历结果并输出
for row in results:
    print(row)

# 关闭数据库连接
conn.close()

'''
docker exec python380_c python3 demo/testmysql.py
'''
