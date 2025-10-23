# import libraries
import os
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import (Table, Column, Integer, Numeric, String, Boolean, ForeignKey)
from sqlalchemy import DateTime
from sqlalchemy import ForeignKeyConstraint, create_engine
from sqlalchemy import insert, select, desc

# secrets dir
load_dotenv(dotenv_path = '.env')

# db user data
# format: #mysql+pymsql://username:passowrd@host:port/database
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
hostname = os.getenv("DB_HOST")
portnumber = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
host_url = f'mysql+pymysql://{username}:{password}@{hostname}:{portnumber}/{db_name}'

#sqlalchemy engine
engine_ = create_engine(url=host_url,
                        pool_recycle=3600)
conn = engine_.connect()

metadata = MetaData()
cookies = Table('cookies', metadata, autoload_with=engine_)

query_ = select(cookies)
res = conn.execute(query_).fetchall()
for r in res:
    print(r)

x = res[0]



res_1 = conn.execute(query_)

for r in res_1:
    print(r)

query_ = select(cookies.c.cookie_name, cookies.c.quantity)
res = conn.execute(query_)

for r in res:
    print(r)


query_ = select(cookies.c.cookie_name, cookies.c.quantity)
res = conn.execute(query_)

print(res.first())

query_ = select(cookies.c.cookie_name, cookies.c.quantity)
query_ = query_.order_by(desc(cookies.c.quantity,))
res = conn.execute(query_)

print(res.first())

query_ = select(cookies.c.cookie_name, cookies.c.quantity)
query_ = query_.order_by(cookies.c.quantity.desc())
res = conn.execute(query_)

print(res.first())

query_ = select(cookies.c.cookie_name, cookies.c.quantity)
query_ = query_.order_by(cookies.c.quantity.desc())
query_ = query_.limit(2)
res = conn.execute(query_)

print(res.fetchall())

