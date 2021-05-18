from io import StringIO
from altair.vegalite.v4.api import Chart
from altair.vegalite.v4.schema.channels import Tooltip
from pandas.core.frame import DataFrame
import streamlit as st
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from plotly import graph_objs as go
import altair as alt
import os
import string

from streamlit.uploaded_file_manager import UploadedFile
  
sets = pd.read_excel("adharr.xlsx")

# Add a selectbox to the sidebar:
st.sidebar.header('Navigation')
rad = st.sidebar.radio('Select Your Domain: ',['Home', 'Consumer Desk','Company Desk','About us'])

if rad == 'Home':
    st.title("WELCOME TO THE RESUME OF YOUR PRODUCT")
    st.markdown(""" 
    # Our Product: 
    ### **Welcome to the first and the only quality asuarance website, where we provide you with the CV of the prodduct you bought. So hop on to the customer panel in the sidebar now!** <br> 
    ### **As we are still in ecperimental stage, we only have a few items in our database. So, be patient, we'll pick each and everyone UP!**
    ### **We intend to develop a prototype for a system where a consumer can ensure the product they are buying are Original to the manufacturer, matches the same level of claimed purity and also tracking the adulteration in the constituents of the product.**
    """,True)
    st.image("rebrand.jpg",caption='The future is Here',use_column_width=True)

if rad == 'Consumer Desk':
    st.title("CONSUMER DESK")   
    st.markdown(""" 
    ### Welcome to our Lobby! <br>

    """,True)
    st.write("""
            ## **ENTER YOUR PRODUCT ID/BARCODE NUMBER**
            # """)
    enterID = st.text_input('Input')
    u_submit = st.button("Submit")
    #if u_submit:
    #connection    
    #add code to check from database and printing the row. 
    
if rad == 'Company Desk':
    st.title("CLIENT DESK") 
    st.markdown(""" 
    ### Welcome to our Lobby! <br>
    """,True)
    client_c = st.text_input('USERNAME OR CLIENT ID')
    client_p = st.text_input('PASSWORD',type='password',)
    client_sub = st.button('Login')
    
    if client_sub and client_c == '123' and client_p == '123':
       
        #Add code for connecting DB for LOGIN window
        #st.header('**Our Data Sets**')
        #st.table(sets) 
            #graphs = st.sidebar.selectbox("What kind of visualisations?",['Future Quaotations','Market Demand VS Supply'], index=0) 
        layout = go.Layout(
            xaxis = dict(range=[0,16.000]),
            yaxis = dict(range=[0,2100.000])
        )
        fig = go.Figure(data=go.Scatter(x = sets['UID'], y = sets['NAME'],mode='markers' ),layout = layout)
        st.plotly_chart(fig)

        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.figure(figsize = (10,5))
        plt.scatter(sets['UID'],sets['NAME'])
        plt.ylim(0)
        plt.ylabel('NAME')
        plt.xlabel('UID')
        plt.tight_layout()
        st.pyplot()

    elif client_sub and client_c == '' or client_p == '':  
         st.error('No Credentials!')
    
    elif client_sub and client_c != '123' or client_p != '123':
        st.error('Wrong Credentials')

if rad == 'About us': 

    st.markdown('''
    # **WE ARE HIRING!!!!** :sunglasses:
    ''',True) 
    st.title('TEAM MEMBERS')
    st.write('''
    ### 1. Bhavya Hingorani      (9)
    ### 2. Rohan Padhye         (29)
    ### 3. Raghuttam Parvatikar (34)
    ''')
    st.markdown('''
    ## **Project Objectives**
    ''')

#st.file_uploader('Dataset')
#st.line_chart(data)
#st.area_chart(data)
#st.bar_chart(data)
#plt.scatter(data['a'], data['b'])
#st.pyplot()
#chart = alt.Chart(data).mark_circle().encode(
#    x = 'a', y = 'b', tooltip = ['a','b']
#)

#st.altair_chart(chart,use_container_width=True)

##st.graphviz_chart("""
#digraph{
#   a->b
#  b->c
# c->d
    #d->a
    #}
#""")

##st.map()

#st.button('Click here')
