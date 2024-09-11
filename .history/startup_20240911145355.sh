#!/bin/bash

# Streamlitの設定ファイルを作成
mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = 8000\n\
[client]\n\
showErrorDetails = false\n\
" > ~/.streamlit/config.toml

# ryeをインストールして環境をセットアップ
curl -sSf https://rye-up.com/install | bash
source ~/.rye/env

# 依存関係をインストール
rye sync

# Streamlitアプリを起動
rye run streamlit run app.py