# request answer
import streamlit as st
import requests
import json
HOST="http://비공개"
MODEL="gemma4:12b"
SYSTEM = 'you are my kind doctor. please answer in easy 3 sentences'
st.caption(f'{MODEL} GPU SERVER')
#record dialogue
if "message" not in st.session_state:
    st.session_state.messages = []
for m in st.session_state.messages:
    st.chat_message(m['role']).write(m['content'])


def stream_answer(prompt):
    with requests.post(f'{HOST}/api/chat',
                        json={"model": MODEL,
                              "messages": prompt,
                              "stream": True,
                              "think": False,
                              "keep_alive": "10m",
                              "options": {"temperature": 0.3}}, timeout=300, stream=True) as res:
        for line in res.iter_lines():
            if line:
                yield json.loads(line).get('message', {}).get('content','')

#chat_input
if question := st.chat_input("ask question"):
    st.session_state.messages.append({'role':'user', 'content':question})
    st.chat_message('user').write(question)
    with st.chat_message('assistant'):
        history = [{'role':'system', 'content':SYSTEM}] + st.session_state.messages
        answer = st.write_stream(stream_answer(history))
    st.session_state.messages.append({'role': 'assistant', 'content':answer})
st.sidebar.button('delete dialog', on_click=lambda : st.session_state.messages.clear())
st.sidebar.caption(f'record{len(st.session_state.messages)} messages')


#streamlit run 'file_name'