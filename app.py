import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load cleaned dataset
df = pd.read_csv("metadata_clean.csv")

# Title and description
st.title("CORD-19 Data Explorer")
st.write("Explore COVID-19 research papers metadata")

# Interactive year range slider
min_year = int(df["year"].min())
max_year = int(df["year"].max())
year_range = st.slider("Select Year Range", min_year, max_year, (2020, 2021))

# Filter dataset
filtered_df = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

# Show sample of data
st.subheader("Sample Data")
st.write(filtered_df.head())

# Publications per year
st.subheader("Publications per Year")
papers_per_year = filtered_df["year"].value_counts().sort_index()
fig, ax = plt.subplots()
papers_per_year.plot(kind="bar", ax=ax, color="skyblue", edgecolor="black")
ax.set_title("Number of Publications per Year")
st.pyplot(fig)

# Top Journals
st.subheader("Top Journals")
top_journals = filtered_df["journal"].value_counts().head(10)
fig, ax = plt.subplots()
top_journals.plot(kind="bar", ax=ax, color="lightgreen", edgecolor="black")
ax.set_title("Top Journals Publishing COVID-19 Research")
st.pyplot(fig)

# Word Cloud of Titles
st.subheader("Word Cloud of Titles")
titles = " ".join(filtered_df["title"].dropna())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles)
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)