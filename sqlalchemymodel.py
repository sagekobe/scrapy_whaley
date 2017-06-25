
# -*- coding:utf-8 -*-

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#基类
Base = declarative_base()

#定义引擎，连接数据库
engine = create_engine('mysql+pymysql://root:zjy199291@localhost:3306/testwhaley?charset=utf8')


class whayelinfo(Base):
    __tablename__ = 'whayelinfo'
    id = Column(Integer, primary_key=True)
    wt_names = Column(String(64))
    wt_sales = Column(String(32))
    wt_prices = Column(String(32))
    wt_comments_number = Column(String(32))
    


#找到Base下所有的子类，然后在数据库中创建这些表，如上面的whayelinfo表
Base.metadata.create_all(engine)

#引入数据库会话类，提供对数据库的操作
Session = sessionmaker(bind=engine)

#session = Session()

