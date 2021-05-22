
from altair.vegalite.v4.api import Chart
from altair.vegalite.v4.schema.channels import Tooltip
from altair.vegalite.v4.schema.core import LayoutAlign
from pandas.core.frame import DataFrame
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import csv
from plotly import graph_objs as go
import altair as alt
import mysql.connector
from sklearn.linear_model import LinearRegression
from streamlit.uploaded_file_manager import UploadedFile
  


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
    
    if u_submit:
        mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password = "raghu1234",
        database="miniProject"
        )
        query = "SELECT Product_info.Name,Product_info.M_location,Batch.EXP,Batch.MFG,Company.Name as Company FROM Product INNER JOIN Batch ON Batch.Batch_id=Product.Batch_id INNER JOIN Product_info ON Product_info.info_id=Batch.info_id INNER JOIN Company ON Company.C_id=Product_info.C_id WHERE Product.Product_id =%s;"
        content = "SELECT Content.Content,Content.Source FROM Product INNER JOIN Batch ON Batch.Batch_id=Product.Batch_id INNER JOIN Product_info ON Product_info.info_id=Batch.info_id INNER JOIN Content ON Content.Cinfo_id=Product_info.C_id WHERE Product.Product_id=%s;"
        if enterID == '':
            st.error("NO ID ENTERED")
        else:
            try: 
                mycursor = mydb.cursor()
                #1st query fired
                mycursor.execute(query,[(enterID)])
                info = mycursor.fetchall()
                
                #2nd query fired
                mycursor.execute(content,[(enterID)])
                
                content=mycursor.fetchall()
                if not info :
                    st.error("NO DATA")
                    exit()
                st.header("CONTENT")
                st.table(info)  
                st.write(content)
                
                for x in info:
                    print (x)
                print()
                for x in content:
                    print(x)
                
            except: print("ERR : NO DATA FOUND")
        
    #add code to check from database and printing the row. 
    
