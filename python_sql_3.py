# import libraries
import os
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import (Table, Column, Integer, Numeric, String, Boolean, ForeignKey)
from sqlalchemy import DateTime
from sqlalchemy import ForeignKeyConstraint, create_engine
from sqlalchemy import insert

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

# load tables
# if commit is not used, any changes is in transaction buffer stage, but not happened in database yet
# after using commit it updates
# if commit is not used while executing, ID will not rollback to 1 it will be the new one

metadata = MetaData()
cookies = Table('cookies', metadata, autoload_with=engine_)

# single insert
ins = insert(cookies).values(cookie_name = 'chocolate chip',
                             cookie_recipe_url = 'http://some.aweso.me/cookie/recipe.html',
                             cookie_sku = 'CC01',
                             quantity = '12',
                             unit_cost = '0.5')

res = conn.execute(ins)
conn.commit()