import streamlit as st
import requests
from datetime import datetime

event_id = st.text_input("大会のIDを入力してください。")
# フォームを作成
if st.button("大会情報取得"):
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
                    tags = races[0]["check_points "]  # 最初のレースデータのtagsを取得
                    df = pd.DataFrame(tags)
                    st.dataframe(sorted_df, height=500, width=800)  # 高さ500px、幅800pxに設定

                st.success("データの取得に成功しました！")
                # st.json(data)  # 取得したJSONデータを表示

            else:
                st.error(f"データの取得に失敗しました。ステータスコード: {response.status_code}")

        except Exception as e:
            st.error(f"エラーが発生しました: {e}")
    else:
        st.error("URLを入力してください。")


# POSTリクエストを送信する関数
def send_post_request(number, id_value, timestamp):
    url = 'http://example.com/your-endpoint'  # 送信先のURLに置き換えてください
    data = {
        'number': number,
        'id': id_value,
        'timestamp': timestamp
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
    id_value = st.text_input('ID')
    submit_button = st.form_submit_button(label='送信')

    if submit_button:
        # 現在のタイムスタンプを取得
        timestamp = datetime.now().isoformat()
        # POSTリクエストを送信
        send_post_request(number, id_value, timestamp)
