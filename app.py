import streamlit as st
import pandas as pd

# Load dataset with correct separator
df = pd.read_csv("career.csv", sep=",")
df.columns = df.columns.str.strip()


st.title("🎓 AI-Powered Career & Skills Advisor")
st.write("Get personalized career suggestions and pathways based on your skills and interests.")

# User input
skills = st.text_input("Enter your skills (comma-separated)")
interests = st.text_input("Enter your interests (comma-separated)")

if st.button("Find My Career Path"):
    if skills and interests:
        # Normalize user input
        skill_list = [s.strip().lower() for s in skills.split(",") if s.strip()]
        interest_list = [i.strip().lower() for i in interests.split(",") if i.strip()]

        # Matching: filter careers that match any skill AND any interest
        matched = df[
            df['skill'].str.lower().apply(lambda x: any(skill in x for skill in skill_list)) &
            df['interest'].str.lower().apply(lambda x: any(interest in x for interest in interest_list))
        ]

        if not matched.empty:
            career = matched.iloc[0]
            st.subheader(f"✨ Suggested Career: {career['career']}")
            st.write(f"**Required Skills:** {career['required_skills']}")
            st.write(f"**Learning Resources:** [Link]({career['resources']})")
        else:
            st.warning("No exact match found. Try different skills or interests.")
    else:
        st.error("Please enter both skills and interests.")
