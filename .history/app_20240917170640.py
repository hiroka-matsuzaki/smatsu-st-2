import os
import streamlit as st
from pages import entries, arrival

import jwt  # PyJWTライブラリを使用
from jwt import DecodeError

headers = st.context.headers

access_token = headers.get("X-Ms-Token-Aad-Access-Token")

decoded_token = jwt.decode(access_token, options={"verify_signature": False}, algorithms=["HS256", "RS256"])

st.subheader("Decoded Access Token")
st.json(decoded_token)  # デコードされたトークンを表示

# st.title("Athreco（裏）")

# event_id = st.text_input("取得する大会のIDを入力してください。")
# if event_id:
#   button_disabled = False
# else:
#   button_disabled = True

# if st.button("参加者リスト",disabled=button_disabled):
  
  