import os
import streamlit as st
from pages import entries, arrival

# import jwt  # PyJWTライブラリを使用
# from jwt import DecodeError

# headers = st.context.headers

# access_token = headers.get("X-Ms-Token-Aad-Access-Token")

# decoded_token = jwt.decode(access_token, options={"verify_signature": False}, algorithms=["HS256", "RS256"])

# st.subheader("Decoded Access Token")
# st.json(decoded_token)  # デコードされたトークンを表示

st.title("Athreco（裏）")
st.set_page_config(initial_sidebar_state="collapsed")

pages = ["参加者一覧", "計測データ登録"]

parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(parent_dir, "Logo.svg")
styles = {
    "nav": {
        "background-color": "royalblue",
        "justify-content": "left",
        "font-size": "20px",
        "height": "60px",
    },
    "img": {
        "padding-right": "7px",
    },
    "span": {
        "color": "white",
        "padding": "14px",
    },
    "active": {
        "background-color": "white",
        "color": "var(--text-color)",
        "font-weight": "normal",
        "padding": "14px",
    }
}
options = {
    "show_menu": False, # アプリ完成時に削除したほうが良い?
    "show_sidebar": False,
}

# ナビゲーションバーのリンクページ設定
page = st_navbar(
    pages,
    logo_path=logo_path,
    styles=styles,
    options=options,
)

functions = {
    "Home": home.show_home(principal_name),
    "イベント一覧": events.show_events,
    "新規イベント": new_event.show_new_event,
    "使い方": test_page.show_test_page,
}
go_to = functions.get(page)
if go_to:
    go_to()




event_id = st.text_input("取得する大会のIDを入力してください。")
if event_id:
  button_disabled = False
else:
  button_disabled = True

if st.button("参加者リスト",disabled=button_disabled):
  