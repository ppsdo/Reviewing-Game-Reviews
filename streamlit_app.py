import streamlit as st
import pandas as pd

df = pd.read_csv("final_datasheet.csv") # (video id, title, normalized title, score, likes, dislikes, rating, viewCount, result, published at)
df = df[df['score']!=-1]
df["approval rating"] = df["likes"] / (df["likes"] + df["dislikes"])
games_list_df = df['title']

tab1, tab2 = st.tabs(["📊 Statistics", "📼 Game Review List"])

with tab1:
    metrics_container = st.container()
    score_mean = df['score'].mean()
    score_count = df.shape[0]

    col1, col2, col3 = st.columns([10, 10, 10])

    with metrics_container:
        with col1:
            metric_score_mean = st.metric("Average Review Score", round(score_mean, 2))

        with col2:
            metric_score_count = st.metric("Number of Reviews", score_count)

        with col3:
            res = df['score'].sub(df['approval rating']).pow(2).sum()
            tot = df['score'].sub(df['score'].mean()).pow(2).sum()
            r2 = 1 - res/tot
            metric_correlation = st.metric("R$^\\text{2}$", round(r2, 2))

    # chart
    st.scatter_chart(data=df[["score", "approval rating"]], x="score", y="approval rating")

with tab2:
    games_list_df
    # df[["score", "approval rating"]]

