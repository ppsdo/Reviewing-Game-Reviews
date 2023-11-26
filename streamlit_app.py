import streamlit as st
import pandas as pd
import seaborn as sns

df = pd.read_csv("review_scores.csv")
df_valid_scores = df[df['score']!=-1]
games_list_df = df_valid_scores['video title']
# df_valid_scores

tab1, tab2 = st.tabs(["📊 Statistics", "📼 Game Review List"])

metrics_container = st.container()
score_mean = df_valid_scores['score'].mean()
score_count = df_valid_scores.shape[0]

col1, col2, col3 = st.columns([10, 10, 10])

with metrics_container:
    with col1:
        metric_score_mean = st.metric("Average Review Score", round(score_mean, 2))

    with col2:
        metric_score_count = st.metric("Number of Reviews", score_count)

    with col3:
        st.write("inside right metrics")

# chart



# with left_column:
#     metric_score_mean = st.metric("Average Review Score", round(score_mean, 2))
#     metric__score_count = st.metric("Number of Reviews", score_count)

# # Or even better, call Streamlit functions inside a "with" block:
# with right_column:
#     chosen = st.radio(
#         'Sorting hat',
#         ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#     st.write(f"You are in {chosen} house!")

