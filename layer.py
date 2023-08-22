import streamlit as st
from testcode import Orders,OrderItems
import pandas as pd


class Layer():
    def __init__(self) -> None:
        self.order = Orders()
        self.order_items = OrderItems()
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
            self.order.post_entry(self.blank)
            list_of_dict = self.edited_df.to_dict(orient='list')
            st.write(list_of_dict)
            self.__update_order_items__(list_of_dict)

    def __update_order_items__(self, list_of_input):
        for i in range(len(list_of_input["ITEM_NAME"])):
                list_input = []
                list_input.append(list_of_input["ITEM_NAME"][i])
                list_input.append(list_of_input["PRICE"][i])
                list_input.append(list_of_input["COUNT"][i])
                self.order_items.post_entry(list_input)    
    
if __name__ == '__main__':
    layer = Layer()