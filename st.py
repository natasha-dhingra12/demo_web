import streamlit as st
import pandas as pd
# st.title("Welcome to mywebsite")
# st.header("python")
# st.subheader("java")
# st.markdown("My name is Natasha")
# st.code("""for i in range(1,5):
#     print("hi") """)
# df=pd.read_csv("Orders.csv")
# st.dataframe(df)

name=st.text_input("Enter your name:")
father_name=st.text_input("Enter father's name:")
address=st.text_area("enter ur address:")
class1=st.selectbox("enter your class",(1,2,3,4,5,6))
button=st.button("Done")
if button:
    st.markdown(f""" 
        Name:{name}
        Father name:{father_name}
        address:{address}
        class:{class1}

""")