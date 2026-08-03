from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url="http://www.hanatour.com/package/international"
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(url)
time.sleep(2)
input_search = driver.find_element(By.ID, 'input_keyword')
input_search.send_keys('하와이') #하와이가 자동으로 검색된다.
driver.find_element(By.CSS_SELECTOR, 'button.brn_search').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="ViewsPageId-AA28gj7N"]/div[1]/div/div[2]/desktop-article-content/div[1]/msn-article-page/div/cp-article-reader/article/cp-article//body/p[1]').click()
driver.quit()

