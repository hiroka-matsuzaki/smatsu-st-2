import streamlit as st
from streamlit.web.server.websocket_headers import _get_websocket_headers


st.title('Hello! This streamlit app is on Azure AppService.')

headers = _get_websocket_headers()
principal_name = headers.get("X-Ms-Client-Principal-Name")
principal_id = headers.get("X-Ms-Client-Principal-Id")
access_token = headers.get("X-Ms-Token-Aad-Access-Token")

st.header("AzureAD's auth results")

if principal_name is not None:
    st.markdown('X-Ms-Client-Principal-Name: ' + principal_name)
if principal_id is not None:
    st.markdown('X-Ms-Client-Principal-Id: ' + principal_id)
if access_token is not None:
    st.markdown('X-Ms-Token-Aad-Access-Token: ' + access_token)

st.header('http headers count')
st.text(len(headers))

st.header('List http headers')
if headers is not None:
    for key, value in headers.items():
        text = 'key={}, value={}'
        st.text(text.format(key, value))
