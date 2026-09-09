# request answer
import streamlit as st
import requests

HOST="http://비공개"
MODEL="gemma4:12b"

st.caption(f'{MODEL} GPU SERVER')
questions = st.text_input("question", "good life cycle for high pressure patient ")
if st.button("request", type="primary"):
    with st.spinner("thinking..."):
        res = requests.post(f'{HOST}/api/generate',
                            json= {"model":MODEL,
                                   "prompt":questions,
                                   "stream": False,
                                   "think": False,
                                   "keep_alive":"10m",
                                   "options": {"temperature":0.3}}, timeout=300).json()
        st.markdown(res["response"])
        st.caption(f'{res["eval_count"]} token, {res["total_duration"]/1e9:.1f}sec')