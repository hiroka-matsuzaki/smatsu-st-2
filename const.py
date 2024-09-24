SET_PAGE_CONFIG = {
    "page_title": "Streamlit Base",
    "page_icon": "😀",
    "layout": "wide",
    "initial_sidebar_state": "collapsed",
}


OPTION_MENU_CONFIG = {
    "menu_title": "Streamlit Base",
    "options": ["About", "DataBase", "Other"],
    "icons": ["bi-chat-dots", "bi-cloud-arrow-up", "bi-book"],
    "menu_icon": "bi-search",
    "default_index": 0,
    "orientation": "horizontal",
    "styles": {
        "container": {
            "display": "flex",  # 横並びのためフレックスボックスを使用
            "justify-content": "flex-start",  # 左寄せ
            "align-items": "center",  # 垂直方向のセンター揃え
            "background-color": "#fafafa",
            "padding": "10px",
        },
        "menu-title": {  # メニュータイトルのスタイルを追加
            "font-size": "25px",
            "color": "#333",
            "padding-right": "20px",  # タイトルとオプションの間に余白を追加
        },
        "icon": {"color": "#fafafa", "font-size": "25px"},
        "nav-link": {
            "font-size": "20px",
            "margin": "0px 10px",  # 各オプション間に余白を追加
            "--hover-color": "#eee",
        },
        "nav-link-selected": {"background-color": "004a55"},
    },
}

HIDE_ST_STYLE = """
                <style>
                div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stDecoration"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                #MainMenu {
                visibility: hidden;
                height: 0%;
                }
                header {
                visibility: hidden;
                height: 0%;
                }
                footer {
                visibility: hidden;
                height: 0%;
                }
				        .appview-container .main .block-container{
                            padding-top: 1rem;
                            padding-right: 3rem;
                            padding-left: 3rem;
                            padding-bottom: 1rem;
                        }  
                        .reportview-container {
                            padding-top: 0rem;
                            padding-right: 3rem;
                            padding-left: 3rem;
                            padding-bottom: 0rem;
                        }
                        header[data-testid="stHeader"] {
                            z-index: -1;
                        }
                        div[data-testid="stToolbar"] {
                        z-index: 100;
                        }
                        div[data-testid="stDecoration"] {
                        z-index: 100;
                        }
                </style>
"""

