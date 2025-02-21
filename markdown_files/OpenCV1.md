---
title: "OpenCV"
css: style.css
tags:
  - datetime
---

**(1) OpenCV 소개 **

#### OpenCV란 무엇일까요?

- **컴퓨터 비전의 핵심 도구:** OpenCV는 컴퓨터가 사람처럼 이미지를 보고 이해할 수 있게 해주는 핵심 도구입니다.
- **다양한 기능 제공:** 이미지 처리, 영상 처리, 객체 인식, 머신러닝 등 다양한 기능을 제공합니다.
- **폭넓은 활용 분야:** 실시간 영상 처리, 자율 주행, 로봇 공학, 의료 영상 분석 등 다양한 분야에서 활용됩니다.
- **오픈소스 & 쉬운 사용법:** 무료로 사용할 수 있으며, 다양한 프로그래밍 언어에서 쉽게 사용할 수 있습니다.

---

#### OpenCV 설치 및 환경 설정

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

1.  **OpenCV 설치:**
    - 터미널(명령 프롬프트)를 열고 다음 명령어를 입력하여 OpenCV를 설치합니다:
      ```bash
      pip install opencv-python
      ```
      - `pip`: 파이썬 패키지 설치 도구
      - `opencv-python`: OpenCV 라이브러리
2.  **필요한 추가 라이브러리 설치:**
    - 이미지 데이터를 다루기 위한 `numpy`와 그래프를 그리기 위한 `matplotlib`도 설치합니다:
      ```bash
      pip install numpy
      pip install matplotlib
      ```
3.  **설치 확인:**
    - 파이썬 콘솔에서 다음 코드를 실행하여 설치를 확인합니다:
      ```python
      import cv2
      print(cv2.__version__)
      ```
      - OpenCV 버전이 출력되면 정상적으로 설치된 것입니다.

</div>

---

**(2) OpenCV 주요 기능 소개 **

#### 이미지 로드 및 저장

- **이미지 로드 (읽기):** `cv2.imread()` 함수 사용
  - **기능:** 이미지 파일에서 이미지 데이터를 읽어 NumPy 배열 형태로 저장합니다.
  - **사용법:**
    ```python
    image = cv2.imread('image.jpg')  # 이미지 파일 경로 지정
    ```
    - `image`: 이미지 데이터가 저장된 NumPy 배열
    - `'image.jpg'`: 읽어올 이미지 파일의 경로. 같은 폴더에 있다면 파일 이름만 써도 됩니다.
  - **주의사항:** 이미지 파일 경로를 정확하게 입력해야 합니다.

---

- **이미지 저장:** `cv2.imwrite()` 함수 사용
  - **기능:** NumPy 배열 형태의 이미지 데이터를 파일로 저장합니다.
  - **사용법:**
    ```python
    cv2.imwrite('output.jpg', image) # 저장할 파일 경로, 저장할 이미지 데이터
    ```
    - `'output.jpg'`: 저장할 파일의 경로 및 이름
    - `image`: 저장할 이미지 데이터
  - **주의사항:** 저장할 파일의 확장자(`.jpg`, `.png` 등)에 따라 파일 형식이 결정됩니다.

---

**[실습 1]** 이미지를 로드하고 저장해 보세요.

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

1.  `image.jpg` 파일을 준비합니다. (이 파일 이름은 예시이며, 다른 이름의 파일을 사용해도 됩니다.)
2.  다음 코드를 실행해 보세요.

    ```python
    import cv2

    # 이미지 로드
    image = cv2.imread('image.jpg')

    if image is None: # 이미지 로드 실패 시
        print("Error: Could not read image.")
    else:
        # 이미지 저장
        cv2.imwrite('output.png', image)
        print("Image saved as output.png")
    ```

</div>

---

#### 기본 이미지 조작 (크기 변경, 회전, 자르기)

- **이미지 크기 변경:** `cv2.resize()` 함수 사용
  - **기능:** 이미지의 크기를 조절합니다.
  - **사용법:**
    ```python
    resized_image = cv2.resize(image, (300, 200)) # 변경할 크기 (가로, 세로)
    ```
    - `(300, 200)`: 이미지의 새로운 가로 및 세로 크기 (픽셀 단위)

---

