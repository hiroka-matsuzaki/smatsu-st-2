import streamlit as st
import requests

# APIからデータを取得
url = 'https://example.com/api/data'  # APIのエンドポイント
response = requests.get(url)

# データが正常に取得できたか確認
if response.status_code == 200:
    data = response.json()  # JSONデータをパース
    st.write("取得したデータ:")
    
    # リストのデータを表示
    for item in data['items']:  # 例: itemsがリストデータを含むキー
        st.write(item)

else:
    st.error("データの取得に失敗しました。")
