#pip install -U selenium
import bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
url = "https://www.msn.com/ko-kr"
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(url)
time.sleep(2)
page = 1
body = driver.find_element(By.TAG_NAME, "body")
while page < 10: #100페이지까지 스크롤을 내린다.
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    page += 1
soup = bs4.BeautifulSoup(driver.page_source, "html.parser")
driver.quit()
print(soup.prettify())