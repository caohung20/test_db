import streamlit as st
import pandas as pd
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
        row2dict = {'ID':[],'NAME':[],'CREATED TIMESTAMP':[]}
        for i in range(len(row)):
            row2dict['ID'].append(row[i][0])
            row2dict['NAME'].append(row[i][1])
            row2dict['CREATED TIMESTAMP'].append(row[i][2])
        row2df = pd.DataFrame(row2dict)
        st.table(row2df)

if __name__ == '__main__':
    layer = LayerInput()

        