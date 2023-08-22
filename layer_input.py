import streamlit as st
from connector import Database
from testcode import Orders

class LayerInput(Database):
    def __init__(self):
        self.ord = Orders()
        self.ord_name = self.ord.get_ord_name()
        for i in range(len(self.ord_name)):
            self.ord_name[i] = str(self.ord_name[i]).replace('(','')
            self.ord_name[i] = str(self.ord_name[i]).replace(')','')
            self.ord_name[i] = str(self.ord_name[i]).replace(',','')
        option = st.selectbox('Information of:',options=self.ord_name)
        row = self.ord.query_row(option)
        st.write(row)

if __name__ == '__main__':
    layer = LayerInput()
        