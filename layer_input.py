import streamlit as st
import streamlit_authenticator as stauth
from connector import Database
from testcode import Orders

class LayerInput(Database):
    def __init__(self):
        self.ord = Orders()
        self.ord_name = self.ord.get_ord_name()
        option = st.selectbox('Information of:',options=self.ord_name)
        st.write(option)
        new_option = str(option)
        new_option.replace(',','')
        new_option.replace('(','')
        new_option.replace(')','')
        st.write(new_option)
        row = self.ord.query_row(new_option)
        st.write(row)

if __name__ == '__main__':
    layer = LayerInput()
        