- **이미지 회전:** `cv2.rotate()` 함수 사용
  - **기능:** 이미지를 특정 각도로 회전합니다.
  - **사용법:**
    ```python
    rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)  # 시계 방향 90도 회전
    rotated_image2 = cv2.rotate(image, cv2.ROTATE_180) # 180도 회전
    rotated_image3 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE) # 반시계 방향 90도 회전
    ```
    - `cv2.ROTATE_90_CLOCKWISE`: 시계 방향 90도 회전
    - `cv2.ROTATE_180`: 180도 회전
    - `cv2.ROTATE_90_COUNTERCLOCKWISE`: 반시계 방향 90도 회전

---

- **이미지 자르기:** NumPy 배열 슬라이싱 사용
  - **기능:** 이미지에서 특정 영역만 잘라냅니다.
  - **사용법:**
    ```python
    cropped_image = image[100:200, 50:150]  # y축 시작:끝, x축 시작:끝
    ```
    - `100:200`: y축 (세로) 방향으로 100번째 픽셀부터 199번째 픽셀까지 자릅니다.
    - `50:150`: x축 (가로) 방향으로 50번째 픽셀부터 149번째 픽셀까지 자릅니다.
    - **주의사항:** 좌표는 0부터 시작합니다.

---

**[실습 2]** 이미지 크기를 변경하고 회전, 자르기를 해보세요.

```python
import cv2

# 이미지 로드
image = cv2.imread('image.jpg')

if image is not None:
    # 크기 변경
    resized_image = cv2.resize(image, (200, 150))

    # 회전
    rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    # 자르기
    cropped_image = image[50:150, 100:200]

    # 결과 저장
    cv2.imwrite('resized_image.jpg', resized_image)
    cv2.imwrite('rotated_image.jpg', rotated_image)
    cv2.imwrite('cropped_image.jpg', cropped_image)
    print("Images resized, rotated, and cropped successfully")
else:
    print("Error: Could not load image.")
```

---

#### 색 공간 변환 (RGB <-> GrayScale)

- **색 공간 변환:** `cv2.cvtColor()` 함수 사용
  - **기능:** 이미지의 색 공간을 변경합니다.
  - **사용법:**
    ```python
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # BGR -> Gray
    rgb_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR) # Gray -> BGR
    ```
    - `cv2.COLOR_BGR2GRAY`: BGR (Blue, Green, Red) 색상 순서를 GrayScale로 변환합니다.
    - `cv2.COLOR_GRAY2BGR`: GrayScale 이미지를 BGR 이미지로 변환합니다.
  - **주의사항:** OpenCV는 이미지의 색상 채널을 **BGR** 순서로 처리합니다. 일반적인 RGB 순서와 다르다는 것을 주의하세요.

---

**[실습 3]** 이미지를 Grayscale로 변환하고 다시 RGB로 변환해 보세요.

```python
import cv2

# 이미지 로드
image = cv2.imread('image.jpg')
if image is not None:
    # BGR -> Gray
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Gray -> BGR
    rgb_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

    # 결과 저장
    cv2.imwrite('gray_image.jpg', gray_image)
    cv2.imwrite('rgb_image.jpg', rgb_image)
    print("Images converted successfully")
else:
    print("Error: Could not load image.")
```

---

#### 2.1. RGB 컬러 모델

<div style="display: flex; justify-content: space-between;">

- **RGB 컬러 모델 소개:**
  - **빛의 삼원색 (빨강, 초록, 파랑)을 조합하여 색상을 표현하는 방식:**
    - RGB 모델이란?
    - 빛의 삼원색인 빨강(Red), 초록(Green), 파랑(Blue)을 섞어 다양한 색을 표현하는 방식
    - 각 채널은 0~255 범위의 값을 가짐

<div style="max-height: 400px; overflow-y: auto;">

![RGB 컬러 모델 예시](./contents/rgb_example.jpg)

</div>

</div>

---

- **각 채널 (R, G, B)의 의미와 역할:**

- 각 채널은 특정 색의 강도 표현
- R 채널은 빨간색 빛의 강도, G 채널은 초록색 빛의 강도, B 채널은 파란색 빛의 강도 표현
- 각 채널의 강도 값을 조절하여 다양한 색상을 표현

<div class="mt-4">
  <div class="w-64 h-64 rounded-full" style="background: conic-gradient(from 0deg, rgb(255,0,0), rgb(255,255,0), rgb(0,255,0), rgb(0,255,255), rgb(0,0,255), rgb(255,0,255), rgb(255,0,0))"></div>
</div>

---

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

