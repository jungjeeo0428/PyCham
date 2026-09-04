import os
# OpenMP 중복 실행으로 인한 비정상 종료 방지 설정
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
plt.rcParams['font.family'] = 'Malgun Gothic'
data = [("i am a student", "나는 학생이다"), ("i love pytorch", "나는 파이토치를 사랑한다"), ("attention is all you need", "어텐션만 있으면 충분하다"),
("i am trying to understand deep learning models and how they work", "나는 딥러닝 모델과 그것이 어떻게 작동하는지 이해하려고 노력하고 있다"),
("i am reading a book about artificial intelligence and data science", "나는 인공지능과 데이터 사이언스에 관한 책을 읽고 있다"),

("you are a person who always tries to solve problems logically", "너는 항상 문제를 논리적으로 해결하려고 하는 사람이다"),
("you can improve your skills if you practice consistently every day", "너는 매일 꾸준히 연습하면 실력을 향상시킬 수 있다"),

("he is a researcher who analyzes medical data using machine learning", "그는 머신러닝을 사용하여 의료 데이터를 분석하는 연구자이다"),
("she is developing a system that can predict future outcomes based on data", "그녀는 데이터를 기반으로 미래 결과를 예측할 수 있는 시스템을 개발하고 있다"),

("we are building a model that can classify images into different categories", "우리는 이미지를 여러 카테고리로 분류할 수 있는 모델을 만들고 있다"),
("they are working on a project that involves natural language processing and computer vision", "그들은 자연어 처리와 컴퓨터 비전을 포함하는 프로젝트를 진행하고 있다"),

("i like studying machine learning because it combines mathematics and programming", "나는 머신러닝을 공부하는 것을 좋아한다 왜냐하면 그것이 수학과 프로그래밍을 결합하기 때문이다"),
("i enjoy writing code that can solve real world problems efficiently", "나는 실제 문제를 효율적으로 해결할 수 있는 코드를 작성하는 것을 즐긴다"),

("i study every day to improve my understanding of algorithms and data structures", "나는 알고리즘과 자료구조에 대한 이해를 높이기 위해 매일 공부한다"),
("i read research papers to learn about the latest advancements in artificial intelligence", "나는 인공지능의 최신 발전을 배우기 위해 논문을 읽는다"),

("i go to the lab to run experiments and analyze the results carefully", "나는 실험을 수행하고 결과를 신중하게 분석하기 위해 연구실에 간다"),
("i come back home after finishing my work and review what i learned", "나는 일을 마친 후 집에 돌아와서 배운 내용을 복습한다"),

("this is a model that can learn complex patterns from large scale data", "이것은 대규모 데이터로부터 복잡한 패턴을 학습할 수 있는 모델이다"),
("that is a system which can automatically generate summaries from long documents", "저것은 긴 문서로부터 자동으로 요약을 생성할 수 있는 시스템이다"),

("what is the best way to train a model that generalizes well on unseen data", "보지 못한 데이터에도 잘 일반화되는 모델을 학습하는 가장 좋은 방법은 무엇인가"),
("where are you planning to apply machine learning in real world applications", "너는 머신러닝을 실제 응용에 어디에 적용할 계획인가"),

("i want to learn how to build a deep learning model that performs well on complex datasets", "나는 복잡한 데이터셋에서도 잘 작동하는 딥러닝 모델을 만드는 방법을 배우고 싶다"),
("i want to understand how attention mechanisms improve the performance of sequence models", "나는 어텐션 메커니즘이 시퀀스 모델의 성능을 어떻게 향상시키는지 이해하고 싶다"),

("machine learning is interesting because it allows systems to learn from data without explicit programming", "머신러닝은 흥미로운데 왜냐하면 명시적인 프로그래밍 없이도 데이터로부터 학습할 수 있기 때문이다"),
("deep learning is powerful because it can model highly complex relationships in data", "딥러닝은 강력한데 왜냐하면 데이터 내의 매우 복잡한 관계를 모델링할 수 있기 때문이다"),

("this model works well when the data is clean and properly preprocessed", "이 모델은 데이터가 깨끗하고 적절히 전처리되었을 때 잘 작동한다"),
("this problem is difficult because it requires both theoretical understanding and practical experience", "이 문제는 어려운데 왜냐하면 이론적 이해와 실무 경험을 모두 요구하기 때문이다"),

("i can solve this problem if i break it down into smaller and manageable parts", "나는 이 문제를 더 작고 관리 가능한 부분으로 나누면 해결할 수 있다"),
("i can understand this concept better when i visualize it using diagrams and examples", "나는 이 개념을 다이어그램과 예제로 시각화하면 더 잘 이해할 수 있다"),

("let's start the project now and define the objectives clearly before implementation", "지금 프로젝트를 시작하고 구현 전에 목표를 명확히 정의하자"),
("let's study together and share our knowledge to improve faster", "함께 공부하면서 지식을 공유하여 더 빠르게 성장하자"),

("do you like working on challenging problems that require deep thinking and creativity", "너는 깊은 사고와 창의성이 필요한 어려운 문제를 해결하는 것을 좋아하나"),
("do you understand how different models behave under various data distributions", "너는 다양한 데이터 분포에서 모델이 어떻게 동작하는지 이해하나"),

("i will try again even if i fail because failure is part of the learning process", "나는 실패하더라도 다시 시도할 것이다 왜냐하면 실패는 학습 과정의 일부이기 때문이다"),
("i will continue to improve my skills by practicing consistently and learning from mistakes", "나는 꾸준히 연습하고 실수로부터 배우면서 계속 실력을 향상시킬 것이다")
]

