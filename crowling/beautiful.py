import re
from bs4 import BeautifulSoup

# 백틱(```) 대신 큰따옴표 3개(""")를 사용합니다.
html_doc = """
<html>
    <body>
        <ul id="news_list">
            <li class="headline"><a href="https://example.com/1">뉴스 1</a></li>
            <li class="headline"><a href="https://example.com/2">뉴스 2</a></li>
        </ul>
    </body>
</html>
"""

# beautifulSoup -> BeautifulSoup (대문자 B)
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())

# a_rr -> a_arr 변수명 오타 수정
a_arr = soup.find_all('a')
for a in a_arr:
    print(a['href'])

print('=' * 50)
print(soup.find('ul', {'id': 'news_list'}))

print('=' * 50)
print(soup.find_all('li', {'class': 'headline'}))

print(soup.select_one('#news-list'))
print(soup.select('.headline'))
en = soup.find_all('a', string=re.compile(r'[a-zA-Z]]'))
print(en)