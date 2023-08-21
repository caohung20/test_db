import streamlit as st
import streamlit_authenticator as stauth
import yaml
import pandas as pd
from styles import Styles
from users import Users
from logs import Logs
import datetime as dt
import pytz
from connector import Database


utc_timezone = pytz.timezone('UTC')
local_timezone = pytz.timezone('Europe/Vienna')
timestamp = dt.datetime.now(pytz.timezone('UTC'))

    
class Orders(Database):
    def __init__(self):
        super().__init__()

    def query_row(self,row_name):
        query = f"""
        SELECT *
        FROM ORDERS
        WHERE NAME = {row_name}  
        ;
        """
        data = self.snowflake_connection.cursor().execute(query).fetchall()
        return data

    def query_columns(self, columns: list) -> str:
        return super().query_columns(columns)
    
    def create_table(self):
        query = f"""
        CREATE OR REPLACE TABLE ORDERS(
        ID int,
        NAME varchar(255),
        CREATED_TIMESTAMP TIMESTAMP
        );
        """
        data = self.snowflake_connection.cursor().execute(query).fetchall()
        return

    def post_entry(self,values:str):
        query = f"""
            INSERT INTO ORDERS( "NAME")
            VALUES(%s);"""    
        self.snowflake_connection.cursor().execute(query, values)
    
    def get_ord_name(self):
        query = f"""
        SELECT NAME
        FROM "ORDERS"
        """
        data = self.snowflake_connection.cursor().execute(query).fetchall()
        return data


class OrderItems(Database):
    def __init__(self):
        super().__init__()
          
    def query_columns(self, columns: list) -> str:
        return super().query_columns(columns)
    
    def create_table(self):
        query = f"""
        CREATE OR REPLACE TABLE ORDER_ITEMS(
        ID int,
        ORDER_ID int,
        ITEM_NAME varchar(255),
        CREATED_TIMESTAMP TIMESTAMP,
        PRICE int,
        COUNT int
        );
        """
        data = self.snowflake_connection.cursor().execute(query).fetchall()
        return
    def post_entry(self,values:list):
        query = f"""
            INSERT INTO ORDERS( "ITEM_NAME", "PRICE", "COUNT")
            VALUES(%s, %s, %s);"""    
        self.snowflake_connection.cursor().execute(query, values)

if __name__ == '__main__':
    #cost = Costs()
    #df = cost.get_costs()
    #print(df)
    order = Orders()
    data = order.get_ord_name()
    for i in range(len(data)):
        data[i] = str(data[i]).replace('(','')
        data[i] = str(data[i]).replace(')','')
        data[i] = str(data[i]).replace(',','')
    data_row = order.query_row(data[i])
    print(data_row)
