#구글 이미지 다운받는법
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib.request as req
import os


def get_img(query):
    all_cnt = 0
    del_cnt = 0
    result = []
    url = f'https://www.google.com/search?q={query}'
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    try:
        driver.get(url)
        time.sleep(1)
        # 캡차 등이 뜨면 브라우저에서 해결한 뒤 터미널에서 Enter
        input("해결한 후 Enter...")
        driver.find_element(By.LINK_TEXT, '이미지').click()
        time.sleep(1)
        start_h = driver.execute_script('return document.body.scrollHeight')
        while True:
            driver.execute_script('window.scrollTo(0, arguments[0]);', start_h) #맨 아래로 내리게
            time.sleep(2)
            next_h = driver.execute_script('return document.body.scrollHeight')
            # 더 내려가도 페이지 높이가 같으면 종료
            if start_h == next_h:
                break
            start_h = next_h
        imgs = driver.find_elements(By.TAG_NAME, 'img')
        img_set = set()
        for img in imgs:
            src = img.get_attribute('src')
            # src 주소가 있는 이미지만 추가
            if src and src.startswith('http'):
                img_set.add(src)
    finally:
        # 오류가 나도 크롬을 종료
        driver.quit()
    # 이미지 저장 폴더 생성
    img_dir = os.path.join('.', query)
    os.makedirs(img_dir, exist_ok=True)

    # 이미지 다운로드
    for i, img_url in enumerate(img_set):
        file_path = os.path.join(img_dir, f'{i}.png')
        try:
            req.urlretrieve(img_url, file_path)
        except Exception as e:
            print(f'다운로드 실패: {e}')

    # 작은 파일 삭제, 정상 파일만 result에 저장
    for filename in os.listdir(img_dir):
        file_path = os.path.join(img_dir, filename)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            if file_size < 1000:
                os.remove(file_path)
                del_cnt += 1
            else:
                result.append(file_path)
    all_cnt = len(img_set)
    return result, all_cnt, del_cnt


if __name__ == '__main__':
    print(get_img('고래'))