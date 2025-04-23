# Import python packages
import streamlit as st
#from snowflake.snowpark.context import get_active_session
from sklearn.feature_extraction.text import TfidfVectorizer
import plotly.express as px
from sklearn.cluster import KMeans, HDBSCAN
from sklearn.feature_extraction import text
import sklearn
# Write directly to the app
st.title("Dynamic Text Clustering")
import pandas as pd
import numpy as np
import re
from openai import OpenAI
from config import openaikey

# Replace with your OpenAI API key
prompt = """I have a text clustering output from European project with popular terms and frequencies below, give me the Cluster name or topic in one sentence with less than 10 words, don't include double quotes or The topic is.
         """

client = OpenAI(
    # This is the default and can be omitted
    api_key=openaikey
)

# Get the current credentials
#session = get_active_session()

# Load a English model and create the nlp object
my_stop_words = text.ENGLISH_STOP_WORDS

#load data
#df = session.table('')
df = pd.read_csv("eu_results.csv")
df = df[["Project description","Funding area","Project country(ies)","Total project budget","Coordinators","EU Budget MFF heading"]]
#df = df.to_pandas()

#ngram_range = st.slider('Select n-gram', 1, 3, 1)

#define vectorizer parameters
vectorizer = TfidfVectorizer(ngram_range=(1,1), stop_words= list(my_stop_words))

# Sidebar for user input filters
st.sidebar.header('Filter Options')

# Support Type filter
type_options = df['EU Budget MFF heading'].unique().tolist()
selected_type = st.sidebar.multiselect('Select EU Budget MFF heading', options=type_options, default=type_options)

# Get the minimum and maximum values of the 'Total project budget' column
min_budget = df['Total project budget'].min()
max_budget = df['Total project budget'].max()

# Add a Streamlit slider for selecting a range within the budget
budget_range = st.slider(
    'Select the Total Project Budget range:',
    min_value=int(min_budget),
    max_value=int(max_budget),
    value=(int(min_budget), int(max_budget))
)

# Apply filters
filtered_df = df[df['EU Budget MFF heading'].isin(selected_type) & (df['Total project budget'] >= budget_range[0]) & (df['Total project budget'] <= budget_range[1])]

df = filtered_df

# Generate matrix of word vectors
#tfidf_matrix = vectorizer.fit_transform(df['Ticket Description'])
tfidf_matrix = vectorizer.fit_transform(df['Project description'])

#model = KMeans(num_clusters, random_state=123)
# User input for n-gram range
#cluster_size = st.slider('Select minimum cluster size', 20, 100, 20)
cluster_size = 20
model = HDBSCAN(min_cluster_size=cluster_size)

model.fit(tfidf_matrix)

clusters=model.labels_
num_clusters = max(clusters)+1
st.text(num_clusters)

df['cluster'] = pd.DataFrame(clusters)

#assign colors to cluster
colors = px.colors.named_colorscales()

def display_topic_cluster(n):
    
    df_text_bow = tfidf_matrix.toarray()
    bow_df = pd.DataFrame(df_text_bow)

    # Map the column names to vocabulary 
    bow_df.columns = vectorizer.get_feature_names_out()
    bow_df['cluster'] = pd.DataFrame(clusters)

    word_freq = pd.DataFrame(bow_df[bow_df.cluster == n].sum().sort_values(ascending = False))
    word_freq.reset_index(level=0, inplace=True)
    word_freq.columns=['word','frequency']

    data_text = word_freq[0:30].to_csv()

    # chat_completion = client.chat.completions.create(
    # messages=[
    #     {
    #         "role": "user",
    #         "content": prompt+data_text,
    #     }
    # ],
    # model="gpt-4",
    # )

    # topic = chat_completion.choices[0].message.content
    # try:
    #     topic = eval(topic)
    # except:
    #     print(topic)
    topic = "Cluster"

    
    if n>0:
        word_freq.drop(index=[0],inplace=True)
        
    fig = px.treemap(word_freq[0:30], path=[px.Constant(topic),'word'], values='frequency',
                color='frequency', hover_data=['frequency'],
                color_continuous_scale= colors[n])
    return fig, topic[1]

for i in range(0,num_clusters):
    fig, recommendation = display_topic_cluster(i)
    st.plotly_chart(fig)
