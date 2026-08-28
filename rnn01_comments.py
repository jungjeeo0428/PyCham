import numpy as np
from tensorflow.keras.layers import LSTM, Dense, Dropout, Embedding
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
comments = [
    # 긍정적인 댓글 (1)
    "이 영상 정말 도움이 됐어요! 감사합니다.",
    "설명이 너무 깔끔해서 이해가 잘 가네요.",
    "최고의 강의입니다. 다음 영상도 기대할게요.",
    "와 진짜 유익하다... 구독하고 갑니다!",
    "덕분에 과제 잘 마쳤어요. 진짜 감사합니다.",
    # 부정적인 댓글 (0)
    "설명이 너무 어렵고 지루해요.",
    "목소리가 잘 안 들려서 짜증나네요.",
    "도움이 하나도 안 됨. 시간 아깝다.",
    "말이 너무 빠르고 이해가 안 가요.",
    "광고가 너무 많아서 보기 힘드네요."
]
labels = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0] # 1: 긍정, 0: 부정]
#text token(words->num)
tokenizer = Tokenizer(num_words=100, oov_token='<OOV>')
tokenizer.fit_on_texts(comments) # make index
seq = tokenizer.texts_to_sequences(comments) #modify word to index
max_len = 20 #len of comments
padded = pad_sequences(seq, maxlen=max_len, padding='post', truncating='post') #make same size
x_train = np.array(padded)
y_train = np.array(labels)

model= Sequential([Embedding(input_dim=100, output_dim=20, input_length=max_len),
                   LSTM(units=40, return_sequences=False),
                   Dropout(0.2),
                   Dense(20, activation='relu'),
                   Dense(1, activation='sigmoid')
])
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=100)
def analyze_comment(new_comment):
    data = tokenizer.texts_to_sequences([new_comment])
    pad = pad_sequences(data, maxlen=max_len, padding='post', truncating='post')
    pred = model.predict(pad)[0][0]
    print(f'comment: {new_comment}, result: {"positive" if pred > 0.5 else "negative"}')
while True:
    analyze_comment(input("Enter a comment: "))


