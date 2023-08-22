import snowflake.connector
import pandas as pd
import yaml
import streamlit as st
import pytz
import datetime as dt

utc_timezone = pytz.timezone('UTC')
local_timezone = pytz.timezone('Asia/Ho_Chi_Minh')


class Database:
    def __init__(self):
        """Loads secrets.yml"""
        self.secrets = yaml.safe_load(open("assets/secrets.yml"))
        self.snowflake_connection = snowflake.connector.connect(
            account = self.secrets["database"]["account"],
            user = self.secrets["database"]["user"],
            password = self.secrets["database"]["password"],
            warehouse = self.secrets["database"]["warehouse"],
            database = self.secrets["database"]["database"],
            schema = self.secrets["database"]["schema"],
            client_session_keep_alive = "true")
        
    
    def query_columns(self, columns: list) -> str:
        """Returns columns for query"""
        columns_string = ""
        for column in columns:
            columns_string += f'"{column}", '
        columns_string = columns_string[:-2]
        return columns_string