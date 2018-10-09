from model.models import AdminInfo
from sqlalchemy import create_engine

# 创建一个和mysql数据库之间的连接引擎对象
engine = create_engine("mysql://root:000000@localhost/blog_web", encoding="utf-8", echo=True)
