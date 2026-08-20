import numpy as np, pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_circles
from sklearn.svm import SVC

plt.rc('font',family='Malgun Gothic')
plt.rcParams['axes.unicode_minus']= False
plt.rcParams['font.family']



X, y = make_circles(n_samples=200, noise=0.05, factor=0.5, random_state=0)

def plot_boundary(ax, clf, X, y, title):
    h = 0.02
    x_min, x_max = X[:,0].min()-0.5, X[:,0].max()+0.5
    y_min, y_max = X[:,1].min()-0.5, X[:,1].max()+0.5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
    ax.contourf(xx, yy, Z, alpha=0.25, cmap='coolwarm')
    ax.scatter(X[:,0], X[:,1], c=y, cmap='coolwarm', edgecolor='k', s=30)
    ax.set_title(title); ax.set_xlabel('x1'); ax.set_ylabel('x2')

lin = SVC(kernel='linear').fit(X, y)
fig, ax = plt.subplots(figsize=(6, 5.5))
plot_boundary(ax, lin, X, y, f'선형 SVM — 직선으로는 실패 (정확도 {lin.score(X,y):.2f})')
plt.show()

from mpl_toolkits.mplot3d import Axes3D  # noqa

def phi(P):
    return np.column_stack([P[:,0], P[:,1], P[:,0]**2 + P[:,1]**2])

Xm = phi(X)
z_in, z_out = Xm[y==1, 2].mean(), Xm[y==0, 2].mean()
print(f'안쪽 원 평균 높이 z = {z_in:.2f},  바깥쪽 원 평균 높이 z = {z_out:.2f}')

fig = plt.figure(figsize=(8, 6.5))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(Xm[:,0], Xm[:,1], Xm[:,2], c=y, cmap='coolwarm', edgecolor='k', s=30)
# 두 무리를 가르는 평평한 판
xx, yy = np.meshgrid(np.linspace(-1.2,1.2,10), np.linspace(-1.2,1.2,10))
ax.plot_surface(xx, yy, np.full_like(xx, (z_in+z_out)/2), alpha=0.3, color='green')
ax.set_xlabel('x1'); ax.set_ylabel('x2'); ax.set_zlabel('x1² + x2²')
ax.set_title('3차원으로 올리면 평면(초록)으로 나뉜다'); plt.show()

from sklearn.svm import SVC

class PhiSVM:                       # phi로 올린 뒤 선형 SVM
    def __init__(self):
         self.m = SVC(kernel='linear')
    def fit(self, X, y):
        self.m.fit(phi(X), y); return self
    def predict(self, X):
        return self.m.predict(phi(X))

fig, ax = plt.subplots(figsize=(6, 5.5))
plot_boundary(ax, PhiSVM().fit(X, y), X, y, '올려서 나눈 뒤 내리면 → 원형 경계')
plt.show()


rbf = SVC(kernel='rbf', gamma=1).fit(X, y)
fig, ax = plt.subplots(figsize=(6, 5.5))
plot_boundary(ax, rbf, X, y, f'RBF 커널 SVM (정확도 {rbf.score(X,y):.2f})')
plt.show()
print('선형 커널 정확도:', round(lin.score(X,y),2), ' vs  RBF 커널 정확도:', round(rbf.score(X,y),2))


#초승달 shape data
from sklearn.datasets import make_moons
xm2, ym2 = make_moons(n_samples=200, noise=0.15, random_state=0)
fig, ax = plt.subplots(1, 2, figsize=(12, 5))
plot_boundary(ax[0], SVC(kernel='rbf').fit(xm2, ym2), xm2, ym2, 'rbf')
plt.show()