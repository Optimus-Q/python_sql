# import libraries
import os
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import (Table, Column, Integer, Numeric, String, Boolean, ForeignKey)
from sqlalchemy import DateTime
from sqlalchemy import ForeignKeyConstraint, create_engine

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


# create table
# we need meta table to create table for thread safe
metadata = MetaData()
cookies_tb = Table('cookies', metadata,
                   Column('cookie_id', Integer(), autoincrement= True, primary_key=True),
                   Column('cookie_name', String(50), index=True),
                   Column('cookie_recipe_url', String(255)),
                   Column('cookie_sku', String(55)),
                   Column('quantity', Integer()),
                   Column('unit_cost', Numeric(12, 2)))

users_tb = Table('users', metadata,
                 Column('user_id', Integer(), autoincrement= True, primary_key=True),
                 Column('user_name', String(15), nullable=False, unique=True),
                 Column('email_address', String(255), nullable=False),
                 Column('phone', String(20), nullable=False),
                 Column('password', String(25), nullable=False),
                 Column('created_on', DateTime(), default=datetime.now()),
                 Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now()))

orders_tb = Table('orders', metadata,
                  Column('order_id', Integer(), autoincrement= True, primary_key=True),
                  Column('user_id', ForeignKey('users.user_id')),
                  Column('shipped', Boolean(), default=False))

line_items_tb = Table('line_items', metadata,
                      Column('line_items_id', Integer(), autoincrement= True, primary_key=True),
                      Column('order_id', ForeignKey('orders.order_id')),
                      Column('cookie_id', ForeignKey('cookies.cookie_id')),
                      Column('quantity', Integer()),
                      Column('extended_cost', Numeric(12, 2)))

engine = create_engine(host_url)
metadata.create_all(engine)