if rad == 'Company Desk':
    st.title("CLIENT DESK") 
    st.markdown(""" 
    ### Welcome to our Lobby! <br>
    """,True)
    client_c = st.text_input('USERNAME OR CLIENT ID')
    client_p = st.text_input('PASSWORD',type='password',)
    client_sub = st.button('Login')

    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password = "raghu1234",
    database="miniProject"
    )
    query = "SELECT * FROM Login WHERE UserName =%s AND Password =%s"
    try: 
        mycursor = mydb.cursor()
        mycursor.execute(query,[(client_c),(client_p)])
        myresult = mycursor.fetchall()
    except: print()
    

    PSQ = []
    demand = []
    netProfit = []
    PIN = []
    time = []
    for i in range(1,20):
        time.append(i)
    
    rad_pred = st.sidebar.radio('Which product data do you want :',["1. TATA tea","2. Lays","3. Mountain dew","4. Hide and seek"])
    if rad_pred == '1. TATA tea':
        path_1 = 'C:\\Users\\raghu\\OneDrive\\Desktop\\Miniproject\\TATA tea.csv'
        with open(path_1) as file :
            reader = csv.reader(file)
            count = 0
            for row in reader:
                if(count > 0):
                    PSQ.append(int(int(float(row[0]))/1000))
                    demand.append(int(int(row[1])/1000))
                    netProfit.append(int(int(float(row[2]))/1000))
                    PIN.append(int(int(row[3])/1000))
                count += 1

        # Training prediction model
        lr = LinearRegression()
        lr.fit(np.array(demand).reshape(-1,1), np.array(PSQ).reshape(-1,1))

        #Prediction
        st.sidebar.header("Next marketing budget : ")
        v = st.sidebar.number_input('Budget')
        val = int(float(v))

        val = np.array(val).reshape(1,-1)
        #pred = lr.predict(val)
        if val == 0:
            pred = 0
        else:
            pred = lr.predict(val)
        st.sidebar.write(pred)
    
    if rad_pred == '2. Lays':
        path_2 = 'C:\\Users\\raghu\\OneDrive\\Desktop\\Miniproject\\Lays.csv'
        with open(path_2) as file :
            reader = csv.reader(file)
            count = 0
            for row in reader:
                if(count > 0):
                    PSQ.append(int(int(float(row[0]))/1000))
                    demand.append(int(int(row[1])/1000))
                    netProfit.append(int(int(float(row[2]))/1000))
                    PIN.append(int(int(row[3])/1000))
                count += 1

        # Training prediction model
        lr = LinearRegression()
        lr.fit(np.array(demand).reshape(-1,1), np.array(PSQ).reshape(-1,1))

        #Prediction
        st.sidebar.header("Next marketing budget : ")
        v = st.sidebar.number_input('Budget')
        val = int(float(v))

        val = np.array(val).reshape(1,-1)
        #pred = lr.predict(val)
        if val == 0:
            pred = 0
        else:
            pred = lr.predict(val)
        st.sidebar.write(pred)
    
    if rad_pred == '3. Mountain dew':
        path_3 = 'C:\\Users\\raghu\\OneDrive\\Desktop\\Miniproject\\Mountain dew.csv'
        with open(path_3) as file :
            reader = csv.reader(file)
            count = 0
            for row in reader:
                if(count > 0):
                    PSQ.append(int(int(float(row[0]))/1000))
                    demand.append(int(int(row[1])/1000))
                    netProfit.append(int(int(float(row[2]))/1000))
                    PIN.append(int(int(row[3])/1000))
                count += 1

        # Training prediction model
        lr = LinearRegression()
        lr.fit(np.array(demand).reshape(-1,1), np.array(PSQ).reshape(-1,1))

        #Prediction
        st.sidebar.header("Next marketing budget : ")
        v = st.sidebar.number_input('Budget')
        val = int(float(v))

        val = np.array(val).reshape(1,-1)
        #pred = lr.predict(val)
        if val == 0:
            pred = 0
        else:
            pred = lr.predict(val)
        st.sidebar.write(pred)

    if rad_pred == '4. Hide and seek':
        path_4 = 'C:\\Users\\raghu\\OneDrive\\Desktop\\Miniproject\\Hide and seek.csv'
        with open(path_4) as file :
            reader = csv.reader(file)
            count = 0
            for row in reader:
                if(count > 0):
                    PSQ.append(int(int(float(row[0]))/1000))
                    demand.append(int(int(row[1])/1000))
                    netProfit.append(int(int(float(row[2]))/1000))
                    PIN.append(int(int(row[3])/1000))
                count += 1  

        # Training prediction model
        lr = LinearRegression()
        lr.fit(np.array(demand).reshape(-1,1), np.array(PSQ).reshape(-1,1))

        #Prediction
        st.sidebar.header("Next marketing budget : ")
        v = st.sidebar.number_input('Budget')
        val = int(float(v))

        val = np.array(val).reshape(1,-1)
        #pred = lr.predict(val)
        if val == 0:
            pred = 0
        else:
            pred = lr.predict(val)
        st.sidebar.write(pred)
    
    if client_sub and myresult:
       
        #Add code for connecting DB for LOGIN window
        #st.header('**Our Data Sets**')
        #st.table(sets) 
            #graphs = st.sidebar.selectbox("What kind of visualisations?",['Future Quaotations','Market Demand VS Supply'], index=0) 
        
        #layout = go.Layout(
        #    xaxis  = dict(range = [0,2000000.000]),
        #    yaxis  = dict(range = [0,100]),
        #)
        #fig = go.Figure(path_1 = go.scatter(x = path_1["demand"], y = path_1['product sales quarterly'],mode = "marker"),layout = layout)
        #st.plotly_chart(fig)

        #Below this is the code to display graphs 
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.bar(demand, PSQ)
        plt.xlabel("Marketing budget in lakhs")
        plt.ylabel("Product sales per quarter")
        plt.tight_layout()
        st.pyplot()

        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.scatter(PSQ, netProfit)
        plt.xlabel("Product sales per quarter")
        plt.ylabel("Net profit")
        plt.tight_layout()
        st.pyplot()

        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.scatter(time, netProfit)
        plt.xlabel("Time in quarters")
        plt.ylabel("Net profit")
        plt.tight_layout()
        st.pyplot()

        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.scatter(time, PIN)
        plt.xlabel("Time in quarters")
        plt.ylabel("Losses in profit")
        plt.tight_layout()
        st.pyplot()

    elif client_sub and client_c == '' or client_p == '':  
        st.error('No Credentials!')
    
    elif client_sub and not myresult:   
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
    ##
    ## **Project Objectives**
    ### 1. User Friendly sharp GUI
    ### 2. A well eshtablished Database
    ### 3. A reliable Prediction Module with Visual Representation of Data
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
