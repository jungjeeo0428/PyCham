import numpy as np

class Perceptron:
    def __init__(self, input_size):
        #가중치 초기화 입력이 2개면 2+1 1은 편향
        self.w = np.zeros(input_size+1)
    def predict(self, inputs):
        sum = np.dot(inputs, self.w[1:]) + self.w[0]
        return Perceptron.step_function(sum)
    @staticmethod
    def step_function(sum):
        if sum > 0:
            return 1
        return 0
    def train(self, train_inputs, labels, lr=0.01, epochs=100):
        for _ in range(epochs):
            for inputs, label in zip(train_inputs, labels):
                #현재 가중치로 예측
                pred = self.predict(inputs)
                # w+ 학습률 *(정답= 예측) * 입력
                self.w[1:] += lr * (label - pred) * inputs
                self.w[0] += lr * (label - pred)
#학습데이터
train_data = np.array([[0, 0],[0, 1], [1, 0], [1,1]])
y_data = np.array([0, 0, 0, 1]) #and 연산 cf or 연산 [0, 1, 1, 1]
model = Perceptron(2)
model.train(train_data, y_data, lr=0.1, epochs=100)

#result
for i, v in zip(train_data, y_data):
    pred = model.predict(i)
    print(f'input:{i}, predict:{pred}, answer:{v}')
print(f'학습된 내부 가중치 : {model.w[1:]}, 편향:{model.w[0]}')