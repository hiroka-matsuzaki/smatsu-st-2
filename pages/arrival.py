import streamlit as st
import requests
import pandas as pd
from datetime import datetime

def show():
  event_id = st.text_input("大会のIDを入力してください。")
  functions_url = "https://asia-northeast1-athreco.cloudfunctions.net/event/"

  col1, col2 = st.columns([1, 2])  # 横に並べるための列を作成

  with col1:
      if st.button("大会結果を見る"):
          if event_id:
              url = "https://athreco.net/event-detail-view-result/?event-id=" + event_id
              st.session_state.url = url  # URLをセッションステートに保存
          else:
              st.error("大会IDを入力してください")

  with col2:
      if 'url' in st.session_state:  # URLがセッションステートに保存されている場合
          st.markdown(f'<a href="{st.session_state.url}" target="_blank" rel="noopener noreferrer">Open URL</a>', unsafe_allow_html=True)

    
  if st.button("大会情報取得"):
    if event_id:
        try:
            # GETリクエストを送信してデータを取得
            url = functions_url + event_id
            response = requests.get(url)

            # ステータスコードを確認
            if response.status_code == 200:
                # JSONデータをパースして表示
                data = response.json()
                races = data["_embedded"]["races"]
                if races:
                    tags = races[0]["check_points "]  # 最初のレースデータのtagsを取得
                    df = pd.DataFrame(tags)
                    st.dataframe(df, height=500, width=800)  # 高さ500px、幅800pxに設定

                st.success("データの取得に成功しました！")
                # st.json(data)  # 取得したJSONデータを表示

            else:
                st.error(f"データの取得に失敗しました。ステータスコード: {response.status_code}")

        except Exception as e:
            st.error(f"エラーが発生しました: {e}")
    else:
        st.error("大会IDを入力してください。")

  # POSTリクエストを送信する関数
  def send_post_request(number, checkpoint, timestamp, event_id):
    url = functions_url + event_id
    data = {
      "race_id": 1,
      "check_point_id": (checkpoint),
      "_embedded": {
        "records": [
          {
            "bib_no": (number),
            "time": "",
            "timestamp": (timestamp),
            "input_type": "python",
            "tag_id": "tag_001"
          }
        ]
      }
    }

    response = requests.post(url, json=data)
    if response.status_code == 200:
        st.success('データが正常に送信されました。')
    else:
        st.error(f'エラーが発生しました: {response.status_code}')

  # StreamlitアプリのUI
  st.title('データ送信フォーム')

  with st.form(key='data_form'):
    number = st.text_input('番号')
    checkpoint = st.number_input('チェックポイント', min_value=0)  # チェックポイントの入力欄
    submit_button = st.form_submit_button(label='送信')

    if submit_button:
        # 現在のタイムスタンプを取得
        timestamp = datetime.now().isoformat()
        # POSTリクエストを送信
        send_post_request(number, checkpoint, timestamp, event_id)
