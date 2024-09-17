import streamlit as st
import requests
import pandas as pd

# タイトル
st.title("URLにGETリクエストを送信してデータを表示")

# URL入力フォームを作成
url = st.text_input("データを取得するAPIのURLを入力してください")

# フォームを作成
if st.button("送信"):
    if url:
        try:
            # GETリクエストを送信してデータを取得
            response = requests.get(url)

            # ステータスコードを確認
            if response.status_code == 200:
                # JSONデータをパースして表示
                data = response.json()
                races = data["_embedded"]["races"]
                if races:
                    tags = races[0]["tags"]  # 最初のレースデータのtagsを取得
                    
                    st.write("選手リスト:")
                    for tag in tags:
                        bib_no = tag["bib_no"]
                        title = tag["title"]
                        st.write(f"ゼッケン番号: {bib_no}, 選手名: {title}")

                st.success("データの取得に成功しました！")
                # st.json(data)  # 取得したJSONデータを表示

            else:
                st.error(f"データの取得に失敗しました。ステータスコード: {response.status_code}")

        except Exception as e:
            st.error(f"エラーが発生しました: {e}")
    else:
        st.error("URLを入力してください。")
