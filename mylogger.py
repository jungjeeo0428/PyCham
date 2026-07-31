import logging


def make_logger(file_nm, name):
    # 1. 로거 생성 및 기본 레벨 설정
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # 2. 포맷터 정의 (문자열 오타 수정 및 Formatter 대문자 적용)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # 3. 콘솔 핸들러 설정
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    logger.addHandler(console)

    # 4. 파일 핸들러 설정
    file_handler = logging.FileHandler(filename=file_nm, encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)  # 중복 제거

    return logger


# 메인 실행부
if __name__ == '__main__':
    log = make_logger('test.log', 'test')
    log.debug('test-ing')
    log.warning('warning!')
    log.critical('critical!')
