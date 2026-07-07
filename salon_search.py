#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import streamlit as st
import plotly.express as px


# In[5]:


# merged.csvを読み込む
merged_df = pd.read_csv("merged.csv")


# In[8]:


# streamlitの部品設計
st.title("サロンサーチ")  # Changed Japanese closing parenthesis ）to regular )

# フィルタ設定
price_limit = st.slider("最低カット価格の上限", min_value=2000, max_value=85000, step=2000, value=6000)  # Changed Japanese comma ，to regular comma , and added missing closing parenthesis )
score_limit = st.slider("人気スコアの下限", min_value=0.0, max_value=35.0, step=2.0, value=5.0)


# In[9]:


filtered_df = merged_df[
       (merged_df['price'] <= price_limit)&
       (merged_df['pop_score'] >score_limit)
    ]


# In[12]:


fig = px.scatter(
       filtered_df,
       x='pop_score',
       y='price',
       hover_data=['name_salon', 'access','star', 'review'],  # Changed 'ster' to 'star'
       title='人気スコアと最低カット価格の散布図'
)  # Changed from Japanese closing parenthesis ）to ASCII closing parenthesis )
st.plotly_chart(fig)


# In[15]:


# Fixed typo: 'at' should be 'st'
selected_salon = st.selectbox('気になるサロンを選んで詳細を確認', filtered_df['name_salon'])

if selected_salon:
    # Fixed typo: 'swlected_salon' should be 'selected_salon'
    # Fixed bracket issue: added missing '[' at the beginning
    # Fixed column name: 'link_deteil' should be 'link_detail' (corrected spelling)
    url = filtered_df[filtered_df['name_salon'] == selected_salon]['link_detail'].values[0]
    # Fixed missing closing parenthesis and variable name 'uri' to 'url'
    # Fixed boolean value: 'true' should be 'True'
    st.markdown(f"[{selected_salon}のページへ移動]({url})", unsafe_allow_html=True)


# In[17]:


sort_key = st.selectbox(
    "ランキング基準を選んでください",
    ("ster", "pop_score", "review", "price", "seats")  # Added missing closing parenthesis
)
ascending = True if sort_key == "price" else False  # Changed 'true' to 'True' (proper Python boolea


# In[22]:


st.dataframe(ranking_df[["name_salon", "praice", "pop_score", "ster", "review", "seats", "access"]])


# # User
# hai

# In[23]:


# Fixed the unmatched parenthesis in the f-string and corrected the variable name typo
st.subheader(f"{sort_key} によるサロンランキング(上位10件)")
ranking_df = filtered_df.sort_values(by=sort_key, ascending=ascending).head(10)  # Changed 'filterd_df' to 'filtered_df'
# Fixed column name from "ster" to "star" - corrected the typo in column name
st.dataframe(ranking_df[["name_salon", "praice", "pop_score", "star", "review",
"seats", "access"]])


# In[ ]:




