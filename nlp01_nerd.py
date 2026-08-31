from kiwipiepy import Kiwi
kiwi = Kiwi()
# NNG, NNP extract function
if __name__ == '__main__':
    text = "1990년 대비 2023년까지 일반 유·초·중·고 학생 수는 41.6% 감소한 반면, 특수교육 대상자는 무려 119.7% 증가했습니다."
    result = kiwi.analyze(text)
    print(result)
    for token in result[0][0]:
        if token.tag == "NNG":
            print(token.form, "ENTITY")

    kiwi.add_user_word("특수교육", "NNG")
    result = kiwi.analyze(text)
    print(result)
    for token in result[0][0]:
        if token.tag == "NNG":
            print(token.form, "ENTITY")