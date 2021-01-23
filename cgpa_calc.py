import streamlit as st
from PIL import Image

logo = Image.open("bmsce.png")
st.image(logo,width=200)
st.title("BMSCE CGPA Calculator")

try:
    num_sub = int(st.text_input("Number of subjects(Excluding non-credit subjects): "))
except:
    pass
    # st.error("Invalid input! Try again!")
# num_sub = int(input("Enter the number of subjects(Excluding non-credit subjects): "))
# print()

credits = []
cie = []
see = []
total = []
earned = []
earned_sum = 0
credits_sum = 0
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
                credits.append(int(placeholder1.text_input("Number of credits for subject {}: ".format(i+1))))
            except:
                pass
                # placeholder.error("Invalid input! Try again!")
        with placeholder2.beta_container():
            try:
                cie.append(int(placeholder2.text_input("CIE marks in subject {}: ".format(i+1))))
            except:
                pass
                # placeholder.error("Invalid input! Try again!")
        with placeholder3.beta_container():
            try:
                see.append(int(placeholder3.text_input("SEE marks in subject {}: ".format(i+1))))
            except:
                pass
                # placeholder.error("Invalid input! Try again!")
        # credits.append(int(input("Enter the number of credits for subject {}: ".format(i))))
        # cie.append(double(input("Enter the CIE marks in subject {}: ".format(i))))
        # see.append(double(input("Enter the SEE marks in subject {}: ".format(i))))
        # print()
        total.append(round(cie[i]+(see[i]/(2.0))))
        if(total[i]>=90):
            earned.append(10)
        elif(total[i]>=80):
            earned.append(9)
        elif(total[i]>=70):
            earned.append(8)
        elif(total[i]>=60):
            earned.append(7)
        elif(total[i]>=50):
            earned.append(6)
        elif(total[i]>=40):
            earned.append(5)
        else:
            earned.append(0)
        earned_sum += (earned[i]*credits[i])
        credits_sum += (credits[i])
except:
    pass
try:
    if(len(credits)==num_sub):
        calc = st.button("Calculate CGPA")
        if(calc):
            cgpa = earned_sum / (credits_sum*1.0)
            st.title("Your CGPA is %.3f"%(cgpa))
except:
    pass
# print("Your CGPA is {}".format(cgpa))
