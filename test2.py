import streamlit as st

# ヘッダーを作成
st.header("ヘッダーのタイトル")

# カスタムCSSを適用してテキストを重ねる
st.markdown(
    """
    <style>
    .custom-text {
        position: absolute; /* 絶対位置に設定 */
        right: 0px; /* 右端からの距離 */
        top: 0px; /* ヘッダーの高さに合わせる */
        font-size: 18px; /* テキストのフォントサイズ */
        color: black; /* テキストの色 */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ヘッダーの右端にテキストを表示
st.markdown('<div class="custom-text">テスト版</div>', unsafe_allow_html=True)

# 他のコンテンツを表示
st.write("ここに他のコンテンツが表示されます。")
