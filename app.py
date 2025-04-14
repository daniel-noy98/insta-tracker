{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tqr\tx720\tqr\tx1440\tqr\tx2160\tqr\tx2880\tqr\tx3600\tqr\tx4320\tqr\tx5040\tqr\tx5760\tqr\tx6480\tqr\tx7200\tqr\tx7920\tqr\tx8640\pardirnatural\qr\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
import instaloader\
import json\
import os\
\
st.set_page_config(page_title="\uc0\u1502 \u1504 \u1514 \u1495  \u1506 \u1493 \u1511 \u1489 \u1497 \u1501  \u1489 \u1488 \u1497 \u1504 \u1505 \u1496 \u1490 \u1512 \u1501 ", layout="centered")\
st.title("\uc0\u55357 \u56589  \u1504 \u1497 \u1514 \u1493 \u1495  \u1506 \u1493 \u1511 \u1489 \u1497 \u1501  \u1489 \u1488 \u1497 \u1504 \u1505 \u1496 \u1490 \u1512 \u1501 ")\
\
username = st.text_input("\uc0\u1513 \u1501  \u1502 \u1513 \u1514 \u1502 \u1513  \u1489 \u1488 \u1497 \u1504 \u1505 \u1496 \u1490 \u1512 \u1501 ")\
password = st.text_input("\uc0\u1505 \u1497 \u1505 \u1502 \u1492 ", type="password")\
\
if st.button("\uc0\u1504 \u1514 \u1495  \u1488 \u1514  \u1492 \u1508 \u1512 \u1493 \u1508 \u1497 \u1500 "):\
    with st.spinner("\uc0\u1502 \u1514 \u1495 \u1489 \u1512  \u1500 \u1488 \u1497 \u1504 \u1505 \u1496 \u1490 \u1512 \u1501 ..."):\
        try:\
            L = instaloader.Instaloader()\
            L.login(username, password)\
            profile = instaloader.Profile.from_username(L.context, username)\
\
            # \uc0\u1511 \u1489 \u1500 \u1514  \u1492 \u1506 \u1493 \u1511 \u1489 \u1497 \u1501  \u1493 \u1492 \u1506 \u1493 \u1511 \u1489 \u1497 \u1501  \u1488 \u1495 \u1512 \u1497 \u1492 \u1501 \
            followers = set([f.username for f in profile.get_followers()])\
            followees = set([f.username for f in profile.get_followees()])\
\
            # \uc0\u1513 \u1502 \u1497 \u1512 \u1514  \u1506 \u1493 \u1511 \u1489 \u1497 \u1501  \u1500 \u1511 \u1493 \u1489 \u1509  \u1492 \u1513 \u1493 \u1493 \u1488 \u1492  \u1506 \u1514 \u1497 \u1491 \u1497 \
            path = f"user_data/\{username\}_followers.json"\
            old_followers = set()\
            if os.path.exists(path):\
                with open(path, "r") as f:\
                    old_followers = set(json.load(f))\
                lost_followers = old_followers - followers\
                st.warning(f"\uc0\u55357 \u56869  \u1488 \u1497 \u1489 \u1491 \u1514  \{len(lost_followers)\} \u1506 \u1493 \u1511 \u1489 \u1497 \u1501 :")\
                st.write(lost_followers)\
\
            with open(path, "w") as f:\
                json.dump(list(followers), f)\
\
            # \uc0\u1504 \u1497 \u1514 \u1493 \u1495  \u1492 \u1491 \u1491 \u1497 /\u1500 \u1488  \u1492 \u1491 \u1491 \u1497 \
            not_following_back = followees - followers\
            fans = followers - followees\
            mutual = followers & followees\
\
            st.success("\uc0\u1492 \u1504 \u1497 \u1514 \u1493 \u1495  \u1492 \u1493 \u1513 \u1500 \u1501  \u9989 ")\
            st.subheader("\uc0\u55357 \u56421  \u1492 \u1491 \u1491 \u1497 \u1497 \u1501 :")\
            st.write(mutual)\
\
            st.subheader("\uc0\u55357 \u57003  \u1488 \u1514  \u1506 \u1493 \u1511 \u1489 \u1514  \'96 \u1492 \u1501  \u1500 \u1488  \u1506 \u1493 \u1511 \u1489 \u1497 \u1501  \u1495 \u1494 \u1512 \u1492 :")\
            st.write(not_following_back)\
\
            st.subheader("\uc0\u55357 \u56907 \u8205 \u9792 \u65039  \u1492 \u1501  \u1506 \u1493 \u1511 \u1489 \u1497 \u1501  \'96 \u1493 \u1488 \u1514  \u1500 \u1488 :")\
            st.write(fans)\
\
        except Exception as e:\
            st.error(f"\uc0\u1513 \u1490 \u1497 \u1488 \u1492 : \{e\}")\
}