en_voc = ["<PAD>", "<SOS>", "<EOS>", "<UNK>"] + sorted(list(set(" ".join([d[0] for d in data]).split())))
ko_voc = ["<PAD>", "<SOS>", "<EOS>", "<UNK>"] + sorted(list(set(" ".join([d[1] for d in data]).split())))
en_idx = {w: i for i, w in enumerate(en_voc)}
ko_idx = {w: i for i, w in enumerate(ko_voc)}
idx_to_ko = {i: w for i, w in enumerate(ko_voc)}
def encode(sentence, voc_idx):
    return [
        voc_idx.get(w, voc_idx["<UNK>"])
        for w in sentence.split()
    ]
class Encoder(nn.Module):
    def __init__(self, input_dim, hidden_dim):
        super(Encoder, self).__init__()
        self.embedding = nn.Embedding(input_dim, hidden_dim)
        self.gru = nn.GRU(hidden_dim, hidden_dim)
    def forward(self, x):
        embedded = self.embedding(x)
        outputs, hidden = self.gru(embedded)
        return outputs, hidden
# 현재 내 생태(디코더)에서 인코더가 읽은 부분 중 어디에 집중해야 할지 점수 산출
class BahdanauAttention(nn.Module):
    def __init__(self, hidden_dim):
        super(BahdanauAttention, self).__init__()
        self.Wa = nn.Linear(hidden_dim, hidden_dim)
        self.Ua = nn.Linear(hidden_dim, hidden_dim)
        self.Va = nn.Linear(hidden_dim, 1)

    def forward(self, decoder_hidden, encoder_outputs):
        # decoder_hidden : 나의 현재 상태, encoder_outputs 인코더가 기억한 소스 문장 전체 정보
        src_len = encoder_outputs.size(0)
        # 문장 길이에 맞춰서 복사하여 전체와 비교 준비
        repeated_decoder_hidden = decoder_hidden.repeat(src_len, 1, 1)
        #tanh(Wa*내상태+ Ua +상대상태)를 통해 단어 간 어울림(에너지)계산
        energy = torch.tanh(self.Wa(repeated_decoder_hidden) + self.Ua(encoder_outputs))
        # 에너지를 하나의 점수로 softmax 적용해서 가중치 확률로 만듬.
        scores = self.Va(energy).squeeze(2)
        weights = F.softmax(scores, dim=0)
        return weights.transpose(0, 1)
# 계산된 어텐션 가중치를 사용하여 인토더에서 필요한 정보만 가져와서 단어 생성

