import streamlit as st

# タイトル
st.title("簡単なStreamlitアプリ")

# テキスト入力フィールド
user_input = st.text_input("あなたの名前を教えてください:")

# ボタン
if st.button("送信"):
    st.write(f"こんにちは、{user_input}さん！")

# スライダーを追加
age = st.slider("年齢を教えてください:", 0, 100, 25)

# 選択結果を表示
st.write(f"あなたの年齢は {age} 歳です。")
