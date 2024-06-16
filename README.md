
# IM2LATEX
IM2LATEX는 수식 이미지를 LaTeX 형식으로 자동 변환하여 문서 작성 과정을 효율화하는 인공지능 기반 솔루션입니다. 이 프로젝트는 이미지에 포함된 수식을 인식하고 이를 LaTeX 형식으로 변환하는 시스템을 제공합니다.

## 설치 방법
1. 리포지토리를 클론합니다.
   ```bash
   git clone https://github.com/username/IM2LATEX.git
   ```
2. 모델의 체크포인트를 설치합니다
   https://www.kaggle.com/datasets/tuannguyenvananh/image2latex-checkpoints
   ```bash
   cd flask/ckpt
   Conv_BiLSTM_LSTM.ckpt 저장
   ```
3. 필요한 의존성을 설치합니다.
   ```bash
   cd flask/
   pip install -r requirements.txt
   ```
4. flask api를 실행합니다.
   ```bash
   python app.py
   ```
5. vue.js를 빌드합니다.
   ```bash
   cd vue-im2latex
   npm run build
   ```
6. Im2latexSpringApplication을 실행합니다.


## 사용 방법
1. https://localhost 에 접속합니다.
2. LaTeX 변환이 필요한 수식 이미지를 업로드합니다.
3. 변환된 LaTeX 코드를 확인하고, 복사하거나 다운로드합니다.

### 예시
![화면 캡처 2024-06-16 233310](https://github.com/BigRain02/IM2LATEX/assets/109780232/4219fb78-5118-4359-98fe-fb30c1d5c9a3)



## 프로젝트 구조

### Flask API
- **역할**: 인공지능 모델의 예측 결과를 백엔드로 보내는 역할을 합니다. 이미지로부터 수식을 인식하고 이를 LaTeX 형식으로 변환하는 핵심 기능을 담당합니다.
- **위치**: `flask/` 폴더에 위치해 있습니다.
- **구조**:
```
flask/
flask/
    app.py
    main.py
    requirements.txt
    data/
        __init__.py
        datamodule.py
        dataset.py
        vocab/
            100k_vocab.json
    image2latex/
        __init__.py
        attention.py
        decoder.py
        encoder.py
        im2latex.py
        model.py
        text.py
    lightning_logs/
```

### Spring Boot 백엔드
- **역할**: 웹 애플리케이션의 백엔드 서버로, 클라이언트와 Flask API 간의 데이터 통신을 관리합니다. 사용자 인증, 데이터베이스 관리 등의 기능도 포함됩니다.
- **위치**: `src/` 폴더에 위치해 있습니다.
- **구조**:
```
src/
src/
    main/
        java/
            com/
                example/
                    im2latexspring/
                        Im2latexSpringApplication.java
                        controller/
                            FlaskController.java
                        service/
                            FlaskService.java
        resources/
            application.yml
            static/
                favicon.ico
                index.html
    test/
        java/
            com/
                example/
                    im2latexspring/
                        Im2latexSpringApplicationTests.java
```

### Vue.js 프론트엔드
- **역할**: 사용자 인터페이스를 담당합니다. 사용자가 이미지를 업로드하고 변환된 LaTeX 코드를 확인하는 등의 작업을 할 수 있도록 합니다.
- **위치**: `vue-im2latex/` 폴더에 위치해 있습니다.
- **구조**:
```
vue-im2latex/
    .gitignore
    babel.config.js
    jsconfig.json
    package-lock.json
    package.json
    vue.config.js
    public/
        favicon.ico
        index.html
    src/
        App.vue
        main.js
        assets/
            logo.png
        components/
            HelloWorld.vue
            ImageUploader.vue
            LatexRender.vue
```
- **연동 방법**:
  1. `vue.config.js` 파일을 수정합니다.
     ```js
     const { defineConfig } = require('@vue/cli-service')
     module.exports = defineConfig({
       transpileDependencies: true,
       outputDir:"../src/main/resources/static",
        devServer:{
          proxy: 'http://localhost'
        }
     })
     ```
  2. 다음 명령어를 실행하여 프론트엔드를 빌드하면 src/main/resources/static폴더에 저장됩니다.
     ```bash
     npm run build
     ```
 3. Spring Boot 어플리케이션을 실행하여 연동된 것을 확인합니다.



## 시스템 구조
![image](https://github.com/BigRain02/IM2LATEX/assets/109780232/9dc118ef-80f6-448d-acf3-d19ac891f537)
![image](https://github.com/BigRain02/IM2LATEX/assets/109780232/0e2fddde-9ff4-498d-8481-c1085f24681b)

### 기술 스택
- IDE: IntelliJ IDEA
- API Platform: Postman
- 백엔드: Java (Spring Boot)
![image](https://github.com/BigRain02/IM2LATEX/assets/109780232/4decf768-c8b0-4f29-b5b4-499c9362c1ae)
- 프론트엔드: JavaScript (Vue.js)
- 인공지능 API: Python (Flask)
