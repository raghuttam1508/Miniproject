from altair.vegalite.v4.api import Chart
from altair.vegalite.v4.schema.channels import Tooltip
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

# Add a selectbox to the sidebar:
st.sidebar.header('Your place or mine?')
rad = st.sidebar.radio('Select Your Domain: ',['Home', 'Customer Desk','Client Desk','About us'])

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
    ### **New to our Page?, no worries Register by clicking Sign up!** <br> <br>    
    """,True)
    reg = st.button('Sign up')

    if reg:
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

if rad == 'Client Desk':
    st.title("CLIENT DESK") 
    st.markdown(""" 
    ### Welcome to our Lobby! <br>

    """,True)
    client_c = st.text_input('USERNAME OR CLIENT ID')
    client_p = st.text_input('PASSWORD',type='password')
    client_sub = st.button('Login')

    if client_sub:
        st.header("Upload the data for analysis.")
        csv = st.file_uploader('Datasets')


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