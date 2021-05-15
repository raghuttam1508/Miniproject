from io import StringIO
from altair.vegalite.v4.api import Chart
from altair.vegalite.v4.schema.channels import Tooltip
from pandas.core.frame import DataFrame
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
import os
import string

from streamlit.uploaded_file_manager import UploadedFile

#def xl_key(kee, database):
    #if database == 'Product Sets':
    #    try :
    #        product_values = set.loc[kee]
    #    except KeyError:
    #        return None,None

    #    nm = product_values['Name']
    #    p_id = product_values['ID']
    #    return nm, p_id


# Add a selectbox to the sidebar:
st.sidebar.header('Your place or mine?')
rad = st.sidebar.radio('Select Your Domain: ',['Home', 'Customer Desk','Client Desk','New Customer?','About us'])

if rad == 'Home':
    st.title("WELCOME TO THE RESUME OF YOUR PRODUCT")
    st.header("You are at home!")
    st.write(""" 
    # Our Product: 
    Yap yap lines
    """)
    st.image("MacW.jpg",caption='The future is Here',use_column_width=True)

if rad == 'Customer Desk':
    st.title("CUSTOMER DESK")   
    st.markdown(""" 
    ### Welcome to our Lobby! <br>

    """,True)
    user_c = st.text_input('USERNAME or CUSTOMER ID')
    user_p = st.text_input('PASSWORD',type = 'password')
    sub = st.button('Login')
    st.markdown("""
    ### **New to our Page?, no worries Register by clicking New User!** <br> <br>    
    """,True)    

    if sub:
        if user_c == '123'and user_p == '123':
            st.write("""
            ## **ENTER YOUR PRODUCT ID/BARCODE NUMBER**
            # """)
            enter_id,submit = st.beta_columns([3,1])
            enterID = enter_id.text_input('Input')
            u_submit = submit.button("Submit")
            #add code to check from database and printing the row
            
        else:
            st.error('Wrong Credentials!!')  

if rad == 'New Customer?':
        st.title('New User')
        first,last = st.beta_columns(2)
        Fname = first.text_input('FIRST NAME')
        Lname = last.text_input('LAST NAME')
        st.write("""
        ### AGE:
        """)
        age = st.slider('Age', min_value= 14)
        address = st.text_area('ADDRESS:', height=14, max_chars= 50)
        id = st.text_input('Valid ID number:')
        first_1,last_1 = st.beta_columns([2.5,1])
        email = first_1.text_input('Valid Email ID')
        nu = last_1.text_input('Phone Number')
        new_user_sub_button = st.button('Submit')
        # Add code linking to database, adding users
        
if rad == 'Client Desk':
    st.title("CLIENT DESK") 
    st.markdown(""" 
    ### Welcome to our Lobby! <br>

    """,True)
    client_c = st.text_input('USERNAME OR CLIENT ID')
    client_p = st.text_input('PASSWORD',type='password')
    client_sub = st.button('Login')

    if client_sub:
        if client_c == '123' and client_p == '123':
            sets = pd.read_excel("adharr.xlsx", index_col="UID")
            a1,a2 = st.beta_columns(2)
            a1.subheader("Data")
            a1.write(sets)
        else:
            st.error('Wrong Credentials!')


if rad == 'About us':   
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
