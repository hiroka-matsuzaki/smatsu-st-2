import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
from pages import home, arrival, entries

st.set_page_config(initial_sidebar_state="collapsed")

pages = ["Home", "Entries", "Arrival", "GitHub"]
parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(parent_dir, "icon.svg")
urls = {"GitHub": "https://github.com/hiroka-matsuzaki/smatsu-st-2"}
styles = {
    "nav": {
        "background-color": "#333",  # ダークグレーに変更
        "display": "flex",
        "justify-content": "space-between",  # アイテムを左右に配置
        "align-items": "center",  # アイテムを垂直方向に中央揃え
        "padding": "0 20px",  # 左右にパディングを追加
        "box-shadow": "0 2px 4px rgba(0, 0, 0, 0.1)",  # 軽いシャドウ効果
    },
    "img": {
        "padding-right": "12px",  # 少しパディングを減らしてバランス調整
    },
    "span": {
        "color": "#fff",  # 白色に変更
        "padding": "12px 16px",  # パディングを調整してバランスよく
        "font-size": "1em",  # フォントサイズを設定
        "font-weight": "bold",  # フォントを太字に
    },
    "active": {
        "background-color": "#555",  # ホバー時の背景色を設定
        "color": "#f0f0f0",  # ホバー時のテキスト色を設定
        "font-weight": "bold",  # アクティブな項目のフォントを太字に
        "padding": "12px 16px",  # パディングを調整
        "border-radius": "4px",  # 角を丸くする
        "transition": "background-color 0.3s, color 0.3s",  # スムーズな色変化を追加
    }
}

options = {
    "show_menu": False,
    "show_sidebar": False,
}

page = st_navbar(
    pages,
    logo_path=logo_path,
    urls=urls,
    styles=styles,
    options=options,
)

functions = {
    "Home": home.show,
    "Arrival": arrival.show,
    "Entries": entries.show,
}
go_to = functions.get(page)
if go_to:
    go_to()