from tkinter import *
from tkinter import scrolledtext
from img_search_util import get_img
import threading

def search_data():
    query = entry.get()
    # UI상태 업데이트
    txt.configure(state='normal')
    txt.delete(1.0, END)
    txt.insert(INSERT, f'{query} 수집을 시작합니다...\n')
    # 스크래핑 호출 (오래 걸리는 작업)
    def fetch_img():
        result, all_cnt, del_cnt = get_img(query)
        txt.insert(INSERT, '관련 이미지 수:{}\n'.format(all_cnt))
        txt.insert(INSERT, '삭제 이미지 수:{}\n'.format(all_cnt))
        txt.insert(INSERT, '수집종료')
        txt.configure(state='disabled')
    threading.Thread(target=fetch_img).start() #별도의 thread로 동작


app = Tk()
app.title('이미지 검색 수집기')
app.resizable(False, False)

lab = Label(app, text='검색어')
lab.pack()

entry = Entry(app)
entry.pack()

btn = Button(app, text='수집!', command=search_data)
btn.pack()

txt = scrolledtext.ScrolledText(app, width=40, height=20, state='disabled')
txt.pack()

app.mainloop()
