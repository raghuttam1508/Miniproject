# online-kyc

In this project we have made a web app which checks the validity of aadhar cards and pan cards. The user is first asked to enter his identity documents. After that the machine learning model classifies whether it is an aadhar card or a pan card. If it is detected as an Aadhar card, then its uid is taken and matched with the dummy Aadhar card data in the xlsl file. If the data matches, it is classified as a valid aadhar card. Similarly for pan card, its uid is matched with the dummy pan card data in the xlsl file, if it matches, it is classified as a valid pan card.
The ml model was trained using transfer learning on the vgg16 model. The dataset consisted of 30 images of aadhar cards and 30 images of pan cards.
The web app was completely made in python using the streamlit framework.



