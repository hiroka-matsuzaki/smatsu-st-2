import streamlit as st
import jwt  # PyJWTライブラリを使用
from jwt import DecodeError

headers = st.context.headers

access_token = headers.get("X-Ms-Token-Aad-Access-Token")

if access_token:
    try:
        # アクセストークンをデコード（署名の検証なし）
        decoded_token = jwt.decode(access_token, options={"verify_signature": False}, algorithms=["HS256", "RS256"])
        
        st.subheader("Decoded Access Token")
        st.json(decoded_token)  # デコードされたトークンを表示
        
    except DecodeError:
        st.error("アクセストークンのデコードに失敗しました。")