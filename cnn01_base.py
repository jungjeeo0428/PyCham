from tensorflow.keras.models import Sequential  # 정상 동작
from tensorflow.keras.layers import Dense, Conv2D, MaxPool2D, Flatten, Dropout
from tensorflow.keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(60000, 28, 28, 1).astype('float32')/255
x_test = x_test.reshape(10000, 28, 28, 1).astype('float32')/255
# structure of cnn
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),input_shape=(28,28,1), activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Dropout(0.25))  #과적합 방지 학습시 0.25% 연결 랜덤하게 사용안함
model.add(Flatten())# fully connected layer
model.add(Dense(10, activation='softmax')) #class
model.summary()
model.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
history = model.fit(x_train, y_train, epochs=10, batch_size=100, validation_split=0.2, verbose=1)
model.save('cnn_base.keras')
test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test loss:', test_loss)
print('Test accuracy:', test_acc)