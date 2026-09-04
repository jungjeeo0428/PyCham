import os
import torch
import torch.nn as nn
import torch.optim as optim
os.environ['KMP_DUPLICATE_LIB_OK'] = "True" # 중복 실행 방지 numpy ,pytorch
data =[
    ("hello", "안녕"),
    ("i am a student", "나는 학생이다")
]
#          길이    시작      끝      없는 토큰
en_voc = ["<PAD>","<SOS>","<EOS>", "<UNK>"] + sorted(list(set(" ".join([d[0] for d in data]).split())))
ko_voc = ["<PAD>","<SOS>","<EOS>", "<UNK>"] + sorted(list(set(" ".join([d[1] for d in data]).split())))
en_idx = {w:i for i, w in enumerate(en_voc)}
ko_idx = {w:i for i, w in enumerate(ko_voc)}
idx_to_ko = {i:w for i, w in enumerate(ko_voc)}
def encode(sentence, voc_idx):
    return [
        #없는 단어만 UNK 있는 단어면 해당 번호 사용
        voc_idx.get(w, voc_idx["<UNK>"])
        for w in sentence.split()
    ]
# 입력 언어를 읽어서 전체 문맥을 담은 하나의 벡터 context vector로 압축하는 역할
class Encoder(nn.Module):
    def __init__(self, input_dim, hidden_dim):
        super(Encoder, self).__init__()
        # 입력 단어를 벡터로 변환
        self.embedding = nn.Embedding(input_dim, hidden_dim)
        # 문장 흐름을 반영하며 정보 누적
        self.rnn = nn.GRU(hidden_dim, hidden_dim)
    def forward(self, x):
        embedded = self.embedding(x) #(단어 수, 1, 특징 차원)
        # rnn 연산 -> 특징 추출 -> hidden layer 사용
        _, hidden = self.rnn(embedded)
        return hidden
class Decoder(nn.Module):
    def __init__(self, output_dim, hidden_dim):
        super(Decoder, self).__init__()
        self.embedding = nn.Embedding(output_dim, hidden_dim)
        self.rnn = nn.GRU(hidden_dim, hidden_dim)
        #단어 분류 점수로 변환하는 선형 레이어
        self.out = nn.Linear(hidden_dim, output_dim)
    def forward(self, x, hidden):
        # 이전 단계의 은닉 상태와 현재 단어 정보를 넣어 업데이트
        embedded = self.embedding(x)
        output, hidden = self.rnn(embedded, hidden)
        #확률점수계산
        prediction = self.out(output.squeeze(0))
        #예측값, 현재의 은닉 상태를 다음 단계로 전달
        return prediction, hidden
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
hidden_dim = 128
encoder = Encoder(len(en_voc), hidden_dim).to(device)
decoder = Decoder(len(ko_voc), hidden_dim).to(device)
optimizer = optim.Adam(list(encoder.parameters()) + list(decoder.parameters()), lr=0.001)
criterion = nn.CrossEntropyLoss()
for epoch in range(1001):
    total_loss = 0
    for en_sent, ko_sent in data:
        optimizer.zero_grad()
        #인코딩단계
        x = torch.LongTensor(encode(en_sent, en_idx)).view(-1,1).to(device)
        #컨텍스트 벡터
        context = encoder(x)
        y = [ko_idx["<SOS>"]] + encode(ko_sent, ko_idx) + [ko_idx["<EOS>"]]
        y = torch.LongTensor(y).to(device)
        decoder_input = y[0].unsqueeze(0).unsqueeze(0)
        decoder_hidden =context
        loss = 0
        for t in range(1, len(y)):
            prediction, decoder_hidden = decoder(decoder_input, decoder_hidden)
            loss += criterion(prediction, y[t].unsqueeze(0))
            decoder_input= y[t].unsqueeze(0).unsqueeze(0)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    if epoch % 200 == 0:
        print(f'epoch {epoch}, loss: {total_loss/len(data):.4f}')
print('테스트')
def translate(sentence):
    encoder.eval()
    decoder.eval()
    with torch.no_grad():
        x = torch.LongTensor(encode(sentence, en_idx)).view(-1, 1).to(device)
        context = encoder(x)
        decoder_input = torch.tensor([[ko_idx["<SOS>"]]]).to(device)
        decoder_hidden = context
        result = []
        for _ in range(10): #최대 생성 수
            prediction, decoder_hidden = decoder(decoder_input, decoder_hidden)
            # 가장 점수 높은 단어 인덱스
            idx = prediction.argmax(1).item()
            if idx == ko_idx["<EOS>"] : break
            result.append(idx_to_ko[idx])
            decoder_input = torch.tensor([[idx]]).to(device)
        return " ".join(result)

print("번역 결과")
print(f'input: hello->:{translate("hello")}')
print(f'input: i am a student->:{translate("i am a student")}')