- **RGB 각 채널의 표현 범위:**

  - **0~255 (또는 0~1) 범위 내에서 각 채널의 강도 표현:**
  - 각 채널의 강도는 일반적으로 0부터 255까지의 정수로 표현
  - -0은 해당 색의 빛이 없다는 뜻이고, 255는 해당 색의 빛이 가장 강하다는 의미.
  - 0~1 사이의 실수로 표현하는 등(정규화) 다양한 방법 존재

- **색상 코드 (헥스코드)와의 관계:**

  - **헥스코드 (예: #FF0000 - 빨강)를 RGB 값으로 변환하는 방법:** 헥스 코드는 웹 디자인 등에서 색상을 표현하는 또 다른 방법
  - #RRGGBB 형식으로 표현되며, RR은 빨강, GG는 초록, BB는 파랑의 강도를 16진수로 표현
  - 예를 들어, #FF0000은 빨간색 빛이 가장 강하고, 초록색과 파란색 빛은 없는 빨간색을 의미함 FF는 10진수로 255

- **실습:**
  - **RGB 값 조절을 통해 다양한 색상을 만들어보고 변화를 관찰 (온라인 도구 활용):** (온라인 RGB 색상 조절 도구 링크 제공) 직접 RGB 값을 변경하며 색상 변화를 경험하고, 각 색상 채널이 어떻게 색을 만드는지 느껴보세요.

</div>

---

#### 2.2. Grayscale 이미지

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

- **Grayscale 이미지 소개:**
  - **흑백 명암으로 이미지를 표현하는 방식:** Grayscale 이미지는 흑백 명암으로만 표현되는 이미지입니다. 색상 정보가 없고, 밝고 어두움으로만 표현됩니다.
  - **각 픽셀 값의 의미와 밝기 정보 (0: 검정, 255: 흰색):** 각 픽셀은 0부터 255까지의 값을 가짐. 0은 검은색, 255는 흰색을 나타내며, 값이 커질수록 밝아짐. 중간값은 회색을 표현
- **컬러 이미지에서 Grayscale 이미지로 변환:**
  - **RGB 값의 평균, 가중 평균 등 다양한 변환 방법 소개:** 컬러 이미지를 Grayscale 이미지로 변환하는 방법은 여러 가지가 있음.
  - 가장 일반적인 방법은 RGB 값의 평균을 이용하는 것입니다. (R + G + B) / 3 과 같이 계산
  - 인간의 눈은 녹색에 가장 민감하므로 가중 평균을 사용할 수도 있음
  - 예를 들어 0.299R + 0.587G + 0.114B 와 같은 식으로 계산

![Grayscale 이미지 예시](./contents/monalisa_gray.png)

</div>

---

#### 필터 적용 (blur, sharpen, edge detection 등)

- **가우시안 블러링:** `cv2.GaussianBlur()` 함수 사용
  - **기능:** 이미지에 흐림 효과를 줍니다.
  - **사용법:**
    ```python
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0) # 커널 크기, 표준편차
    ```
    - `(5, 5)`: 블러링에 사용되는 커널(필터)의 크기. 숫자가 클수록 더 많이 흐려집니다.
    - `0`: 표준편차 (0으로 설정하면 자동으로 계산)

---

- **일반 2D 필터:** `cv2.filter2D()` 함수 사용
  - **기능:** 이미지에 사용자 정의 필터를 적용합니다.
  - **사용법:**
    ```python
    import numpy as np
    # 샤프닝 커널 예시
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    sharpened_image = cv2.filter2D(image, -1, kernel)
    ```
    - `kernel`: 적용할 필터 (NumPy 배열)
    - `-1`: 출력 이미지의 데이터 타입. 원본 이미지와 동일한 타입을 사용하도록 설정합니다.
  - **커널 이해:** 커널은 이미지에 적용되는 필터로, 이미지의 각 픽셀 주변에 적용되어 새로운 값을 생성합니다.

---

- **소벨 필터 (엣지 검출):** `cv2.Sobel()` 함수 사용
  - **기능:** 이미지에서 수직/수평 방향의 엣지를 검출합니다.
  - **사용법:**
    ```python
    sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3) # x 방향 엣지 검출
    sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3) # y 방향 엣지 검출
    ```
    - `gray_image`: 그레이스케일 이미지에 적용합니다.
    - `cv2.CV_64F`: 출력 데이터 타입 (64비트 실수)
    - `1, 0`: x 방향 미분 (1차 미분)
    - `0, 1`: y 방향 미분 (1차 미분)
    - `ksize=3`: 커널 크기

---

- **캐니 엣지 검출:** `cv2.Canny()` 함수 사용
  - **기능:** 이미지에서 엣지를 검출합니다.
  - **사용법:**
    ```python
    edges = cv2.Canny(gray_image, 100, 200) # 임계값 1, 임계값 2
    ```
    - `100, 200`: 엣지를 결정하는 데 사용되는 두 개의 임계값

---

**[실습 4]** 이미지에 다양한 필터를 적용해 보세요.

```python
import cv2
import numpy as np

# 이미지 로드
image = cv2.imread('image.jpg')
if image is not None:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 가우시안 블러링
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

    # 샤프닝
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    sharpened_image = cv2.filter2D(image, -1, kernel)

    # 소벨 필터
    sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)

    # 캐니 엣지 검출
    edges = cv2.Canny(gray_image, 100, 200)

    # 결과 저장
    cv2.imwrite('blurred_image.jpg', blurred_image)
    cv2.imwrite('sharpened_image.jpg', sharpened_image)
    cv2.imwrite('sobelx.jpg', sobelx)
    cv2.imwrite('sobely.jpg', sobely)
    cv2.imwrite('edges.jpg', edges)
    print("Images filtered successfully")
else:
    print("Error: Could not load image.")
```

---

#### 히스토그램 계산 및 시각화

- **히스토그램 계산:** `cv2.calcHist()` 함수 사용
  - **기능:** 이미지의 히스토그램을 계산합니다.
  - **사용법:**
    ```python
    hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
    ```
    - `[gray_image]`: 히스토그램을 계산할 이미지 (배열 형태로 전달)
    - `[0]`: 채널 (0은 Grayscale 이미지의 단일 채널, 컬러 이미지의 경우 [0]은 B, [1]은 G, [2]은 R)
    - `None`: 마스크 (None은 전체 이미지 사용)
    - `[256]`: 히스토그램의 bin 개수 (0부터 255까지 총 256개의 bin)
    - `[0, 256]`: 히스토그램 범위

---

- **히스토그램 시각화:** `matplotlib.pyplot.plot()` 함수 사용

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

- **기능:** 계산된 히스토그램을 그래프로 시각화합니다.
- **사용법:**

  ```python
  import matplotlib.pyplot as plt

  plt.plot(hist)
  plt.xlabel("Pixel Value")
  plt.ylabel("Frequency")
  plt.title("Image Histogram")
  plt.show()
  ```

  - `plt.plot(hist)`: 히스토그램 데이터를 사용하여 그래프를 그림
  - `plt.xlabel()`, `plt.ylabel()`, `plt.title()`: 그래프의 축 이름 및 제목 설정
  - `plt.show()`: 그래프를 화면에 출력

</div>

---

**[실습 5]** 이미지 히스토그램을 계산하고 시각화해 보세요.

```python
import cv2
import matplotlib.pyplot as plt

# 이미지 로드
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE) # 그레이 스케일로 이미지 로드
if image is not None:
    # 히스토그램 계산
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])

    # 히스토그램 시각화
    plt.plot(hist)
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.title("Image Histogram")
    plt.show()
else:
    print("Error: Could not load image.")
```

---

**(3) OpenCV 실습 예제 **

- **이미지 로드 및 표시:**
  - `cv2.imshow()` 함수: 이미지를 새 창에 표시합니다.
  - `cv2.waitKey(0)` 함수: 키보드 입력을 기다립니다.
  - `cv2.destroyAllWindows()` 함수: 열린 창을 모두 닫습니다.

```python
import cv2

# 이미지 로드
image = cv2.imread('image.jpg')

if image is not None:
    # 이미지 표시
    cv2.imshow('Image', image)
    cv2.waitKey(0) # 키 입력 대기 (0은 무한 대기)
    cv2.destroyAllWindows() # 모든 창 닫기
else:
    print("Error: Could not load image.")

```

- **기본 이미지 조작 종합 실습:**
  - 이미지 크기 조절, 회전, 자르기를 순서대로 수행하고 결과를 확인합니다.
  - 각 조작 후 `cv2.imshow()` 함수를 사용하여 결과를 화면에 표시합니다.
- **필터 적용 및 효과 비교:**
  - 다양한 필터를 이미지에 적용하고 결과를 비교합니다.
  - 원본 이미지와 필터링된 이미지를 함께 표시하여 효과를 시각적으로 확인합니다.
- **히스토그램 분석 및 활용:**
  - 이미지 히스토그램을 계산하고 그래프로 시각화합니다.
  - 히스토그램 평활화(equalization)를 통해 이미지의 밝기를 개선합니다.
