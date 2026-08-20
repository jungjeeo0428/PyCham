import matplotlib.pyplot as plt
from keras import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets import mnist
import numpy as np

(x_train, y_train), (x_test, y_test) = mnist.load_data()
print(x_train.shape)
print(y_train.shape)
print(x_train[0])
plt.imshow(x_train[0], cmap='Greys')
plt.show()

# reshape data
x_train = x_train.reshape(60000, 784).astype('float32')/255
x_test = x_test.reshape(10000, 784).astype('float32')/255
y_train_cate = to_categorical(y_train, 10)
y_test_cate = to_categorical(y_test, 10)

#model
model = Sequential()
model.add(Dense(512, input_shape=(784,), activation='relu'))
model.add(Dense(10, activation='softmax'))
model.compile(loss='categorical_crossentropy',optimizer='adam'
              ,metrics=['accuracy'])
history = model.fit(x_train_cate, y_train_cate, batch_size=200, epochs=30,
                    validation_data=(x_test_cate, y_test_cate))
v_loss = histroy.history(['Val_loss'])
loss = v_loss['loss']
model.save('mnist_ann.Keras')

#graph
cnt = np.arange(len(loss))
plt.plot(cnt, v_loss, marker=',', c='red', label='test')
plt.plot(cnt, loss, marker=',', c='blue', label='train')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.show()
