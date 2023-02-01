import time
import json
import streamlit as st
from streamlit_javascript import st_javascript


def get_from_local_storage(k):
    v = st_javascript(
        f"JSON.parse(localStorage.getItem('{k}'));"
    )
    return v or {}


def set_to_local_storage(k, v):
    jdata = json.dumps(v)
    st_javascript(
        f"localStorage.setItem('{k}', JSON.stringify({jdata}));"
    )


def save_update_state(st_data: dict):
    st.session_state[TOOL_PREFIX] = st_data
    set_to_local_storage(TOOL_PREFIX, st_data)

set_btn = st.button("set")
if set_btn:
  set_to_local_storage('token', 'sfsadfjiwjeeif')

get_btn = st.checkbox("get")
if get_btn:
  value = get_from_local_storage('token')
  st.write(value)