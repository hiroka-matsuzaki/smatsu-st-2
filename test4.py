import streamlit as st
import jwt  # PyJWTライブラリを使用
from jwt import DecodeError
from pages import home, arrival, entries  # 各ページの関数をインポート
from fastapi import FastAPI


# headers = st.context.headers
# access_token = headers.get("X-Ms-Token-Aad-Access-Token")
# decoded_token = jwt.decode(access_token, options={"verify_signature": False}, algorithms=["HS256", "RS256"])
# user_name = decoded_token["name"]
user_name = "test_user_name"

st.markdown(f"""
<style>
/* サイドバーを完全に非表示にする */
.css-1d391kg {{
    display: none;  /* 旧サイドバーの非表示 */
}}
.css-18e3th9 {{
    padding: 0;  /* メインコンテンツの幅を広げる */
}}

/* Deployボタンと…メニューを非表示にする */
#MainMenu {{visibility: hidden;}}
header {{visibility: hidden;}}

/* カスタムヘッダー */
.header {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    color: white;
    padding: 15px 30px;  /* paddingを調整 */
    z-index: 100;
    display: flex; /* Flexboxを適用 */
    justify-content: space-between; /* 左右に配置 */
    align-items: center; /* 垂直中央揃え */
    background-color: #444; /* 背景色を少し明るく */
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3); /* 影を追加 */
}}

.header-left {{
    display: flex;
    align-items: center;
}}
.header-left img {{
    width: 45px; /* アイコンのサイズを少し大きく */
    height: 45px;
    margin-right: 20px; /* マージンを調整 */
}}
.header-left h1 {{
    font-size: 32px; /* タイトルのフォントサイズを大きく */
    margin-right: 40px; /* マージンを調整 */
    font-weight: bold; /* 太字にする */
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7); /* 影を追加して目立たせる */
    color: #ffcc00; /* 明るい色に変更 */
}}
.nav-menu a {{
    color: #f0f0f0; /* ナビゲーションリンクの色を調整 */
    text-decoration: none;
    margin-right: 25px; /* マージンを調整 */
    font-size: 20px; /* フォントサイズを大きく */
    transition: color 0.3s; /* ホバー効果の遷移を追加 */
}}
.nav-menu a:hover {{
    color: #ffcc00; /* ホバー時の色を調整 */
    text-decoration: underline;
}}
.beta-version {{
    font-size: 18px;
    color: #ffcc00; /* ベータ版の色を明るく */
}}
.main {{
    margin-top: 100px; /* ヘッダー分の余白を調整 */
    padding: 20px; /* コンテンツのパディングを追加 */
}}
</style>
<div class="header">
    <div class="header-left">
        <img src="./app/static/icon.png" alt="Icon">
        <h1>アレンジ君</h1>
        <nav class="nav-menu">
            <a href="?page=home" target="_self">Home</a>
            <a href="?page=arrival" target="_self">Arrival</a>
            <a href="?page=entries" target="_self">Entries</a>
            <a href="https://github.com/hiroka-matsuzaki/smatsu-st-2" target="_self">Github</a>
        </nav>
    </div>
    <div class="beta-version">
        {user_name}
    </div>
</div>
""", unsafe_allow_html=True)

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id} 

page = st.query_params.get("page", ["home"])[0]

# ページの表示
if "page" not in st.query_params or st.query_params["page"] == "home":
    home.show()
elif st.query_params["page"] == "arrival":
    arrival.show()
elif st.query_params["page"] == "entries":
    entries.show()
