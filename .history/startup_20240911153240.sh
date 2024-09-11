#!/bin/bash

# Streamlitの設定ファイルを作成
mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
[client]\n\
showErrorDetails = false\n\
" > ~/.streamlit/config.toml
