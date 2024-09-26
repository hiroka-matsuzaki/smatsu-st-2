import streamlit as st
import requests
import pandas as pd

def show():
    # st.title("大会参加者リスト取得")
    # event_id = st.text_input("取得する大会のIDを入力してください。")

    # if st.button("送信"):
    #     if event_id:
    #         try:
    #             # GETリクエストを送信してデータを取得
    #             url = "https://asia-northeast1-uf-measure-dev.cloudfunctions.net/event/" + (event_id)
    #             response = requests.get(url)

    #             # ステータスコードを確認
    #             if response.status_code == 200:
    #                 # JSONデータをパースして表示
    #                 data = response.json()
    #                 races = data["_embedded"]["races"]
    #                 if races:
    #                     tags = races[0]["tags"]  # 最初のレースデータのtagsを取得
    #                     df = pd.DataFrame(tags)
    #                     df['bib_no'] = pd.to_numeric(df['bib_no'], errors='coerce')
    #                     sorted_df = df.sort_values(by='bib_no')
    #                     st.dataframe(sorted_df, height=500, width=800)  # 高さ500px、幅800pxに設定

    #                 st.success("データの取得に成功しました！")
    #                 # st.json(data)  # 取得したJSONデータを表示

    #             else:
    #                 st.error(f"データの取得に失敗しました。ステータスコード: {response.status_code}")

    #         except Exception as e:
    #             st.error(f"エラーが発生しました: {e}")
    #     else:
    #         st.error("URLを入力してください。")

    st.title(f'ようこそEntriesへ！！！')