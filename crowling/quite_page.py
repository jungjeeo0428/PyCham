import csv

import requests
from bs4 import BeautifulSoup
#정적페이지 출력
def fn_get(num):
    url="https://www.paxnet.co.kr/tbbs/list?tbbsType=L&id=N10841&page={}".format(num) #여기서 1대신 for문으로 돌리면 전체 제목도 불러올수 있다.
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    ul = soup.select_one('#comm-list')



    lis = ul.find_all('li')
    data_row = []
    for i, li in enumerate(lis):
        print("="*50)
        if i != 0:
            seq = li.select_one('.type')
            if seq:
                print(seq['data-seq'])
                title = li.select_one('.title .best-title').text.strip()
                data_row.append([seq['data-seq'], title])
    if data_row:
        with open('../dist/paxnet.csv', 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, delimiter='|')
            writer.writerows(data_row)

fn_get(2)