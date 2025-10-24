import pickle
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load the iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 학습/테스트 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# KNN 모델 학습
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# 모델 저장
import os
os.makedirs('model', exist_ok=True)
with open('model/knn_model.pkl', 'wb') as f:
    pickle.dump(knn, f)

print("모델이 'model/knn_model.pkl'에 저장되었습니다.")