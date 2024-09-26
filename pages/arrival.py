'''
arrival.py

これはarrival.pyです。
'''

from datetime import datetime

import requests
import streamlit as st


def show():
    st.title(f'ようこそArrivalへ！！！')
    # """
    # この関数は、引数に基づいて特定の処理を実行します。

    # Args:
    #     param1 (int): 最初のパラメータ
    #     param2 (str): 2番目のパラメータ

    # Returns:
    #     str: 処理結果
    # """

    # event_id = st.text_input("大会のIDを入力してください。")
    # functions_url = "https://asia-northeast1-athreco.cloudfunctions.net/event/"

    # col1, col2 = st.columns([1, 2])  # 横に並べるための列を作成

    # with col1:
    #     if st.button("大会結果を見る"):
    #         if event_id:
    #             base_url = "https://athreco.net/event-detail-view-result/?event-id="
    #             url = base_url + event_id
    #             st.session_state.url = url  # URLをセッションステートに保存
    #         else:
    #             st.error("大会IDを入力してください")

    # with col2:
    #     if 'url' in st.session_state:  # URLがセッションステートに保存されている場合
    #         st.markdown(
    #             (
    #                 f'<a href="{st.session_state.url}" target="_blank" '
    #                 'rel="noopener noreferrer">Open URL</a>'
    #             ),
    #             unsafe_allow_html=True
    #         )

    # if st.button("大会情報取得"):
    #     if event_id:
    #         try:
    #             # GETリクエストを送信してデータを取得
    #             url = functions_url + event_id
    #             response = requests.get(url, timeout=5)
    #             response.raise_for_status()  # HTTPエラーがあれば例外を発生させる

    #             # JSONデータをパースして表示
    #             data = response.json()
    #             st.json(data)  # 取得したJSONデータを表示

    #             races = data.get("_embedded", {}).get("races", [])
    #             if races:
    #                 race = races[0]  # 最初のレース
    #                 race_name = race.get("race_name", "不明")
    #                 check_points = race.get("check_points", [])

    #                 # レース名の表示
    #                 st.write(f"レース名: {race_name}")

    #                 # チェックポイントリストの表示
    #                 st.write("### チェックポイントリスト")
    #                 for check_point in check_points:
    #                     checkpoint_num = check_point.get('check_point_num', '不明')
    #                     checkpoint_name = check_point.get('check_point_name', '不明')
    #                     st.write(f"チェックポイント {checkpoint_num}: {checkpoint_name}")
    #             else:
    #                 st.write("レースデータが見つかりませんでした")
    #             st.success("データの取得に成功しました！")
    #         except requests.exceptions.RequestException as e:
    #             st.error(f"リクエストエラーが発生しました: {e}")
    #         except ValueError as e:
    #             st.error(f"JSONデコードエラーが発生しました: {e}")
    #         except KeyError as e:
    #             st.error(f"キーエラーが発生しました: {e}")
    #     else:
    #         st.error("大会IDを入力してください。")

    # # POSTリクエストを送信する関数
    # def send_post_request(number, checkpoint, timestamp, event_id):
    #     url = functions_url + event_id
    #     data = {
    #         "race_id": 1,
    #         "check_point_id": (checkpoint),
    #         "_embedded": {
    #             "records": [
    #                 {
    #                     "bib_no": (number),
    #                     "time": "",
    #                     "timestamp": (timestamp),
    #                     "input_type": "python",
    #                     "tag_id": "tag_001"
    #                 }
    #             ]
    #         }
    #     }

    #     response = requests.post(url, json=data, timeout=5)
    #     if response.status_code == 200:
    #         st.success('データが正常に送信されました。')
    #     else:
    #         st.error(f'エラーが発生しました: {response.status_code}')

    # # StreamlitアプリのUI
    # st.title('データ送信フォーム')

    # with st.form(key='data_form'):
    #     number = st.text_input('番号')
    #     checkpoint = st.number_input('チェックポイント', min_value=0)  # チェックポイントの入力欄
    #     submit_button = st.form_submit_button(label='送信')

    #     if submit_button:
    #         # 現在のタイムスタンプを取得
    #         timestamp = datetime.now().isoformat()
    #         # POSTリクエストを送信
    #         send_post_request(number, checkpoint, timestamp, event_id)
