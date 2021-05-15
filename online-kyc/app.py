#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 14:07:05 2021

@author: shashwat
"""


import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd
import os 
import matplotlib.pyplot as plt
import cv2
from PIL import Image
import pytesseract as pt
import re

def main():
    
    
    def load_model():
        model = tf.keras.models.load_model("/Users/shashwat/adharpancard.model")
        return model
    
        
        
    
    def displayer(pattern_uid, pred, lis):
        a1,a2,a3 = st.beta_columns((2,2,2))
        a1.subheader("Card detected:")
        a1.write("{} ".format(pred))
        if pattern_uid:
            a2.subheader("Unique Number : ")
            a2.write(" {} ".format(pattern_uid))
        else:
            a2.subheader("Unique Number : ")
            a2.write("Not detected")
            a2.write("Please try again")
        if pred == "Pan Card" and lis[0] != None:
            a3.subheader("Details:")
            a3.write("Name: {}".format(lis[0]))
            a3.write("Father's Name : {}".format(lis[1]))
        elif pred == "Aadhar Card" and lis[0] != None:
            a3.subheader("Details:")
            a3.write("Name: {}".format(lis[0]))
            a3.write("Date of Birth : {}".format(lis[1]))
            a3.write("Gender : {}".format(lis[2]))
        else:
            a3.subheader("Details :")
            a3.write("Details not detected, please try again later.")
            a3.write("Authentication failed.")
            
        
        
    def xl_key(kee, database):
        if database == "pan":
            #st.write(pan)
            try :
                pan_values = pan.loc[kee]
            except KeyError:
                return None,None
            #st.write(pan_values)
            #st.write(pan_values["Name"])
            #st.write(pan_values["fathers_name"])
            nm = pan_values["Name"]
            fnm = pan_values["fathers_name"]
            return nm,fnm
        if database == "adhar":
            #st.write(adhar)
            try:
                adhar_values = adhar.loc[kee]
            except KeyError:
                return None,None,None
            nm = adhar_values["Name"]
            dob = adhar_values["dob"]
            gend = adhar_values["gender"]
            return nm,dob,gend
    
    
    def adhar_reader(img):
        img1 = img.resize((300,300))
        k1,k2,k3 = st.beta_columns((1,2,1))
        k2.image(img1)
        img = img.resize((500,500))
        #st.image(img)
        string = pt.image_to_string(img, config="--psm 1")
        #st.write(type(string))
        #st.write(string)
        uid_pattern = "\d... .... ...\d"
        try:
            pattern_uid = re.findall(uid_pattern,string)[0]
            lis = xl_key(pattern_uid, "adhar")
        except IndexError:
            pattern_uid = None
            lis = [None]
        #st.write("UID Number : ",pattern_uid )
        displayer(pattern_uid,"Aadhar Card", lis)
        
    def pan_reader(img):
        img1 = img.resize((300,300))
        k1,k2,k3 = st.beta_columns((1,2,1))
        k2.image(img1)
        img = img.resize((500,500))
        #st.image(img)
        string = pt.image_to_string(img, config="--psm 1")
        #st.write(type(string))
        #st.write(string)
        uid_pattern = "[A-Z|0-9][A-Z|0-9][A-Z|0-9][A-Z|0-9][A-Z|0-9][0-9][0-9][0-9][0-9][A-Z|0-9]"
        try:
            pattern_uid = re.findall(uid_pattern,string)[0]
            lis = xl_key(pattern_uid, "pan")
        except IndexError:
            pattern_uid = None
            lis = [None, None]
        #st.write("UID Number : ",pattern_uid)
        displayer(pattern_uid, "Pan Card",lis)
        
        
        
    
    def import_predict(img,model,pimage):
       #st.write(img.shape)
       img1 = np.expand_dims(img, axis=0)
       #st.write(img.shape)
       #pimage = pimage
       prediction = model.predict(img1)
       #st.write(prediction)
       if prediction[0][0] == 1:
           adhar_reader(pimage)
       else:
           pan_reader(pimage)


           
           
       
       
        
        
        
    
    st.title(" KYC Online Verification ")
    st.sidebar.title(" Choose Option  ")
    adhar = pd.read_excel("adharr.xlsx", index_col="UID")
    pan = pd.read_excel("pann-2.xlsx", index_col="uid")
    #pan.drop(labels="UID", inplace = True)
    if st.sidebar.checkbox("Upload the details ", key = "cb1"):
        l1,l2 = st.beta_columns((2,1))
        l1.subheader("You should upload your aadhar card and pan card for complete verification.")
        if st.checkbox("Upload your identification card "):
            file = st.file_uploader(label="Upload  ",type=["jpg","jpeg","cng"],key = "f1")
            if file:
                
                pimage = Image.open(file)
                #st.image(pi mage, width = 100)
                image = np.array(pimage)
                #st.write(image.shape)
                image= cv2.resize(image,(224,224))
                #st.write(image.shape)
                #image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
                #image = np.reshape(image,(110,110,1))
                #st.write(image.shape)
                model = load_model()
                import_predict(image, model, pimage)
                #st.write()
        
        if st.checkbox("Upload your identification card ", key = "cb2"):
            file = st.file_uploader(label="Upload  ",type=["jpg","jpeg","cng"], key = "f2")
            if file:
                pimage = Image.open(file)
                #st.image(pimage, width = 100)
                image = np.array(pimage)
                #st.write(image.shape)
                image= cv2.resize(image,(224,224))
                #st.write(image.shape)
                #image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
                #image = np.reshape(image,(110,110,1))
                #st.write(image.shape)
                model = load_model()
                import_predict(image, model, pimage)
                #st.write()
                
    if st.sidebar.checkbox("Database", key = "cb2"):
        
        a1,a2,a3 = st.beta_columns((1,2,1))
        a2.subheader("Adhar Data")
        a2.write(adhar)
        a2.subheader("Pan Data")
        a2.write(pan)
        
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

if __name__ == '__main__':
    main()
