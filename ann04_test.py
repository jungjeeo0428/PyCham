from matplotlib import pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import mnist
import numpy as np

(x_train, y_train), (x_test, y_test) = mnist.load_data()
sample = x_test[3].reshape(1,784).astype("float")/255
model = load_model('mnist_ann.keras')
print(model.summary())
pred = model.predict(sample)
pred_cls = np.argmax(pred, axis=1)
print('predict:', pred_cls)
print('answer:', y_test[3])
#imge size
image = Image.open('2.jpg')
img = image.resize((28,28)).convert('L')
img = 255-np.array(img)
plt.imshow(img)
plt.imshow(img, cmap='gray')
plt.show()
sample2 = img.reshape(1, 784).astype("float")/255
pred2 = model.predict(sample2)
pred_cls = np.argmax(pred2, axis=1)
print('predict:', pred_cls)
