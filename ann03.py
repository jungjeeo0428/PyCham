import tensorflow as tf

# 기존 코드
print(f"TF : {tf.__version__}")
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
import pandas as pd

print(f"TF : {tf.__version__}")
print(f"GPU 사용 가능 여부: {tf.config.list_physical_devices('GPU')}")

# 모델 구성
model = Sequential()
model.add(Dense(128, input_dim=8, activation='relu'))
model.add(Dense(60, activation='relu'))
model.add(Dense(30, activation='relu'))
model.add(Dense(20, activation='relu'))
model.add(Dense(20, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.summary()

model.compile(loss='binary_crossentropy',
              optimizer= 'sgd', metrics=['accuracy'])
history = model.fit(x_train, y_train, epochs=100, verbose=1)
from sklearn.metrics import classification_report, confusion_matrix
pred = model.predict(x_test)
y_pred = (pred>0.5).astype(int)
print(confusion_matrix(y_test,y_pred))