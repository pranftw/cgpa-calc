# Author: Pranav Sastry
# Date Created: 23rd Jan 2021
# TODO: If you're from another college/university, fork this repo and modify the code according to your marking scheme

import streamlit as st
from PIL import Image
import pandas as pd

# Uni/College logo
logo = Image.open("bmsce.png")
st.image(logo,width=200)

st.title("BMSCE CGPA Calculator")
st.markdown("Created by **Pranav Sastry, CSE '23**")
st.subheader("Instructions")
st.markdown("**1. Select the number of subjects excluding the non-credit subjects.<br>2. Select the number of credits registered for.<br>3. Enter the CIE (Continuous Internal Evaluation) marks out of 50.<br>4. Enter the SEE (Semester End Examination) marks out of 100.**",unsafe_allow_html=True)

# Get the number of subjects in the semester
try:
    num_sub = int(st.selectbox("Number of Subjects: ",(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,
    18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50)))
except:
    pass
    # st.error("Invalid input! Try again!")


# credits - List containing the credits for the subjects
# cie - List containing the Internals marks
# see - List containing the Semester End Examination marks
# total - List containing the total marks of CIE and SEE
# earned - List containing the credits earned
# earned_sum - List containing the product of earned[i] and credits[i]
# credits_sum - List containing the total sum of credits

credits = []
cie = []
see = []
total = []
earned = []
earned_sum = 0
credits_sum = 0
cie_sum = 0;
see_sum = 0;
total_sum = 0;
grades = []
try:
    for i in range(0,num_sub):
        placeholder = st.empty()
        placeholder1 = st.empty()
        placeholder2 = st.empty()
        placeholder3 = st.empty()
        with placeholder.beta_container():
            try:
                placeholder.subheader("Details of Subject {}: ".format(i+1))
            except:
                pass
                # placeholder.error("Invalid input! Try again!")
        with placeholder1.beta_container():
            try:
                cr = int(placeholder1.selectbox("Number of credits for subject {}: ".format(i+1),(1,2,3,4,5,6,7,8,9,10)))
                credits.append(cr)
            except:
                pass
                # placeholder.error("Invalid input! Try again!")
        with placeholder2.beta_container():
            try:
                ci = int(placeholder2.text_input("CIE marks in subject {}: ".format(i+1)))
                cie.append(ci)
            except:
                pass
                # placeholder.error("Invalid input! Try again!")
        with placeholder3.beta_container():
            try:
                se = int(placeholder3.text_input("SEE marks in subject {}: ".format(i+1)))
                see.append(se)
            except:
                pass
                # placeholder.error("Invalid input! Try again!")
        to = round(cie[i]+(see[i]/(2.0)))
        cie_sum+=ci;
        see_sum+=se;
        total_sum+=to;
        total.append(to)
        if(total[i]>=90):
            earned.append(10)
            grades.append("S")
        elif(total[i]>=80):
            earned.append(9)
            grades.append("A")
        elif(total[i]>=70):
            earned.append(8)
            grades.append("B")
        elif(total[i]>=60):
            earned.append(7)
            grades.append("C")
        elif(total[i]>=50):
            earned.append(6)
            grades.append("D")
        elif(total[i]>=40):
            earned.append(5)
            grades.append("E")
        else:
            earned.append(0)
            grades.append("F")
        earned_sum += (earned[i]*credits[i])
        credits_sum += (credits[i])
except:
    pass
try:
    if(len(credits)==num_sub):
        st.subheader("")
        calc = st.button("Calculate CGPA")
        if(calc):
            cgpa = earned_sum / (credits_sum*1.0)
            st.title("Your CGPA is %.3f"%(cgpa))
            row_name = ["CIE","SEE","Grade","Total"]
            col_name = []
            tab_data = []
            row_data = []
            for i in range(0,num_sub):
                col_name.append("Subject {}".format(i+1))
                row_data.append(cie[i])
            row_data.append("{}/{}".format(cie_sum,(50*num_sub)))
            tab_data.append(row_data)
            row_data = []
            for i in range(0,num_sub):
                row_data.append(see[i])
            row_data.append("{}/{}".format(see_sum,(100*num_sub)))
            tab_data.append(row_data)
            row_data = []
            for i in range(0,num_sub):
                row_data.append(grades[i])
            row_data.append("-")
            tab_data.append(row_data)
            row_data = []
            for i in range(0,num_sub):
                row_data.append(total[i])
            row_data.append("{}/{}".format(total_sum,(100*num_sub)))
            tab_data.append(row_data)
            col_name.append("Total")
            df = pd.DataFrame(tab_data,row_name,col_name)
            st.subheader("Result Details")
            st.dataframe(df)
except:
    pass
