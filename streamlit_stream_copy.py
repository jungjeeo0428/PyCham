# request answer
import streamlit as st
import requests

HOST=("http://비공개")
MODEL="gemma4:12b"

st.caption(f'{MODEL} GPU SERVER')
questions = st.text_input("question", "good life cycle for high pressure patient ")
import json

def stream_answer(prompt):
    with requests.post(f'{HOST}/api/generate',
                        json={"model": MODEL,
                              "prompt": questions,
                              "stream": False,
                              "think": False,
                              "keep_alive": "10m",
                              "options": {"temperature": 0.3}}, timeout=300, stream=True) as res:
        for line in res.iter_lines():
            if line:
                yield json.loads(line).get('response', '') #조각을 그때그때 넘김




if st.button("request", type="primary"):
    st.write_stream(stream_answer(questions))
