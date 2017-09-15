# _*_ coding: utf-8 _*_
__author__ = 'FWJ'
__date__ = 2017 / 9 / 14
# sqlalchemy官方有
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 连接数据库
engine = create_engine('mysql://root:kumanxuan@gzitcast@localhost:3306/xingzheng?charset=utf8')
Base = declarative_base()

Session = sessionmaker(bind=engine)






