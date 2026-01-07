import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns 
import streamlit as st


def main():
    st.title("This is my first site ")
    st.sidebar.title("upload your file")

    uploaded_file = st.sidebar.file_uploader("upload your own file", type= ['csv', 'xlsx'])

    if uploaded_file is not None:
        try :
            if uploaded_file.name.endswith('.csv'):
                data = pd.read_csv(uploaded_file)
            else :
                data = pd.read_excel(uploaded_file)

            st.sidebar.success("file uploaded succesfully")

            st.subheader("data overview")
            st.dataframe(data.head())

            st.subheader("Basic Information of the data")
            st.write("shape of the data", data.shape)
            st.write("columns in my data", data.columns)
            st.write("missing value", data.isnull().sum())

            st.subheader("i will show you stats of the data")
            st.write(data.describe())
        except Exception as e :
            print("it is not working ",e)
    else :
        pass



if __name__ == "__main__":
    main()

    

