# csv 읽기
# 학생 이름의 폴더 생성
#3 해당폴더에 학생 정보 저장

import os
import csv
from datetime import datetime

#파일경로
csv_FILE = 'C:/medicalAI/Pycham/crowling/student_list.csv'
OUTPUT_DIR = './students'
os.makedirs(OUTPUT_DIR, exist_ok=True)

try:
    with open(csv_FILE, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)  #첫줄(컬럼명)
        print("컬럼:{}".format(header))
        for row in reader:
            name = row[0].strip()
            stu_path = os.path.join(OUTPUT_DIR, name)
            os.makedirs(stu_path) #펄더가 각각 이름대로 만들어진다
            phone = row[1].strip()
            email = row[2].strip()
            course = row[3].strip()
            info_path = os.path.join(stu_path, 'info.txt')
            with open(info_path, 'w', encoding='utf-8') as tf:
                tf.write(f'[학생정보]')
                tf.write("이름: {}\n".format(name))
                tf.write("연락처: {}\n".format(phone))
                tf.write("이메일: {}\n".format(email))

except FileNotFoundError:
    print('no_File')
except Exception as e:  #알수없는 에러 예외처리
    print("Error:{}".format(e))
