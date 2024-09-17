import streamlit as st
import requests
from datetime import datetime

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
