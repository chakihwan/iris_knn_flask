# 🌸 붓꽃 품종 예측기 (Flask & KNN)

K-최근접 이웃(KNN) 머신러닝 모델을 사용하여 붓꽃(Iris)의 품종을 예측하는 간단한 Flask 웹 애플리케이션입니다.

사용자는 웹 인터페이스를 통해 4가지 특성(꽃받침 길이/너비, 꽃잎 길이/너비)을 입력하고, 모델은 입력값을 기반으로 해당 붓꽃이 'Setosa', 'Versicolor', 'Virginica' 중 어느 품종에 속하는지 예측 결과를 반환합니다.

## ✨ 주요 기능

* **웹 기반 예측**: 사용자가 HTML 폼을 통해 4가지 붓꽃 특성(Sepal Length, Sepal Width, Petal Length, Petal Width)을 `POST` 방식으로 제출합니다.
* **KNN 모델**: `scikit-learn`의 `KNeighborsClassifier` (n_neighbors=3)로 학습된 모델(`knn_model.pkl`)을 사용하여 예측을 수행합니다.
* **결과 시각화**: 예측된 품종(`setosa`, `versicolor`, `virginica`)의 이름과 해당 품종의 샘플 이미지를 함께 표시합니다.
* **입력 도우미**:
    * **프리셋 버튼**: 각 품종의 평균값(Setosa, Versicolor, Virginica)을 폼에 자동으로 채워주는 버튼이 JavaScript로 구현되어 있습니다.
    * **툴팁**: 각 입력 필드 옆의 `?` 아이콘에 마우스를 올리면 품종별 평균값 정보를 보여주는 툴팁이 CSS로 구현되어 있습니다.

## 📂 프로젝트 구조
/
├── app.py                # Flask 메인 애플리케이션
├── train_model.py        # 모델 학습 및 저장 스크립트
├── model/
│   └── knn_model.pkl     # 학습된 KNN 모델 파일
├── templates/
│   └── index.html        # 메인 HTML 템플릿
└── static/
    ├── css/
    │   └── style.css     # CSS 스타일시트
    └── images/
        ├── iris_setosa.png    
        ├── Iris_versicolor.png
        └── iris_virginica.png

## 🚀 사용 방법

### 1. (선택 사항) 모델 재학습

`scikit-learn`을 사용하여 모델을 직접 학습시키고 저장할 수 있습니다.

```bash
# 필요한 라이브러리 설치 (예시)
# pip install scikit-learn

# 모델 학습 스크립트 실행
python train_model.py

네, 방금 생성해 드린 README 내용을 마크다운(Markdown) 원본 언어로 제공해 드릴게요. 이 내용을 복사해서 README.md 파일로 저장하시면 됩니다.

Markdown

# 🌸 붓꽃 품종 예측기 (Flask & KNN)

간단한 Flask 웹 애플리케이션으로, K-최근접 이웃(KNN) 머신러닝 모델을 사용하여 붓꽃(Iris)의 품종을 예측합니다.

사용자는 꽃받침(Sepal)과 꽃잎(Petal)의 길이와 너비를 입력하여 붓꽃이 'Setosa', 'Versicolor', 'Virginica' 중 어느 품종에 속하는지 예측 결과를 받을 수 있습니다.

## ✨ 주요 기능

* **웹 기반 예측:** 사용자가 웹 인터페이스를 통해 4가지 특성(꽃받침 길이/너비, 꽃잎 길이/너비)을 입력합니다.
* **KNN 모델 예측:** 미리 학습된 KNN 모델을 사용하여 입력된 값에 해당하는 붓꽃 품종을 예측합니다.
* **결과 및 이미지 표시:** 예측된 품종의 이름과 해당 품종의 샘플 이미지를 함께 보여줍니다.
* **데이터 프리셋:** 각 품종(Setosa, Versicolor, Virginica)의 평균값을 자동으로 입력해주는 버튼을 제공하여 테스트를 용이하게 합니다.

## 📂 프로젝트 구조

/ ├── app.py # Flask 메인 애플리케이션 ├── train_model.py # 모델 학습 및 저장 스크립트 ├── model/ │ └── knn_model.pkl # 학습된 KNN 모델 파일 ├── templates/ │ └── index.html # 메인 HTML 템플릿 └── static/ ├── css/ │ └── style.css # CSS 스타일시트 └── images/ ├── iris_setosa.png

├── Iris_versicolor.png └── iris_virginica.png


## 🚀 사용 방법

### 1. (선택 사항) 모델 재학습

`scikit-learn`을 사용하여 모델을 직접 학습시키고 저장할 수 있습니다.

```bash
# 필요한 라이브러리 설치 (예시)
# pip install scikit-learn

# 모델 학습 스크립트 실행
# python train_model.py
# 스크립트가 실행되면 model/knn_model.pkl 파일이 생성(또는 덮어쓰기)됩니다.

### 2. Flask 애플리케이션 실행
웹 애플리케이션을 실행합니다.

# 필요한 라이브러리 설치 (예시)
# pip install Flask numpy scikit-learn

# Flask 앱 실행
python app.py

### 3. 웹사이트 접속
애플리케이션이 실행되면 (* Running on http://0.0.0.0:5000/), 웹 브라우저에서 다음 주소로 접속합니다.

http://127.0.0.1:5000

🛠 사용 기술
백엔드: Python, Flask

머신러닝: Scikit-learn (KNeighborsClassifier), Numpy

모델 저장: Pickle

프론트엔드: HTML, CSS, JavaScript (ES5)
