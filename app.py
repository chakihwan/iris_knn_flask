from flask import Flask, render_template, request, url_for
import pickle
import numpy as np

# Flask 애플리케이션 생성
app = Flask(__name__)

SPECIES_IMG = {
    'setosa' : 'images/iris_setosa.png',
    'versicolor' : 'images/iris_versicolor.png',
    'virginica' : 'images/iris_virginica.png'
}

# 모델 로드
with open('model/knn_model.pkl', 'rb') as f:
    model = pickle.load(f)

# 꽃 이름 매핑
iris_names = ['setosa', 'versicolor', 'virginica']

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    image_url = None
    err_msg = None

    if request.method == 'POST':
        try:
            # 폼에서 입력값 가져오기
            sepal_length = float(request.form['sepal_length'])
            sepal_width = float(request.form['sepal_width'])
            petal_length = float(request.form['petal_length'])
            petal_width = float(request.form['petal_width'])

            # 입력값을 배열로 변환
            features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
            # 예측 수행
            pred = model.predict(features)[0]
            # prediction = iris_names[pred]
            if isinstance(pred, (int, np.integer)):
                label = iris_names[int(pred)]
            else:
                label = str(pred).strip().lower()

            prediction = label

            if label in SPECIES_IMG:
                image_url = url_for('static', filename=SPECIES_IMG[label])

        except Exception as e:
            err_msg = f"입력 Error: {e}"
    return render_template('index.html', prediction=prediction,
                           image_url=image_url, err_msg=err_msg)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000 ,debug=True)