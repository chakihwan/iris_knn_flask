🌸 붓꽃 품종 예측기 (Flask & KNN)
간단한 Flask 웹 애플리케이션으로, K-Nearest Neighbors (KNN) 머신러닝 모델을 사용하여 붓꽃(Iris)의 품종을 예측합니다.

사용자가 꽃받침(Sepal)의 길이/너비와 꽃잎(Petal)의 길이/너비를 입력하면, 모델이 해당 붓꽃이 'setosa', 'versicolor', 'virginica' 중 어느 품종에 속하는지 예측 결과를 보여줍니다.

✨ 주요 기능
붓꽃 품종 예측: 4가지 특성(sepal length, sepal width, petal length, petal width)을 입력받아 품종을 예측합니다.

결과 시각화: 예측된 품종의 이름과 샘플 이미지를 함께 보여줍니다.

대표값 입력: 각 품종(setosa, versicolor, virginica)의 평균 특성값을 자동으로 입력해주는 편의 버튼을 제공합니다.

입력 가이드: 각 입력 필드마다 품종별 평균값을 알려주는 툴팁을 제공합니다.

📂 프로젝트 구조
iris_knn_flask/
├── app.py              # 메인 Flask 애플리케이션
├── train_model.py      # 모델 학습 스크립트
├── model/
│   └── knn_model.pkl   # 학습된 KNN 모델
├── templates/
│   └── index.html      # 웹페이지 HTML 템플릿
└── static/
    ├── css/
    │   └── style.css   # CSS 스타일시트
    └── images/
        ├── iris_setosa.png      
        ├── iris_versicolor.png  
        └── iris_virginica.png   
🚀 시작하기
1. 필요 라이브러리 설치
프로젝트 실행에 필요한 Python 라이브러리들을 설치합니다.

Bash

pip install Flask scikit-learn numpy
2. (선택) 모델 재학습
이미 학습된 모델(model/knn_model.pkl)이 포함되어 있습니다. 만약 모델을 직접 다시 학습시키고 싶다면 다음 명령어를 실행하세요.

Bash

python train_model.py
실행 시 model/knn_model.pkl 파일이 새로 생성되거나 덮어쓰기됩니다.

3. 웹 애플리케이션 실행
Flask 서버를 실행합니다.

Bash

python app.py
4. 서비스 접속
웹 브라우저를 열고 다음 주소로 접속합니다.

http://127.0.0.1:5000

💻 사용 방법
웹페이지에 접속하면 4개의 입력 필드가 나타납니다.

예측하려는 붓꽃의 'Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width' 값을 (cm) 단위로 입력합니다.

(선택) 하단의 'setosa', 'versicolor', 'virginica' 버튼을 클릭하여 각 품종의 평균값을 자동으로 입력할 수 있습니다.

'🌼 예측하기' 버튼을 클릭합니다.

버튼 하단에 모델이 예측한 품종 이름과 샘플 이미지가 나타납니다.
