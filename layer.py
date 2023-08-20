import streamlit as st

from testcode import Orders,OrderItems
import pandas as pd
from styles import Styles
from users import Users
from logs import Logs
import datetime as dt
import pytz
from connector import Database

class Layer():
    def __init__(self) -> None:
        
        self.df = pd.DataFrame(
            [
                {"ITEM_NAME": "", "PRICE":"", "COUNT":""},         
            ]
        )
        self.blank = st.text_input('Name of order')
        self.edited_df = st.data_editor(self.df,width=500, height=500, 
                                        use_container_width=True, num_rows="dynamic")
        self.save_button = st.button('Save')
        if self.save_button:
            st.write('already save')
            st.write(f"{self.blank}")
            self.__updateorder__()
            self.data_to_insert = self.edited_df.loc[0]["PRICE"]
            st.write(f"{self.data_to_insert}")
            
            self.__update_order_items__()
            
    def __updateorder__(self): 
        order = Orders()
        order.post_entry(self.blank)

    def __update_order_items__(self):
        order_items = OrderItems()
        no_row = self.edited_df.shape[0]
        for i in range(no_row):
            cell0 = self.edited_df.loc[i]["ITEM_NAME"]
            cell1 = int(self.edited_df.loc[i]["PRICE"])
            cell2 = int(self.edited_df.loc[i]["COUNT"])
            l1st = [cell0, cell1, cell2]
            print(l1st)
            order_items.post_entry(l1st)


if __name__ == '__main__':
    layer = Layer()