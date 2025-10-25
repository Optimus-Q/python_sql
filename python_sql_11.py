# import libraries
import os
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import (Table, Column, Integer, Numeric, String, Boolean, ForeignKey)
from sqlalchemy import DateTime
from sqlalchemy import ForeignKeyConstraint, create_engine
from sqlalchemy import insert, select, desc, asc, and_, or_ , distinct, func, update, delete

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
users = Table('users', metadata, autoload_with=engine_)
orders = Table('orders', metadata, autoload_with=engine_)
line = Table('line_items', metadata, autoload_with=engine_)


customer_list = [
    {
        'user_name': "cookiemon",
        'email_address': "mon@cookie.com",
        'phone': "111-111-1111",
        'password': "password"
    },
    {
        'user_name': "cakeeater",
        'email_address': "cakeeater@cake.com",
        'phone': "222-222-2222",
        'password': "password"
    },
    {
        'user_name': "pieguy",
        'email_address': "guy@pie.com",
        'phone': "333-333-3333",
        'password': "password"
    }
]

# insert multiple
query_ = insert(users)
res = conn.execute(query_, customer_list)
conn.commit()

# insert orders 
order_ins = insert(orders).values(user_id = 1)
order_ins_ex = conn.execute(order_ins)
conn.commit()

order_items = [
    {
        'order_id': 1,
        'cookie_id': 1,
        'quantity': 2,
        'extended_cost': 1.00
    },
    {
        'order_id': 1,
        'cookie_id': 3,
        'quantity': 12,
        'extended_cost': 3.00
    }
]

line_ins = insert(line)
line_ex = conn.execute(line_ins, order_items)
conn.commit()

order_ins = insert(orders).values(user_id = 2)
order_ins_ex = conn.execute(order_ins)
conn.commit()

order_items = [
    {
        'order_id': 2,
        'cookie_id': 1,
        'quantity': 24,
        'extended_cost': 12.00
    },
    {
        'order_id': 2,
        'cookie_id': 4,
        'quantity': 6,
        'extended_cost': 6.00
    }
]

line_ins = insert(line)
line_ex = conn.execute(line_ins, order_items)
conn.commit()