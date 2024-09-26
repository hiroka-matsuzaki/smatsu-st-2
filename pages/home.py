import streamlit as st
import jwt

def show():
  # headers = st.context.headers
  # access_token = headers.get("X-Ms-Token-Aad-Access-Token")
  # decoded_token = jwt.decode(access_token, options={"verify_signature": False}, algorithms=["HS256", "RS256"])

  # st.title(f'ようこそ、{decoded_token["name"]}さん！！')

  # for key, value in headers.items():
  #     text = 'key={}, value={}'
  #     st.text(text.format(key, value))

  # decoded_token = jwt.decode(access_token, options={"verify_signature": False}, algorithms=["HS256", "RS256"])

  # st.subheader("Decoded Access Token")
  # st.json(decoded_token)  # デコードされたトークンを表示
  st.title(f'ようこそHomeへ！！！')