
import streamlit as st
import instaloader
import json
import os

st.set_page_config(page_title="מנתח עוקבים באינסטגרם", layout="centered")
st.title("🔍 ניתוח עוקבים באינסטגרם")

username = st.text_input("שם משתמש באינסטגרם")
password = st.text_input("סיסמה", type="password")

if st.button("נתח את הפרופיל"):
    with st.spinner("מתחבר לאינסטגרם..."):
        try:
            L = instaloader.Instaloader()
            L.login(username, password)
            profile = instaloader.Profile.from_username(L.context, username)

            # קבלת העוקבים והעוקבים אחריהם
            followers = set([f.username for f in profile.get_followers()])
            followees = set([f.username for f in profile.get_followees()])

            # שמירת עוקבים לקובץ השוואה עתידי
            os.makedirs("user_data", exist_ok=True)
            path = f"user_data/{username}_followers.json"
            old_followers = set()
            if os.path.exists(path):
                with open(path, "r") as f:
                    old_followers = set(json.load(f))
                lost_followers = old_followers - followers
                st.warning(f"😥 איבדת {len(lost_followers)} עוקבים:")
                st.write(lost_followers)

            with open(path, "w") as f:
                json.dump(list(followers), f)

            # ניתוח הדדי/לא הדדי
            not_following_back = followees - followers
            fans = followers - followees
            mutual = followers & followees

            st.success("הניתוח הושלם ✅")
            st.subheader("👥 הדדיים:")
            st.write(mutual)

            st.subheader("🚫 את עוקבת – הם לא עוקבים חזרה:")
            st.write(not_following_back)

            st.subheader("🙋‍♀️ הם עוקבים – ואת לא:")
            st.write(fans)

        except Exception as e:
            st.error(f"שגיאה: {e}")
