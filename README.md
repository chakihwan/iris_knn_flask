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

* **`train_model.py`**: `sklearn`의 `load_iris` 데이터셋을 불러와 `KNeighborsClassifier` (n_neighbors=3) 모델을 학습시키고, 결과를 `model/knn_model.pkl` 파일로 저장합니다.
* **`app.py`**:
    * `model/knn_model.pkl` 파일을 로드합니다.
    * 루트 URL (`/`)에 대해 `GET` (페이지 렌더링) 및 `POST` (폼 제출 처리) 요청을 처리합니다.
    * `POST` 요청 시 폼 데이터를 받아 `numpy` 배열로 변환 후 `model.predict()`를 호출합니다.
    * 예측 결과(품종 이름)와 해당 이미지 URL을 `index.html` 템플릿으로 전달합니다.
* **`templates/index.html`**:
    * 4개의 `input[type="number"]` 필드를 가진 폼을 포함합니다.
    * Jinja2 템플릿을 사용하여 `prediction`, `image_url`, `err_msg` 변수를 조건부로 렌더링합니다.
    * 프리셋 버튼(`setosa`, `versicolor`, `virginica`)을 위한 간단한 JavaScript 코드가 포함되어 있습니다.
* **`static/css/style.css`**:
    * 그라데이션 배경, 둥근 모서리, 그림자 효과 등 모던한 UI 스타일을 정의합니다.
    * `.tooltip`, `.preset-group`, `.result` 등 커스텀 클래스 스타일을 포함합니다.

## 🚀 실행 방법

### 1. (선택 사항) 모델 재학습

필요한 경우, `train_model.py`를 실행하여 `model/knn_model.pkl` 파일을 새로 생성하거나 업데이트할 수 있습니다.

```bash
# scikit-learn, numpy 필요
# pip install scikit-learn numpy

# 모델 학습 스크립트 실행
python train_model.py

2. Flask 애플리케이션 실행
메인 애플리케이션을 실행합니다.

Bash

# Flask, numpy, scikit-learn 필요
# pip install Flask numpy scikit-learn

# Flask 앱 실행 (디버그 모드)
python app.py
3. 웹사이트 접속
애플리케이션이 실행되면 (* Running on http://0.0.0.0:5000/), 웹 브라우저에서 다음 주소로 접속합니다.

http://127.0.0.1:5000

🛠 사용 기술
백엔드: Python, Flask

머신러닝: Scikit-learn (KNeighborsClassifier), Numpy

모델 저장: Pickle

프론트엔드: HTML, CSS, JavaScript (ES5)