class AttnDecoder(nn.Module):
    def __init__(self, output_dim, hidden_dim):
        super(AttnDecoder, self).__init__()
        self.embedding = nn.Embedding(output_dim, hidden_dim)
        # 어텐션 점수 계산
        self.attention = BahdanauAttention(hidden_dim)
        #입력(단어 임베딩) +요약 정보(문맥 벡터)를 함께 입력
        self.gru = nn.GRU(hidden_dim * 2, hidden_dim)
        self.out = nn.Linear(hidden_dim, output_dim)

    def forward(self, x, hidden, encoder_outputs):
        embedded = self.embedding(x)
        # 이번 생성 단계에서 인코더의 어디를 집중해서 볼지 가중치 계산
        attn_weights = self.attention(hidden, encoder_outputs)
        # 계산 가중치를 인코더 정보에 곱해서 이번 단계의 맞춤형 문백 벡터(context vector) 생성
        context = torch.bmm(attn_weights.unsqueeze(0), encoder_outputs.transpose(0, 1))
        #내 단어 정보와 인코더에서 골라온 정보를 합쳐서 RNN에 입력
        rnn_input = torch.cat((embedded, context), dim=2)
        #최종 특징으로 부터 가장 적절한 한국어 단어 예측
        output, hidden = self.gru(rnn_input, hidden)
        prediction = self.out(output.squeeze(0))
        return prediction, hidden, attn_weights

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
hidden_dim = 128

encoder = Encoder(len(en_voc), hidden_dim).to(device)
decoder = AttnDecoder(len(ko_voc), hidden_dim).to(device)
optimizer = optim.Adam(list(encoder.parameters()) + list(decoder.parameters()), lr=0.001)

criterion = nn.CrossEntropyLoss()
print("Training Seq2Seq with Bahdanau Attention (2015)...")
for epoch in range(1001):
    total_loss = 0
    for en_sent, ko_sent in data:
        optimizer.zero_grad()
        x = torch.LongTensor(encode(en_sent, en_idx)).view(-1, 1).to(device)
        y = [ko_idx["<SOS>"]] + encode(ko_sent, ko_idx) + [ko_idx["<EOS>"]]
        y = torch.LongTensor(y).to(device)
        enc_outputs, enc_hidden = encoder(x)
        decoder_input = y[0].unsqueeze(0).unsqueeze(0)
        decoder_hidden = enc_hidden
        loss = 0
        for t in range(1, len(y)):
            prediction, decoder_hidden, _ = decoder(decoder_input, decoder_hidden, enc_outputs)
            loss += criterion(prediction, y[t].unsqueeze(0))
            decoder_input = y[t].unsqueeze(0).unsqueeze(0)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    if epoch % 200 == 0:
        print(f"Epoch {epoch}, Loss: {total_loss/len(data):.4f}")

def show_attention(input_sentence, output_words, attentions):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111)
    cax = ax.matshow(attentions.numpy(), cmap='bone')
    fig.colorbar(cax)
    ax.set_xticklabels([''] + input_sentence.split() + ['<EOS>'], rotation=90)
    ax.set_yticklabels([''] + output_words)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
    plt.title("Attention Heatmap (Bahdanau 2015)")
    plt.show()

def evaluate_and_plot(sentence):
    encoder.eval()
    decoder.eval()
    with torch.no_grad():
        x = torch.LongTensor(encode(sentence, en_idx)).view(-1, 1).to(device)
        enc_outputs, enc_hidden = encoder(x)
        decoder_input = torch.tensor([[ko_idx["<SOS>"]]]).to(device)
        decoder_hidden = enc_hidden
        decoded_words = []
        decoder_attentions = torch.zeros(15, len(sentence.split()))

        for t in range(15):
            prediction, decoder_hidden, attn_weights = decoder(decoder_input, decoder_hidden, enc_outputs)
            decoder_attentions[t] = attn_weights.cpu()
            idx = prediction.argmax(1).item()
            if idx == ko_idx["<EOS>"]:
                decoded_words.append('<EOS>')
                break
            else:
                decoded_words.append(idx_to_ko[idx])
            decoder_input = torch.tensor([[idx]]).to(device)
        print(f"\n영어 문장: {sentence}")
        print(f"한국어 번역 결과: {' '.join(decoded_words)}")
        show_attention(sentence, decoded_words, decoder_attentions[:len(decoded_words), :])



evaluate_and_plot("I am reading a book about Michel Foucault")
evaluate_and_plot("I like studying machine learning")