import streamlit as st
import requests
import pandas as pd

# タイトル
st.title("大会参加者リスト取得")

# URL入力フォームを作成
event_id = st.text_input("取得する大会のIDを入力してください。")

# フォームを作成
if st.button("送信"):
    if event_id:
        try:
            # GETリクエストを送信してデータを取得
            url = "https://asia-northeast1-uf-measure-dev.cloudfunctions.net/event/" + (event_id)
            response = requests.get(url)

            # ステータスコードを確認
            if response.status_code == 200:
                # JSONデータをパースして表示
                data = response.json()
                races = data["_embedded"]["races"]
                if races:
                    tags = races[0]["tags"]  # 最初のレースデータのtagsを取得
                    df = pd.DataFrame(tags)
                    st.dataframe(df, height=500, width=800)  # 高さ500px、幅800pxに設定

                st.success("データの取得に成功しました！")
                # st.json(data)  # 取得したJSONデータを表示

            else:
                st.error(f"データの取得に失敗しました。ステータスコード: {response.status_code}")

        except Exception as e:
            st.error(f"エラーが発生しました: {e}")
    else:
        st.error("URLを入力してください。")
