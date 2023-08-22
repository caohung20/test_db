import streamlit as st
from layer import Layer
from layer_input import LayerInput

tab1, tab2 = st.tabs([ "Input Layer","Visual Layer",])
with tab1:
    Layer()
with tab2:
    LayerInput()