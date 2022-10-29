# import packages
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
plt.style.use('seaborn')

# show the title
st.title('Effects on math achievement.')
df = pd.read_csv('Maths.csv')

# create a parents' education filter 
st.subheader('Effect of average parental education level on math achievement.')
edu_filter = st.slider('The average parental education level is:', 0.0, 4.0, 0.0)
st.write(df.avedu.value_counts())

# filter data by avedu
df = df[df.avedu >= edu_filter]
fig, ax = plt.subplots(figsize=(10, 5))
df.groupby('avedu')['avegrade'].mean().plot.line(ax=ax, ylabel='avegrade')
st.pyplot(fig)

# create a radio button(alcohol filter)
st.subheader('Pie chart about alcohol consumption of student.')
alcohol_filter = st.radio(
    "Choose the time",
    ('Workday', 'Weekend'))

if alcohol_filter == 'Workday':   
    fig, ax = plt.subplots(figsize=(10,6))
    df.Dalc.value_counts(normalize=True).plot.pie(ax=ax, title='Workday alcohol consumption of student\n--from [1:very low] to [5:very high]', autopct='%.2f%%')
    st.pyplot(fig)
else:
    fig, ax = plt.subplots(figsize=(10,6))
    df.Walc.value_counts(normalize=True).plot.pie(ax=ax, title='Weekend alcohol consumption of student\n--from [1:very low] to [5:very high]', autopct='%.2f%%')
    st.pyplot(fig)

# willing to take higher education on academic performance
st.subheader('The impact of willing to take higher education on math achievement.')
fig, ax = plt.subplots(figsize=(10,6))
df.groupby('higher')['avegrade'].mean().plot.bar(ax=ax, ylabel='avegrade')
st.pyplot(fig)
