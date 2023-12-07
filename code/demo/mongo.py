from pymongo import MongoClient
from dotenv import load_dotenv
import sys
import os

# 加载 .env 文件
load_dotenv()

# 配置 MongoDB 连接信息
mongo_host = os.getenv("MONGO_HOST")
mongo_port = os.getenv("MONGO_PORT")
mongo_user = os.getenv("MONGO_USER")
mongo_password = os.getenv("MONGO_PASSWORD")
mongo_database = os.getenv("MONGO_DATABASE")

# 构建 MongoDB 连接字符串
connection_string = f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/{mongo_database}"

# 连接 MongoDB
client = MongoClient(connection_string)

# 选择数据库
db = client["your_database1"]

# 选择集合
collection = db["your_collection"]

# 执行查询或其他操作
result = collection.find_one()

# 关闭连接
client.close()

print(result)
sys.exit();


'''
docker exec python380_c python3 demo/mongo.py
'''
