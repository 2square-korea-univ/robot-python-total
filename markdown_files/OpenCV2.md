# OpenCV-Python 강좌: 이미지 처리 기초

---

## 강좌 소개

본 강좌는 OpenCV-Python 튜토리얼을 기반으로 이미지 처리의 기본 개념과 OpenCV 라이브러리의 사용법을 익히는 것을 목표로 합니다.

**학습 목표:**

- OpenCV-Python 환경 설정 및 기본 사용법 이해
- 이미지 및 영상 데이터 처리 기초
- 다양한 이미지 처리 기법 습득 및 응용

---

## 목차

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

1. 이미지 다루기
2. 영상 다루기
3. 도형 그리기
4. Mouse로 그리기
5. Trackbar
6. Basic Operation (기본 연산)
7. 이미지 연산
8. 이미지 Processing (처리)
9. 이미지 임계처리
10. 이미지의 기하학적 변형
11. Image Smoothing (이미지 스무딩)
12. Morphological Transformations (형태학적 변환)
13. Image Gradients (이미지 기울기)
14. Image Pyramids (이미지 피라미드)
15. Image Contours (이미지 윤곽선)
16. Contour Feature (윤곽선 특징)
17. Contour Property (윤곽선 속성)
18. Contours Hierarchy (윤곽선 계층 구조)
19. 히스토그램
20. 히스토그램 균일화
21. 2D Histogram (2차원 히스토그램)
22. 푸리에 변환
23. 템플릿 매칭
24. 허프 변환
25. Hough Circle Transform (허프 원 변환)
26. Watershed 알고리즘을 이용한 이미지 분할
27. k-Nearest Neighbour(kNN)
28. kNN을 이용한 숫자 인식
29. Demo 준비 1 & 2

</div>

---

## 1. 이미지 다루기 (Image Handling)

**Goal:**

- 이미지 파일 읽기, 보기, 저장 방법 학습
- `cv2.imread()`, `cv2.imshow()`, `cv2.imwrite()` 함수 이해
- Matplotlib를 이용한 이미지 출력 방법 학습

---

### 1.1 이미지 읽기: `cv2.imread()`

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

OpenCV를 사용하기 위한 기본 모듈 import:

```python
import cv2
```

`cv2.imread()` 함수를 사용하여 이미지 파일을 읽습니다.

```python
img = cv2.imread('lena.jpg', cv2.IMREAD_COLOR)
```

- **`cv2.imread(fileName, flag)`**: 이미지 파일을 읽어 NumPy 배열 (ndarray) 객체로 반환합니다.

| Parameter  | Description                                 |
| :--------- | :------------------------------------------ |
| `fileName` | 이미지 파일 경로 (상대 경로 또는 절대 경로) |
| `flag`     | 이미지 읽기 옵션 (아래 표 참조)             |

**`flag` 옵션:**

| Flag                   | Value | Description                                                           |
| :--------------------- | :---- | :-------------------------------------------------------------------- |
| `cv2.IMREAD_COLOR`     | 1     | 컬러 이미지로 읽기 (투명 부분 무시, 기본값)                           |
| `cv2.IMREAD_GRAYSCALE` | 0     | 흑백 이미지 (Grayscale) 로 읽기 (이미지 처리 중간 단계에서 자주 사용) |
| `cv2.IMREAD_UNCHANGED` | -1    | Alpha 채널 포함하여 읽기 (투명도 정보 유지)                           |

**Note:** `flag` 값 대신 정수 `1`, `0`, `-1`을 직접 사용할 수도 있습니다.

</div>

---

| Parameter  | Description                                 |
| :--------- | :------------------------------------------ |
| `fileName` | 이미지 파일 경로 (상대 경로 또는 절대 경로) |
| `flag`     | 이미지 읽기 옵션 (아래 표 참조)             |

**`flag` 옵션:**

| Flag                   | Value | Description                                                           |
| :--------------------- | :---- | :-------------------------------------------------------------------- |
| `cv2.IMREAD_COLOR`     | 1     | 컬러 이미지로 읽기 (투명 부분 무시, 기본값)                           |
| `cv2.IMREAD_GRAYSCALE` | 0     | 흑백 이미지 (Grayscale) 로 읽기 (이미지 처리 중간 단계에서 자주 사용) |
| `cv2.IMREAD_UNCHANGED` | -1    | Alpha 채널 포함하여 읽기 (투명도 정보 유지)                           |

**Note:** `flag` 값 대신 정수 `1`, `0`, `-1`을 직접 사용할 수도 있습니다.

---

| Parameter  | Description                                 |
| :--------- | :------------------------------------------ |
| `fileName` | 이미지 파일 경로 (상대 경로 또는 절대 경로) |
| `flag`     | 이미지 읽기 옵션 (아래 표 참조)             |

**`flag` 옵션:**

| Flag                   | Value | Description                                                           |
| :--------------------- | :---- | :-------------------------------------------------------------------- |
| `cv2.IMREAD_COLOR`     | 1     | 컬러 이미지로 읽기 (투명 부분 무시, 기본값)                           |
| `cv2.IMREAD_GRAYSCALE` | 0     | 흑백 이미지 (Grayscale) 로 읽기 (이미지 처리 중간 단계에서 자주 사용) |
| `cv2.IMREAD_UNCHANGED` | -1    | Alpha 채널 포함하여 읽기 (투명도 정보 유지)                           |

**Note:** `flag` 값 대신 정수 `1`, `0`, `-1`을 직접 사용할 수도 있습니다.

---

| Parameter  | Description                                 |
| :--------- | :------------------------------------------ |
| `fileName` | 이미지 파일 경로 (상대 경로 또는 절대 경로) |
| `flag`     | 이미지 읽기 옵션 (아래 표 참조)             |

**`flag` 옵션:**

| Flag                   | Value | Description                                                           |
| :--------------------- | :---- | :-------------------------------------------------------------------- |
| `cv2.IMREAD_COLOR`     | 1     | 컬러 이미지로 읽기 (투명 부분 무시, 기본값)                           |
| `cv2.IMREAD_GRAYSCALE` | 0     | 흑백 이미지 (Grayscale) 로 읽기 (이미지 처리 중간 단계에서 자주 사용) |
| `cv2.IMREAD_UNCHANGED` | -1    | Alpha 채널 포함하여 읽기 (투명도 정보 유지)                           |

**Note:** `flag` 값 대신 정수 `1`, `0`, `-1`을 직접 사용할 수도 있습니다.

---

### 1.2 이미지 데이터: NumPy ndarray

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

`cv2.imread()`로 읽은 이미지 데이터는 NumPy의 `ndarray` (N-dimensional array) 타입입니다.

이미지 데이터의 형태 확인:

```python
img.shape
```

출력 예시: `(206, 207, 3)`

- **3차원 행렬:** 높이(행), 너비(열), 채널 수
  - `206`: 높이 (Y축)
  - `207`: 너비 (X축)
  - `3`: 채널 (BGR 색상 정보)

**채널 정보:**

- **BGR:** OpenCV는 기본적으로 BGR (Blue, Green, Red) 순서로 색상을 표현합니다. (일반적인 RGB 순서와 다름에 유의)

</div>

---

### 1.3 이미지 보기: `cv2.imshow()`

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

`cv2.imshow()` 함수는 이미지를 윈도우 창에 표시합니다.

```python
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

- **`cv2.imshow(title, image)`**: 이미지 데이터를 윈도우 창에 표시합니다.

| Parameter | Description                          |
| :-------- | :----------------------------------- |
| `title`   | 윈도우 창 제목 (문자열)              |
| `image`   | 표시할 이미지 데이터 (NumPy ndarray) |

**`cv2.waitKey(delay)`**: 키보드 입력을 대기하는 함수입니다.

- `delay = 0`: 키 입력이 있을 때까지 무한정 대기
- `delay > 0`: `delay` 밀리초 동안 대기 (동영상 프레임 표시 등에 사용)

**`cv2.destroyAllWindows()`**: 화면에 열린 모든 OpenCV 윈도우 창을 닫습니다.

**일반적으로 `cv2.imshow()`, `cv2.waitKey()`, `cv2.destroyAllWindows()`는 함께 사용됩니다.**

</div>

---

### 1.4 샘플 코드: 이미지 읽고 보기

```python
import cv2

fname = 'lena.jpg'

original = cv2.imread(fname, cv2.IMREAD_COLOR)
gray = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
unchange = cv2.imread(fname, cv2.IMREAD_UNCHANGED)

cv2.imshow('Original', original)
cv2.imshow('Gray', gray)
cv2.imshow('Unchange', unchange)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

### 1.5 이미지 저장: `cv2.imwrite()`

`cv2.imwrite()` 함수는 이미지 또는 동영상 프레임을 파일로 저장합니다.

```python
cv2.imwrite('lenagray.png', gray)
```

- **`cv2.imwrite(fileName, image)`**: 이미지 데이터를 파일로 저장합니다.

| Parameter  | Description                          |
| :--------- | :----------------------------------- |
| `fileName` | 저장할 파일 이름 (경로 포함 가능)    |
| `image`    | 저장할 이미지 데이터 (NumPy ndarray) |

---

### 1.6 샘플 코드: 이미지 저장 (키 입력으로 저장)

```python
import cv2

img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27: # esc key (ASCII 코드 27)
    cv2.destroyAllWindows()
elif k == ord('s'): # 's' key (ASCII 코드 's')
    cv2.imwrite('lenagray.png',img)
    cv2.destroyAllWindows()
```

**Warning (64bit OS):** 64bit OS 환경에서는 `k = cv2.waitKey(0) & 0xFF` 와 같이 bit 연산을 수행해야 키 입력이 제대로 인식될 수 있습니다.

---

### 1.7 Matplotlib 사용

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Matplotlib는 Python의 강력한 plotting 라이브러리입니다. OpenCV 이미지 데이터를 표시하고 분석하는 데 유용합니다.

**Matplotlib 장점:**

- 이미지 확대/축소 (Zoom) 기능
- 하나의 화면에 여러 이미지 동시 표시
- 다양한 plot 기능 제공

**샘플 코드:**

```python
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg', cv2.IMREAD_COLOR)

plt.imshow(img)
plt.xticks([]) # x축 눈금 제거
plt.yticks([]) # y축 눈금 제거
plt.show()
```

**실행 결과:**

[Matplotlib Result - Incorrect Color]

**문제점:** Matplotlib으로 표시된 이미지의 색상이 원본과 다르게 푸른색 계열로 나타납니다.

</div>

---

### 1.8 Matplotlib 색상 문제 해결 (BGR to RGB)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Matplotlib는 이미지를 RGB (Red, Green, Blue) 순서로 해석하지만, OpenCV는 BGR 순서를 사용합니다. 따라서 Matplotlib으로 이미지를 올바르게 표시하려면 색상 채널 순서를 변경해야 합니다.

**해결 방법:**

1. `cv2.split(img)`: BGR 이미지를 B, G, R 채널로 분리합니다.
2. `cv2.merge([r,g,b])`: 분리된 채널을 RGB 순서로 재조합합니다.

**수정된 샘플 코드:**

```python
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg', cv2.IMREAD_COLOR)

b, g, r = cv2.split(img)   # BGR 이미지 채널 분리
img_rgb = cv2.merge([r,g,b]) # RGB 순서로 채널 재조합

plt.imshow(img_rgb)
plt.xticks([])
plt.yticks([])
plt.show()
```

**RGB 값으로 변경 후 Matplotlib에서 원본과 동일한 색상으로 이미지가 표시됩니다.**

</div>

---

## 2. 영상 다루기 (Video Handling)

**Goal:**

- 카메라 또는 비디오 파일로부터 영상 재생 방법 학습
- 영상 저장 방법 학습
- `cv2.VideoCapture()`, `cv2.VideoWriter()` 함수 이해

---

### 2.1 카메라로부터 영상 재생

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

카메라로부터 영상을 읽어와 화면에 표시하는 과정:

1. **VideoCapture 객체 생성:** `cv2.VideoCapture(device_index)`

   - `device_index`: 카메라 장치 인덱스 (일반적으로 내장 카메라는 `0`)

2. **프레임 읽기 루프:** `cap.read()`

   - `ret, frame = cap.read()`: 카메라로부터 프레임 읽기
     - `ret`: 프레임 캡처 성공 여부 (Boolean)
     - `frame`: 캡처된 프레임 (NumPy ndarray)

3. **프레임 처리 및 표시:** `cv2.imshow()`, `cv2.cvtColor()` 등

4. **종료 처리:** `cap.release()`, `cv2.destroyAllWindows()`
   - `cap.release()`: VideoCapture 객체 해제 (카메라 자원 반환)

</div>

---

### 2.2 샘플 코드: 카메라 영상 GrayScale로 재생

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

```python
import cv2

cap = cv2.VideoCapture(0) # 카메라 장치 0번

# 카메라 속성 확인 (width, height)
print('width: {0}, height: {1}'.format(cap.get(3), cap.get(4)))

# 카메라 속성 변경 (width, height 설정)
cap.set(3, 320) # width
cap.set(4, 240) # height

while(True):
    ret, frame = cap.read() # 프레임 읽기

    if (ret):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # GrayScale 변환
        cv2.imshow('frame', gray) # GrayScale 프레임 표시

        if cv2.waitKey(1) & 0xFF == ord('q'): # 'q' 키 입력 시 종료
            break

cap.release() # VideoCapture 객체 해제
cv2.destroyAllWindows() # 윈도우 창 닫기
```

**`cap.get(propId)` / `cap.set(propId, value)`**: VideoCapture 객체의 속성 (Property) 값을 얻거나 설정합니다.

- `propId`: 속성 ID (예: `3` - width, `4` - height)

</div>

---

### 2.3 파일로부터 영상 재생

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

비디오 파일로부터 영상 재생 방법은 카메라 재생과 거의 동일합니다. `cv2.VideoCapture()` 함수에 비디오 파일 경로를 인자로 전달합니다.

```python
import cv2

cap = cv2.VideoCapture('vtest.avi') # 비디오 파일 경로

while(cap.isOpened()): # 비디오 파일 열기 성공 여부 확인
    ret, frame = cap.read()

    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break # ret == False (파일 끝 or 오류)

cap.release()
cv2.destroyAllWindows()
```

**Note:** 비디오 재생 시 해당 비디오 파일의 코덱 (Codec) 이 설치되어 있어야 합니다.

</div>

---

### 2.4 영상 저장: `cv2.VideoWriter()`

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

영상을 파일로 저장하려면 `cv2.VideoWriter` 객체를 생성해야 합니다.

- **`cv2.VideoWriter(outputFile, fourcc, fps, frameSize)`**: VideoWriter 객체 생성

| Parameter    | Description                                                            |
| :----------- | :--------------------------------------------------------------------- |
| `outputFile` | 저장될 파일 이름 (경로 포함)                                           |
| `fourcc`     | Codec 정보 (Four Character Code). `cv2.VideoWriter_fourcc()` 함수 사용 |
| `fps`        | 초당 프레임 수 (frames per second)                                     |
| `frameSize`  | 프레임 크기 (width, height) 튜플                                       |

**`fourcc` 정보:**

- `cv2.VideoWriter_fourcc('M','J','P','G')` 또는 `cv2.VideoWriter_fourcc(*'MJPG')` 와 같이 표현
- 운영체제 (OS) 및 환경에 따라 지원하는 코덱이 다릅니다. (Windows: 'DIVX' 추천)

</div>

---

### 2.5 샘플 코드: 카메라 영상 저장

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

```python
import cv2

cap = cv2.VideoCapture(0) # 카메라 장치 0번

# 코덱 설정 (DIVX)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# VideoWriter 객체 생성 (output.avi 파일, DIVX 코덱, 25 FPS, 640x480 사이즈)
out = cv2.VideoWriter('output.avi', fourcc, 25.0, (640, 480))

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret:
        frame = cv2.flip(frame, 0) # 이미지 상하 반전 (0: 상하, 1: 좌우)

        out.write(frame) # 프레임 저장

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release() # VideoCapture 객체 해제
out.release() # VideoWriter 객체 해제
cv2.destroyAllWindows()
```

</div>

---

## 3. 도형 그리기 (Drawing Shapes)

**Goal:**

- 다양한 도형 (직선, 사각형, 원, 타원, 다각형) 그리기 학습
- 이미지에 텍스트 추가 방법 학습
- `cv2.line()`, `cv2.circle()`, `cv2.rectangle()`, `cv2.putText()` 함수 이해

**도형 그리기의 활용:**

- 객체 검출 (Object Detection) 결과 표시
- 이미지에 시각적인 정보 추가

---

### 3.1 직선 그리기: `cv2.line()`

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

`cv2.line()` 함수는 시작점과 끝점을 연결하는 직선을 그립니다.

- **`cv2.line(img, start, end, color, thickness)`**

| Parameter   | Description                                   |
| :---------- | :-------------------------------------------- |
| `img`       | 그림을 그릴 이미지 (NumPy ndarray)            |
| `start`     | 시작 좌표 (x, y) 튜플 (예: `(0, 0)`)          |
| `end`       | 종료 좌표 (x, y) 튜플 (예: `(511, 511)`)      |
| `color`     | BGR 색상 값 (튜플) (예: `(255, 0, 0)` - Blue) |
| `thickness` | 선 두께 (pixel 단위, 정수)                    |

**샘플 코드:**

```python
import numpy as np
import cv2

# 검정색 배경 이미지 생성 (512x512, 3 channels, 8-bit unsigned integer)
img = np.zeros((512, 512, 3), np.uint8)

# 대각선 (Blue, 두께 5px)
img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

</div>

---

### 3.2 사각형 그리기: `cv2.rectangle()`

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

`cv2.rectangle()` 함수는 좌상단 (top-left corner) 과 우하단 (bottom-right corner) 점을 연결하는 사각형을 그립니다.

- **`cv2.rectangle(img, start, end, color, thickness)`**

| Parameter   | Description                                              |
| :---------- | :------------------------------------------------------- |
| `img`       | 그림을 그릴 이미지                                       |
| `start`     | 좌상단 좌표 (x, y) 튜플 (예: `(384, 0)`)                 |
| `end`       | 우하단 좌표 (x, y) 튜플 (예: `(510, 128)`)               |
| `color`     | BGR 색상 값 (튜플) (예: `(0, 255, 0)` - Green)           |
| `thickness` | 선 두께 (pixel 단위, 정수). `-1` 이면 사각형 내부 채우기 |

**샘플 코드:**

```python
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3) # Green 사각형
```

</div>

---

### 3.3 원 그리기: `cv2.circle()`

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

`cv2.circle()` 함수는 원의 중심 좌표와 반지름을 이용하여 원을 그립니다.

- **`cv2.circle(img, center, radius, color, thickness)`**

| Parameter   | Description                                          |
| :---------- | :--------------------------------------------------- |
| `img`       | 그림을 그릴 이미지                                   |
| `center`    | 원의 중심 좌표 (x, y) 튜플 (예: `(447, 63)`)         |
| `radius`    | 반지름 (pixel 단위, 정수)                            |
| `color`     | BGR 색상 값 (튜플) (예: `(0, 0, 255)` - Red)         |
| `thickness` | 선 두께 (pixel 단위, 정수). `-1` 이면 원 내부 채우기 |

**샘플 코드:**

```python
img = cv2.circle(img, (447, 63), 63, (0, 0, 255), -1) # Red 원 (내부 채우기)
```

</div>

---

### 3.4 타원 그리기: `cv2.ellipse()`

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

`cv2.ellipse()` 함수는 타원의 중심, 장축/단축 길이, 각도 등을 이용하여 타원을 그립니다.

- **`cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color[, thickness[, lineType[, shift]]])`**

| Parameter    | Description                                            |
| :----------- | :----------------------------------------------------- |
| `img`        | 그림을 그릴 이미지                                     |
| `center`     | 타원의 중심 좌표 (x, y) 튜플 (예: `(256, 256)`)        |
| `axes`       | 장축/단축 길이 (튜플, 예: `(100, 50)`)                 |
| `angle`      | 타원의 기울기 각도 (반시계 방향, degree)               |
| `startAngle` | 타원 호의 시작 각도 (시계 방향, degree)                |
| `endAngle`   | 타원 호의 종료 각도 (시계 방향, degree)                |
| `color`      | BGR 색상 값 (튜플) (예: `(255, 255, 255)` - White)     |
| `thickness`  | 선 두께 (pixel 단위, 정수). `-1` 이면 타원 내부 채우기 |

**샘플 코드:**

```python
img = cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1) # White 반원 (내부 채우기)
```

</div>

---

### 3.5 다각형 그리기: `cv2.polylines()`

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

`cv2.polylines()` 함수는 여러 점을 연결하여 다각형 또는 폴리라인 (polyline) 을 그립니다.

- **`cv2.polylines(img, pts, isClosed, color, thickness)`**

| Parameter   | Description                                                                       |
| :---------- | :-------------------------------------------------------------------------------- |
| `img`       | 그림을 그릴 이미지                                                                |
| `pts`       | 꼭지점 좌표 배열 (NumPy array). shape: `(N, 1, 2)` 또는 `(N, 2)` (N: 꼭지점 개수) |
| `isClosed`  | 닫힌 도형 여부 (True: 다각형, False: 폴리라인)                                    |
| `color`     | BGR 색상 값 (튜플) (예: `(0, 255, 255)` - Yellow)                                 |
| `thickness` | 선 두께 (pixel 단위, 정수)                                                        |

**샘플 코드:**

```python
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32) # 꼭지점 좌표 (2차원 array)
pts = pts.reshape((-1, 1, 2)) # 3차원 array로 reshape (polylines() 입력 형식)
img = cv2.polylines(img, [pts], True, (0, 255, 255)) # Yellow 다각형 (닫힌 도형)
```

**Note:** `pts` 는 꼭지점 좌표를 담은 NumPy array이며, `cv2.polylines()` 함수의 입력 형식에 맞게 reshape 해야 합니다.

</div>

---

### 3.6 텍스트 추가: `cv2.putText()`

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

`cv2.putText()` 함수는 이미지에 텍스트 문자열을 추가합니다.

- **`cv2.putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])`**

| Parameter   | Description                                                        |
| :---------- | :----------------------------------------------------------------- |
| `img`       | 그림을 그릴 이미지                                                 |
| `text`      | 표시할 문자열                                                      |
| `org`       | 텍스트 시작 위치 (bottom-left corner 좌표, 튜플) (예: `(10, 500)`) |
| `fontFace`  | 폰트 종류 (OpenCV 폰트 상수, 예: `cv2.FONT_HERSHEY_SIMPLEX`)       |
| `fontScale` | 폰트 크기 (float 값)                                               |
| `color`     | 폰트 색상 (BGR 튜플) (예: `(255, 255, 255)` - White)               |
| `thickness` | 폰트 두께 (pixel 단위, 정수)                                       |

**샘플 코드:**

```python
cv2.putText(img, 'OpenCV', (10, 500), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 2) # White "OpenCV" 텍스트
```

**OpenCV 폰트 종류 (fontFace):**

- `cv2.FONT_HERSHEY_SIMPLEX` (일반적인 폰트)
- `cv2.FONT_HERSHEY_PLAIN`
- `cv2.FONT_HERSHEY_DUPLEX`
- `cv2.FONT_HERSHEY_COMPLEX`
- `cv2.FONT_HERSHEY_TRIPLEX`
- `cv2.FONT_HERSHEY_COMPLEX_SMALL`
- `cv2.FONT_HERSHEY_SCRIPT_SIMPLEX`
- `cv2.FONT_HERSHEY_SCRIPT_COMPLEX`
- `cv2.FONT_ITALIC` (이탤릭체 플래그, 다른 폰트와 함께 사용)

</div>

---

## 4. Mouse로 그리기 (Drawing with Mouse)

**Goal:**

- Mouse Event 처리 방법 학습
- `cv2.setMouseCallback()` 함수 이해

**Mouse Event 활용:**

- 사용자 인터랙티브 (Interactive) 이미지 처리 프로그램 개발
- 이미지 영역 선택, 객체 지정 등

---

### 4.1 Mouse Event 종류

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

OpenCV는 다양한 Mouse Event 종류를 미리 정의해 놓았습니다. Python Terminal에서 다음 코드를 실행하여 확인해 볼 수 있습니다.

```python
import cv2
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)
```

**주요 Mouse Event 종류:**

- `EVENT_LBUTTONDOWN`: 마우스 왼쪽 버튼 누름
- `EVENT_LBUTTONUP`: 마우스 왼쪽 버튼 떼기
- `EVENT_MOUSEMOVE`: 마우스 이동
- `EVENT_LBUTTONDBLCLK`: 마우스 왼쪽 버튼 더블 클릭
- ... (다양한 이벤트 종류 확인 가능)

</div>

---

### 4.2 `cv2.setMouseCallback()` 함수

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

`cv2.setMouseCallback()` 함수는 특정 윈도우 창에서 Mouse Event가 발생했을 때 호출될 Callback 함수를 지정합니다.

- **`cv2.setMouseCallback(windowName, callback, param=None)`**

| Parameter    | Description                                                   |
| :----------- | :------------------------------------------------------------ |
| `windowName` | Mouse Event를 감지할 윈도우 창 이름                           |
| `callback`   | Callback 함수. Mouse Event 발생 시 자동으로 호출됩니다.       |
| `param`      | Callback 함수에 전달할 추가 데이터 (Optional, 기본값: `None`) |

**Callback 함수 형식:**

```python
def draw_circle(event, x, y, flags, param):
    # event: 발생한 Mouse Event 종류 (예: cv2.EVENT_LBUTTONDOWN)
    # x, y: Mouse Cursor 좌표
    # flags: Mouse Event 발생 시 눌러진 키 (Ctrl, Shift, Alt, 마우스 버튼 등)
    # param: cv2.setMouseCallback() 함수에서 전달된 param 값
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1) # Double Click 시 원 그리기
```

</div>

---

### 4.3 간단한 Demo: Double Click으로 원 그리기

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

```python
import cv2
import numpy as np

# Callback 함수
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK: # Left Button Double Click Event
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1) # 원 그리기

# 빈 Image 생성 (검정색 배경)
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image') # 윈도우 창 생성
cv2.setMouseCallback('image', draw_circle) # Mouse Callback 함수 등록

while(1):
    cv2.imshow('image', img) # 이미지 표시
    if cv2.waitKey(20) & 0xFF == 27: # ESC 키 입력 시 종료
        break

cv2.destroyAllWindows()
```

**실행 결과:** 'image' 윈도우 창에서 마우스 왼쪽 버튼을 더블 클릭하면 클릭한 위치에 원이 그려집니다.

</div>

---

### 4.4 고급 Demo: Drag & Drop으로 사각형 또는 원 그리기

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

마우스를 누른 상태에서 이동 (Drag) 시 사각형 또는 원을 그리는 Demo 예제입니다.

**응용:**

- 객체 추적 (Object Tracking) 또는 이미지 Segmentation 시 응용 가능
- 이미지에서 관심 영역 (Region of Interest, ROI) 선택

```python
import cv2
import numpy as np

drawing = False # Mouse 클릭 상태 (False: 떼어진 상태, True: 눌린 상태)
mode = True # 도형 모드 (True: 사각형, False: 원)
ix, iy = -1, -1 # 시작점 좌표 초기화

# Mouse Callback 함수
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN: # Left Button Down Event
        drawing = True # 클릭 상태로 변경
        ix, iy = x, y # 시작점 좌표 저장

    elif event == cv2.EVENT_MOUSEMOVE: # Mouse Move Event
        if drawing == True: # 클릭 상태인 경우
            if mode == True: # 사각형 모드
                cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), -1) # 사각형 그리기
            else: # 원 모드
                cv2.circle(img, (x, y), 5, (0, 255, 0), -1) # 원 그리기

    elif event == cv2.EVENT_LBUTTONUP: # Left Button Up Event
        drawing = False # 떼어진 상태로 변경
        if mode == True: # 사각형 모드
            cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), -1) # 최종 사각형 그리기
        else: # 원 모드
            cv2.circle(img, (x, y), 5, (0, 255, 0), -1) # 최종 원 그리기

img = np.zeros((512, 512, 3), np.uint8) # 검정색 배경 이미지 생성
cv2.namedWindow('image') # 윈도우 창 생성
cv2.setMouseCallback('image', draw_circle) # Mouse Callback 함수 등록

while True:
    cv2.imshow('image', img) # 이미지 표시
    k = cv2.waitKey(1) & 0xFF # 키 입력 대기

    if k == ord('m'): # 'm' 키 입력 시 도형 모드 변경 (사각형 <-> 원)
        mode = not mode
    elif k == 27: # ESC 키 입력 시 종료
        break

cv2.destroyAllWindows()
```

**실행 결과:** 'image' 윈도우 창에서 마우스를 드래그하여 사각형 또는 원을 그릴 수 있습니다. 'm' 키를 눌러 도형 모드를 변경할 수 있습니다.

</div>

---

## 5. Trackbar

**Goal:**

- Trackbar (슬라이드 바) 와 OpenCV 연동 방법 학습
- `cv2.createTrackbar()`, `cv2.getTrackbarPos()` 함수 이해

**Trackbar 활용:**

- 이미지 처리 파라미터 (Threshold 값, Filter 크기 등) 실시간 조절
- GUI 기반 인터랙티브 프로그램 개발

---

### 5.1 Demo: RGB 값 조절 Trackbar

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

4개의 Trackbar를 사용하여 이미지 배경색 (RGB 값) 을 실시간으로 변경하는 Demo 예제입니다.

- 3개의 Trackbar: R, G, B 값 조절 (0 ~ 255 범위)
- 1개의 Trackbar: 초기화 (On/Off 스위치)

**`cv2.createTrackbar(trackbarName, windowName, value, count, onChange)`**

| Parameter      | Description                                                                                   |
| :------------- | :-------------------------------------------------------------------------------------------- |
| `trackbarName` | Trackbar 이름 (문자열)                                                                        |
| `windowName`   | Trackbar를 생성할 윈도우 창 이름                                                              |
| `value`        | Trackbar 초기 값 (정수)                                                                       |
| `count`        | Trackbar 최대 값 (최소 값은 항상 0)                                                           |
| `onChange`     | Slide Bar 값이 변경될 때 호출될 Callback 함수. 함수는 Trackbar Position 값을 인자로 받습니다. |

**`cv2.getTrackbarPos(trackbarName, windowName)`**

| Parameter      | Description                      |
| :------------- | :------------------------------- |
| `trackbarName` | Trackbar 이름                    |
| `windowName`   | Trackbar가 등록된 윈도우 창 이름 |
| **Return**     | Trackbar 현재 Position 값 (정수) |

</div>

---

### 5.2 샘플 코드: RGB Trackbar Demo

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

```python
import cv2
import numpy as np

def nothing(x): # Trackbar Callback 함수 (empty function)
    pass

img = np.zeros((300, 512, 3), np.uint8) # 검정색 배경 이미지 생성
cv2.namedWindow('image') # 윈도우 창 생성

# Trackbar 생성 및 윈도우 창에 등록
cv2.createTrackbar('R', 'image', 0, 255, nothing) # R 값 Trackbar
cv2.createTrackbar('G', 'image', 0, 255, nothing) # G 값 Trackbar
cv2.createTrackbar('B', 'image', 0, 255, nothing) # B 값 Trackbar

switch = '0:OFF\n1:On' # Switch Trackbar 이름
cv2.createTrackbar(switch, 'image', 1, 1, nothing) # Switch Trackbar (0 또는 1 값)

while(1):
    cv2.imshow('image', img) # 이미지 표시

    if cv2.waitKey(1) & 0xFF == 27: # ESC 키 입력 시 종료
        break

    # Trackbar 현재 Position 값 얻기
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image') # Switch Trackbar 값

    if s == 0: # Switch Off (초기화)
        img[:] = 0 # 검정색 배경으로 변경
    else: # Switch On
        img[:] = [b, g, r] # RGB 값으로 배경색 변경

cv2.destroyAllWindows()
```

**실행 결과:** 'image' 윈도우 창에 RGB Trackbar와 Switch Trackbar가 생성됩니다. Trackbar를 조작하여 이미지 배경색을 실시간으로 변경할 수 있습니다. Switch Trackbar를 Off (0) 로 설정하면 배경색이 검정색으로 초기화됩니다.

</div>

---

## 6. Basic Operation (기본 연산)

**Goal:**

- Pixel 값 접근 및 수정 방법 학습
- 이미지 기본 속성 (Shape, Size, Data Type) 확인 방법 학습
- 이미지 ROI (Region of Image, 관심 영역) 설정 및 활용 방법 학습
- 이미지 채널 분리 및 병합 방법 학습

---

### 6.1 Pixel 값 접근 및 수정

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

이미지는 3차원 NumPy 배열 형태로 표현됩니다 (높이, 너비, 채널).

**Pixel 값 접근:**

```python
import cv2
import numpy as np

img = cv2.imread('lena.jpg')

px = img[100, 200] # (100, 200) 좌표 Pixel 값 (BGR)
print(px) # 출력 예: [157 100 190] (BGR 값)

blue = img[100, 200, 0] # (100, 200) 좌표 Blue 채널 값
print(blue) # 출력 예: 157
```

**Pixel 값 수정:**

```python
img[100, 200] = [255, 255, 255] # (100, 200) 좌표 Pixel 값을 흰색으로 변경 (BGR)
```

**NumPy item() / itemset() 사용 (효율적):**

```python
red = img.item(10, 10, 2) # (10, 10) 좌표 Red 채널 값
print(red) # 출력 예: 59

img.itemset((10, 10, 2), 100) # (10, 10) 좌표 Red 채널 값을 100으로 변경
red = img.item(10, 10, 2)
print(red) # 출력 예: 100
```

</div>

---

### 6.2 이미지 기본 속성

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

이미지 데이터의 기본 정보 확인:

- **`img.shape`**: 이미지 Shape (높이, 너비, 채널)

```python
img.shape # 출력 예: (206, 207, 3) (컬러 이미지)
```

- **`img.size`**: 전체 Pixel 수

```python
img.size # 출력 예: 42642
```

- **`img.dtype`**: 이미지 Data Type

```python
img.dtype # 출력 예: dtype('uint8') (8-bit unsigned integer)
```

**Note:** Grayscale 이미지의 경우 `img.shape` 는 (높이, 너비) 만 반환합니다 (채널 정보 없음).

</div>

---

### 6.3 이미지 ROI (Region of Image, 관심 영역)

ROI는 이미지 내에서 특정 영역을 지정하여 처리하는 데 사용됩니다. NumPy Indexing을 사용하여 ROI를 설정할 수 있습니다.

**ROI 설정 및 복사 예제:**

```python
img = cv2.imread('baseball-player.jpg')

ball = img[409:454, 817:884] # ROI 설정 (야구공 영역)
img[470:515, 817:884] = ball # ROI 영역을 다른 영역에 복사

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

**실행 결과:**

[Original Image - 야구 선수 이미지]

[Result Image - 야구공 ROI 복사된 이미지]

---

### 6.4 이미지 채널 (Channels)

컬러 이미지는 B, G, R 3개의 채널로 구성됩니다. `cv2.split()` 함수를 사용하여 채널을 분리하고, `cv2.merge()` 함수를 사용하여 채널을 병합할 수 있습니다.

**채널 분리:**

```python
b, g, r = cv2.split(img) # BGR 채널 분리
```

**채널 병합:**

```python
img = cv2.merge((r, g, b)) # RGB 순서로 채널 병합
```

**NumPy Indexing으로 채널 접근 (더 효율적):**

```python
b = img[:, :, 0] # Blue 채널 접근
g = img[:, :, 1] # Green 채널 접근
r = img[:, :, 2] # Red 채널 접근
```

**채널 값 변경:**

```python
img[:, :, 2] = 0 # Red 채널 값을 0으로 설정 (Red 채널 제거 효과)
```

**Warning:** `cv2.split()` 함수는 연산 비용이 높은 함수입니다. 채널 접근 시 NumPy Indexing을 사용하는 것이 효율적입니다.

---

## 7. 이미지 연산 (Image Operations)

**Goal:**

- 이미지 덧셈, Blending (가중치 합), 비트 연산 학습
- `cv2.add()`, `cv2.addWeighted()` 함수 이해

**이미지 연산의 활용:**

- 이미지 합성 (Image Compositing)
- 이미지 개선 (Image Enhancement)
- 특정 영역 추출 (Region Extraction)

---

### 7.1 이미지 덧셈 (Image Addition)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

이미지 덧셈은 `cv2.add()` 함수 또는 NumPy 연산 (`+` 연산자) 를 사용하여 수행할 수 있습니다.

**`cv2.add(img1, img2)`**: OpenCV 덧셈 (Saturation 연산)

- Saturation 연산: 덧셈 결과가 255를 초과하면 255로, 0 미만이면 0으로 고정

**`img1 + img2`**: NumPy 덧셈 (Modulo 연산)

- Modulo 연산: 덧셈 결과가 256을 초과하면 256으로 나눈 나머지 값을 사용

**Note:** OpenCV 덧셈과 NumPy 덧셈은 연산 방식이 다르므로 결과가 다를 수 있습니다. 일반적으로 이미지 덧셈에는 `cv2.add()` 함수 (Saturation 연산) 를 사용하는 것이 적합합니다.

</div>

---

### 7.2 이미지 Blending (Blending Images)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

이미지 Blending은 두 이미지를 가중치를 적용하여 혼합하는 방법입니다.

**수학식:**

\[g(x) = (1 - \alpha)f*{0}(x) + \alpha f*{1}(x)\]

- `α` 값 (0 ~ 1): Blending 비율. `α` 가 0에 가까울수록 `f0(x)` 이미지의 비중이 높고, 1에 가까울수록 `f1(x)` 이미지의 비중이 높아집니다.

**`cv2.addWeighted(img1, alpha, img2, beta, gamma)`**: 이미지 Blending 함수

- `alpha`: `img1` 에 대한 가중치 (0 ~ 1)
- `beta`: `img2` 에 대한 가중치 (0 ~ 1)
- `gamma`: 결과 이미지에 더할 값 (offset, 일반적으로 0 사용)

**샘플 코드 (Trackbar를 이용한 Blending):**

```python
import cv2
import numpy as np

img1 = cv2.imread('images/flower1.jpg')
img2 = cv2.imread('images/flower2.jpg')

def nothing(x): # Trackbar Callback 함수 (empty function)
    pass

cv2.namedWindow('image')
cv2.createTrackbar('W', 'image', 0, 100, nothing) # W Trackbar (Blending 비율 조절)

while True:
    w = cv2.getTrackbarPos('W', 'image') # Trackbar 값 얻기

    alpha = float(100 - w) * 0.01 # img1 가중치 (0.01 ~ 1.0)
    beta = float(w) * 0.01 # img2 가중치 (0.01 ~ 1.0)

    dst = cv2.addWeighted(img1, alpha, img2, beta, 0) # 이미지 Blending

    cv2.imshow('dst', dst) # Blending 결과 이미지 표시

    if cv2.waitKey(1) & 0xFF == 27: # ESC 키 입력 시 종료
        break

cv2.destroyAllWindows()
```

**실행 결과:** 'image' 윈도우 창에 W Trackbar가 생성됩니다. Trackbar를 조작하여 두 이미지를 부드럽게 Blending 할 수 있습니다.

</div>

---

### 7.3 비트 연산 (Bitwise Operations)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

비트 연산은 이미지의 특정 영역을 추출하거나 마스크 (Mask) 를 적용하는 데 유용하게 사용됩니다. OpenCV는 AND, OR, NOT, XOR 비트 연산을 지원합니다.

- `cv2.bitwise_and(img1, img2, mask=None)`: AND 연산
- `cv2.bitwise_or(img1, img2, mask=None)`: OR 연산
- `cv2.bitwise_not(img1, mask=None)`: NOT 연산 (반전)
- `cv2.bitwise_xor(img1, img2, mask=None)`: XOR 연산

**샘플 코드 (OpenCV 로고 합성):**

```python
import cv2
import numpy as np

img1 = cv2.imread('images/logo.png') # OpenCV 로고 이미지
img2 = cv2.imread('images/lena.jpg') # 배경 이미지

rows, cols, channels = img1.shape # 로고 이미지 Shape

roi = img2[0:rows, 0:cols] # 배경 이미지에서 로고 이미지 영역 추출 (ROI)

# 로고 이미지를 GrayScale로 변환 후 Binary 이미지로 변환 (Mask 생성)
img2gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY) # Thresholding (Binary Mask)
mask_inv = cv2.bitwise_not(mask) # Mask 반전 (Inverse Mask)

# Bitwise AND 연산: Mask를 이용하여 로고 이미지에서 전경 (Logo) 추출
img1_fg = cv2.bitwise_and(img1, img1, mask=mask)

# Bitwise AND 연산: 반전된 Mask를 이용하여 ROI 영역에서 배경 추출
img2_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# 전경 (Logo) 와 배경 이미지 합성
dst = cv2.add(img1_fg, img2_bg)

img2[0:rows, 0:cols] = dst # 합성된 이미지를 원본 배경 이미지에 적용

cv2.imshow('res', img2) # 최종 결과 이미지 표시
cv2.waitKey(0)
cv2.destroyAllWindows()
```

**실행 결과:**

[Result Image - OpenCV 로고가 Lena 이미지에 합성된 이미지]

**Note:** `cv2.threshold()` 함수는 이미지 임계처리에 사용되며, 다음 챕터에서 자세히 다룹니다.

</div>

---

## 8. 이미지 Processing (처리) - 이미지 임계처리 (Image Thresholding)

**Goal:**

- 이미지 이진화 (Image Binarization) 방법 학습:
  - 기본 임계처리 (Simple Thresholding)
  - 적응 임계처리 (Adaptive Thresholding)
  - Otsu의 이진화 (Otsu's Binarization)
- `cv2.threshold()`, `cv2.adaptiveThreshold()` 함수 이해

**이미지 임계처리 (Thresholding) 의 활용:**

- 이미지 Segmentation (영역 분할)
- 객체 검출 (Object Detection) 전처리 (Preprocessing)
- 텍스트 추출 (Text Extraction)

---

### 8.1 기본 임계처리 (Simple Thresholding)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

이미지를 흑백 (Binary) 이미지로 변환하는 가장 기본적인 방법입니다. 사용자가 임계값 (Threshold Value) 을 직접 지정합니다.

- **`cv2.threshold(src, thresh, maxval, type)`**: 기본 임계처리 함수

| Parameter  | Description                                                                                                 |
| :--------- | :---------------------------------------------------------------------------------------------------------- |
| `src`      | 입력 이미지 (GrayScale 이미지)                                                                              |
| `thresh`   | 임계값 (Threshold Value). Pixel 값이 `thresh` 값과 비교됩니다.                                              |
| `maxval`   | 임계값 조건을 만족하는 (또는 만족하지 않는) Pixel 에 적용할 최대 값 (일반적으로 255, 흰색)                  |
| `type`     | 임계처리 타입 (Thresholding Type). 임계값 조건 및 적용 방식 지정 (아래 표 참조)                             |
| **Return** | `retval` (실제 사용된 임계값, Otsu's Binarization 의 경우 자동 계산된 임계값), `dst` (임계처리 결과 이미지) |

**임계처리 타입 (Thresholding Type):**

| Type                    | `type` 상수             | Description                                                                    |
| :---------------------- | :---------------------- | :----------------------------------------------------------------------------- |
| `cv2.THRESH_BINARY`     | `cv2.THRESH_BINARY`     | Pixel 값이 `thresh` 초과: `maxval`, 이하: 0                                    |
| `cv2.THRESH_BINARY_INV` | `cv2.THRESH_BINARY_INV` | `cv2.THRESH_BINARY` 의 반대. Pixel 값이 `thresh` 초과: 0, 이하: `maxval`       |
| `cv2.THRESH_TRUNC`      | `cv2.THRESH_TRUNC`      | Pixel 값이 `thresh` 초과: `thresh` 값으로 자름 (Truncate), 이하: Pixel 값 유지 |
| `cv2.THRESH_TOZERO`     | `cv2.THRESH_TOZERO`     | Pixel 값이 `thresh` 초과: Pixel 값 유지, 이하: 0                               |
| `cv2.THRESH_TOZERO_INV` | `cv2.THRESH_TOZERO_INV` | `cv2.THRESH_TOZERO` 의 반대. Pixel 값이 `thresh` 초과: 0, 이하: Pixel 값 유지  |

**샘플 코드 (각 Type 별 임계처리 결과 비교):**

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gradient.jpg', 0) # GrayScale 이미지 로드

ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) # BINARY Thresholding
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV) # BINARY_INV Thresholding
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC) # TRUNC Thresholding
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO) # TOZERO Thresholding
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV) # TOZERO_INV Thresholding

titles = ['Original', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray') # 결과 이미지 Plot
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([]) # X, Y 축 눈금 제거

plt.show()
```

**Note:** `plt.subplot()` 함수는 Matplotlib 에서 여러 이미지를 한 화면에 표시할 때 사용됩니다.

</div>

---

### 8.2 적응 임계처리 (Adaptive Thresholding)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

기본 임계처리의 문제점: 이미지 전체에 고정된 임계값을 적용하므로, 이미지 내 밝기 변화가 심한 경우 일부 영역에서 정보 손실 발생 (전부 흰색 또는 검정색으로 표현).

**적응 임계처리:** 이미지의 작은 영역별로 임계값을 다르게 적용하여 밝기 변화에 robust 하게 처리합니다.

- **`cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)`**: 적응 임계처리 함수

| Parameter        | Description                                                                          |
| :--------------- | :----------------------------------------------------------------------------------- |
| `src`            | 입력 이미지 (GrayScale 이미지)                                                       |
| `maxValue`       | 임계값 조건을 만족하는 Pixel 에 적용할 최대 값 (일반적으로 255, 흰색)                |
| `adaptiveMethod` | 임계값 결정 방법 (아래 표 참조)                                                      |
| `thresholdType`  | 임계처리 타입 (일반적으로 `cv2.THRESH_BINARY` 또는 `cv2.THRESH_BINARY_INV` 사용)     |
| `blockSize`      | 임계값을 계산할 영역 크기 (Block Size). 홀수 값                                      |
| `C`              | 평균 또는 가중 평균 값에서 뺄 상수 값 (Bias). 영역별로 계산된 임계값을 보정하는 역할 |

**Adaptive Method:**

| Method                           | `adaptiveMethod` 상수            | Description                                                                                   |
| :------------------------------- | :------------------------------- | :-------------------------------------------------------------------------------------------- |
| `cv2.ADAPTIVE_THRESH_MEAN_C`     | `cv2.ADAPTIVE_THRESH_MEAN_C`     | 주변 영역 Pixel 값의 평균 값으로 임계값 결정                                                  |
| `cv2.ADAPTIVE_THRESH_GAUSSIAN_C` | `cv2.ADAPTIVE_THRESH_GAUSSIAN_C` | 주변 영역 Pixel 값에 Gaussian 가중치를 적용한 평균 값으로 임계값 결정. 노이즈에 더 robust 함. |

**샘플 코드 (적응 임계처리 결과 비교):**

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/dave.png', 0) # GrayScale 이미지 로드
# img = cv2.medianBlur(img, 5) # Median Filter (노이즈 제거, Optional)

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) # Global Thresholding (기본 임계처리)

th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                            cv2.THRESH_BINARY, 15, 2) # Mean Adaptive Thresholding
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                            cv2.THRESH_BINARY, 15, 2) # Gaussian Adaptive Thresholding

titles = ['Original', 'Global', 'Mean', 'Gaussian']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
```

</div>

---

### 8.3 Otsu의 이진화 (Otsu's Binarization)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Otsu의 이진화는 Bimodal Image (히스토그램에 2개의 Peak 가 있는 이미지) 에서 최적의 임계값을 자동으로 찾아주는 알고리즘입니다.

**장점:** 사용자가 임계값을 직접 지정할 필요 없이 자동으로 최적의 임계값을 찾을 수 있습니다.

**`cv2.threshold()` 함수와 `cv2.THRESH_OTSU` flag 함께 사용:**

```python
ret, th = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
```

- `thresh` parameter 값으로 `0` 을 전달합니다.
- `cv2.THRESH_OTSU` flag 를 `cv2.THRESH_BINARY` 또는 `cv2.THRESH_BINARY_INV` 와 함께 사용합니다.
- `cv2.threshold()` 함수는 `retval` 로 자동 계산된 최적 임계값을 반환합니다.

**샘플 코드 (Otsu의 이진화 결과 비교):**

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/noise.png', 0) # 노이즈 이미지 로드

# Global Thresholding (임계값: 127)
ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Otsu's Thresholding
ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Gaussian Blur + Otsu's Thresholding (노이즈 제거 후 Otsu 적용)
blur = cv2.GaussianBlur(img, (5, 5), 0) # Gaussian Blur
ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) # Otsu's Thresholding

# Plot images and histograms
images = [img, 0, th1, img, 0, th2, blur, 0, th3]
titles = ['Original Noisy Image', 'Histogram', 'Global Thresholding (v=127)',
          'Original Noisy Image', 'Histogram', "Otsu's Thresholding",
          'Gaussian filtered Image', 'Histogram', "Otsu's Thresholding"]

for i in range(3):
    plt.subplot(3, 3, i * 3 + 1), plt.imshow(images[i * 3], 'gray') # 원본 이미지 Plot
    plt.title(titles[i * 3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, i * 3 + 2), plt.hist(images[i * 3].ravel(), 256) # 히스토그램 Plot
    plt.title(titles[i * 3 + 1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, i * 3 + 3), plt.imshow(images[i * 3 + 2], 'gray') # 임계처리 결과 이미지 Plot
    plt.title(titles[i * 3 + 2]), plt.xticks([]), plt.yticks([])

plt.show()
```

**Otsu의 이진화는 노이즈가 있는 이미지에서도 효과적으로 이진화 결과를 얻을 수 있습니다.** Gaussian Blur 를 적용하여 노이즈를 제거한 후 Otsu의 이진화를 적용하면 더욱 좋은 결과를 얻을 수 있습니다.

</div>

---

## 9. 이미지의 기하학적 변형 (Geometric Transformations of Images)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

**Goal:**

- 이미지 기하학적 변형 종류 학습:
  - 이동 (Translation)
  - 확대/축소 (Scaling)
  - 회전 (Rotation)
  - Affine 변환 (Affine Transformation)
  - 원근 변환 (Perspective Transformation)
- `cv2.resize()`, `cv2.warpAffine()`, `cv2.getRotationMatrix2D()`, `cv2.getPerspectiveTransform()` 함수 이해

**기하학적 변형의 활용:**

- 이미지 정렬 (Image Alignment)
- 시점 변환 (View Transformation)
- 이미지 왜곡 보정 (Image Distortion Correction)

</div>

---

### 9.1 Transformations (변환) 개요

기하학적 변환은 이미지의 Pixel 좌표를 변환하는 연산입니다. 수학적으로는 좌표 `x` 를 좌표 `x'` 로 변환하는 함수로 표현됩니다.

**변환 종류:**

- **강체 변환 (Rigid-Body Transformation):** 크기 및 각도 보존 (Translation, Rotation)
- **유사 변환 (Similarity Transformation):** 각도 보존, 크기 변화 가능 (Scaling)
- **선형 변환 (Linear Transformation):** Vector 공간에서의 이동 (Translation 제외)
- **Affine 변환 (Affine Transformation):** 선형 변환 + 이동 변환. 직선의 평행성 유지 (사각형 -> 평행사변형)
- **원근 변환 (Perspective Transformation):** Affine 변환 + 원근 효과. 직선의 평행성 유지 X (기차길 -> 한 점에서 만나는 것처럼 보임)

---

### 9.2 Scaling (확대/축소)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

이미지 크기를 변경하는 변환입니다. `cv2.resize()` 함수를 사용합니다.

- **`cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]]`**: 이미지 크기 변경 함수

| Parameter       | Description                                                                                         |
| :-------------- | :-------------------------------------------------------------------------------------------------- |
| `src`           | 입력 이미지                                                                                         |
| `dsize`         | 수동 크기 지정 (튜플, `(width, height)` 형식). `dsize` 가 0 이면 `fx`, `fy` 값을 이용하여 자동 계산 |
| `fx`            | 가로 (width) 크기 비율 (배수). `dsize` 가 0 이면 `fx` 값 필수                                       |
| `fy`            | 세로 (height) 크기 비율 (배수). `dsize` 가 0 이면 `fy` 값 필수                                      |
| `interpolation` | 보간법 (Interpolation Method). Pixel 값 보간 방식 지정 (크기 변경 시 Pixel 값 결정 방식)            |

**주요 보간법 (Interpolation Method):**

- `cv2.INTER_AREA`: 이미지 축소 (Shrink) 시 사용. Pixel Area Relation 이용
- `cv2.INTER_CUBIC`: 이미지 확대 (Zoom In) 시 사용. Bicubic Interpolation
- `cv2.INTER_LINEAR`: 이미지 확대 (Zoom In) 시 사용. Bilinear Interpolation (기본값)

**샘플 코드 (Scaling 예제):**

```python
import cv2
import numpy as np

img = cv2.imread('images/logo.png')

height, width = img.shape[:2] # 이미지 높이, 너비

# 이미지 축소 (Shrink)
shrink = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# 수동 크기 지정 (Manual Size)
zoom1 = cv2.resize(img, (width * 2, height * 2), interpolation=cv2.INTER_CUBIC)

# 배수 크기 지정 (Scale Factor)
zoom2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

cv2.imshow('Original', img)
cv2.imshow('Shrink', shrink)
cv2.imshow('Zoom1', zoom1)
cv2.imshow('Zoom2', zoom2)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

</div>

---

### 9.3 Translation (이동)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

이미지를 특정 방향으로 이동시키는 변환입니다. `cv2.warpAffine()` 함수를 사용합니다.

- **`cv2.warpAffine(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]])`**: Affine 변환 함수 (Translation, Rotation, Scaling, Shear 등 포함)

| Parameter | Description                                                                                                              |
| :-------- | :----------------------------------------------------------------------------------------------------------------------- |
| `src`     | 입력 이미지                                                                                                              |
| `M`       | 변환 행렬 (Transformation Matrix). 2x3 float32 type NumPy array. Translation, Rotation, Scaling, Shear 등 변환 정보 포함 |
| `dsize`   | 결과 이미지 크기 (튜플, `(width, height)` 형식). `dsize` 가 `None` 이면 원본 이미지 크기와 동일                          |

**Translation 변환 행렬 (M):**

\[M = \begin{bmatrix} 1 & 0 & t_x \\ 0 & 1 & t_y \end{bmatrix}\]

- `t_x`: X축 이동 거리 (양수: 오른쪽 이동, 음수: 왼쪽 이동)
- `t_y`: Y축 이동 거리 (양수: 아래쪽 이동, 음수: 위쪽 이동)

**샘플 코드 (Translation 예제):**

```python
import cv2
import numpy as np

img = cv2.imread('images/logo.png')

rows, cols = img.shape[:2] # 이미지 높이, 너비

# Translation 변환 행렬 생성 (X축으로 10, Y축으로 20 이동)
M = np.float32([[1, 0, 10], [0, 1, 20]])

dst = cv2.warpAffine(img, M, (cols, rows)) # Affine 변환 적용

cv2.imshow('Original', img)
cv2.imshow('Translation', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

**Warning:** `dsize` 는 `(width, height)` 형식으로, width (열 수) 가 먼저, height (행 수) 가 나중에 옵니다.

</div>

---

### 9.4 Rotation (회전)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

이미지를 특정 각도만큼 회전시키는 변환입니다. `cv2.warpAffine()` 함수와 회전 변환 행렬 생성 함수인 `cv2.getRotationMatrix2D()` 를 함께 사용합니다.

- **`cv2.getRotationMatrix2D(center, angle, scale)`**: 회전 변환 행렬 생성 함수

| Parameter  | Description                                                                                                         |
| :--------- | :------------------------------------------------------------------------------------------------------------------ |
| `center`   | 회전 중심 좌표 (튜플, `(x, y)` 형식). 이미지 중심 좌표를 기준으로 회전하려면 `(cols/2, rows/2)` 사용                |
| `angle`    | 회전 각도 (Degree). 양수: 반시계 방향 회전, 음수: 시계 방향 회전                                                    |
| `scale`    | Scale Factor (크기 비율). `1` 이면 원본 크기 유지, `0.5` 이면 0.5배 축소, `2` 이면 2배 확대. 회전 후 크기 변경 가능 |
| **Return** | 회전 변환 행렬 (2x3 float32 type NumPy array)                                                                       |

**샘플 코드 (Rotation 예제):**

```python
import cv2

img = cv2.imread('images/logo.png')

rows, cols = img.shape[:2] # 이미지 높이, 너비

# Rotation 변환 행렬 생성 (이미지 중심 기준, 90도 회전, 0.5배 Scale)
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 0.5)

dst = cv2.warpAffine(img, M, (cols, rows)) # Affine 변환 적용

cv2.imshow('Original', img)
cv2.imshow('Rotation', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

</div>

---

### 9.5 Affine Transformation (Affine 변환)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Affine 변환은 직선의 평행성을 유지하면서 이미지를 변환하는 변환입니다 (Translation, Scaling, Rotation, Shear 포함). 3개의 대응점 (Matching Points) 이 주어지면 변환 행렬을 구할 수 있습니다.

- **`cv2.getAffineTransform(src, dst)`**: Affine 변환 행렬 생성 함수

| Parameter  | Description                                                                                          |
| :--------- | :--------------------------------------------------------------------------------------------------- |
| `src`      | 원본 이미지 좌표 (3개의 점, 3x2 float32 type NumPy array)                                            |
| `dst`      | 이동할 이미지 좌표 (3개의 점, 3x2 float32 type NumPy array). `src` 좌표에 대응되는 `dst` 좌표를 지정 |
| **Return** | Affine 변환 행렬 (2x3 float32 type NumPy array)                                                      |

**샘플 코드 (Affine 변환 예제):**

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/chessboard.jpg') # Chessboard 이미지 로드
rows, cols, ch = img.shape # 이미지 Shape

# 원본 이미지 좌표 (3개의 점)
pts1 = np.float32([[200, 100], [400, 100], [200, 200]])

# 이동할 이미지 좌표 (3개의 점). pts1 좌표에 대응되는 pts2 좌표를 지정
pts2 = np.float32([[200, 300], [400, 200], [200, 400]])

# pts1 좌표에 원 표시 (Affine 변환 후 이동 점 확인)
cv2.circle(img, (200, 100), 10, (255, 0, 0), -1) # Blue
cv2.circle(img, (400, 100), 10, (0, 255, 0), -1) # Green
cv2.circle(img, (200, 200), 10, (0, 0, 255), -1) # Red

M = cv2.getAffineTransform(pts1, pts2) # Affine 변환 행렬 생성

dst = cv2.warpAffine(img, M, (cols, rows)) # Affine 변환 적용

plt.subplot(121), plt.imshow(img), plt.title('image') # 원본 이미지 Plot
plt.subplot(122), plt.imshow(dst), plt.title('Affine') # Affine 변환 이미지 Plot
plt.show()
```

</div>

---

### 9.6 Perspective Transformation (원근 변환)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

원근 변환은 직선의 성질만 유지되고, 평행성은 유지되지 않는 변환입니다 (원근 효과 적용). 4개의 대응점 (Input Points & Output Points) 이 필요합니다.

- **`cv2.getPerspectiveTransform(src, dst)`**: 원근 변환 행렬 생성 함수

| Parameter  | Description                                                                                          |
| :--------- | :--------------------------------------------------------------------------------------------------- |
| `src`      | 원본 이미지 좌표 (4개의 점, 4x2 float32 type NumPy array). 좌상 -> 좌하 -> 우상 -> 우하 순서로 지정  |
| `dst`      | 이동할 이미지 좌표 (4개의 점, 4x2 float32 type NumPy array). `src` 좌표에 대응되는 `dst` 좌표를 지정 |
| **Return** | 원근 변환 행렬 (3x3 float32 type NumPy array)                                                        |

- **`cv2.warpPerspective(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]])`**: 원근 변환 적용 함수

| Parameter | Description                                                                                            |
| :-------- | :----------------------------------------------------------------------------------------------------- |
| `src`     | 입력 이미지                                                                                            |
| `M`       | 원근 변환 행렬 (3x3 float32 type NumPy array). `cv2.getPerspectiveTransform()` 함수로 생성된 행렬 사용 |
| `dsize`   | 결과 이미지 크기 (튜플, `(width, height)` 형식). `dsize` 가 `None` 이면 원본 이미지 크기와 동일        |

**샘플 코드 (원근 변환 예제):**

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/perspective.jpg') # 원근 효과 이미지 로드

# 원본 이미지 좌표 (4개의 점). 좌상 -> 좌하 -> 우상 -> 우하 순서
pts1 = np.float32([[504, 1003], [243, 1525], [1000, 1000], [1280, 1685]])

# 이동할 이미지 좌표 (4개의 점). pts1 좌표에 대응되는 pts2 좌표를 지정
pts2 = np.float32([[10, 10], [10, 1000], [1000, 10], [1000, 1000]])

# pts1 좌표에 원 표시 (Perspective 변환 후 이동 점 확인)
cv2.circle(img, (504, 1003), 20, (255, 0, 0), -1) # Blue
cv2.circle(img, (243, 1524), 20, (0, 255, 0), -1) # Green
cv2.circle(img, (1000, 1000), 20, (0, 0, 255), -1) # Red
cv2.circle(img, (1280, 1685), 20, (0, 0, 0), -1) # Black

M = cv2.getPerspectiveTransform(pts1, pts2) # Perspective 변환 행렬 생성

dst = cv2.warpPerspective(img, M, (1100, 1100)) # Perspective 변환 적용

plt.subplot(121), plt.imshow(img), plt.title('image') # 원본 이미지 Plot
plt.subplot(122), plt.imshow(dst), plt.title('Perspective') # Perspective 변환 이미지 Plot
plt.show()
```

**원근 변환을 통해 이미지의 시점을 변경하거나, 원근 왜곡을 보정할 수 있습니다.**

</div>

---

## 10. Image Smoothing (이미지 스무딩)

**Goal:**

- 이미지 Filtering (필터링) 개념 학습
- 이미지 Blurring (블러링) 종류 학습:
  - Averaging (평균 필터)
  - Gaussian Filtering (가우시안 필터)
  - Median Filtering (미디언 필터)
  - Bilateral Filtering (양방향 필터)
- 사용자 정의 Filter (Kernel) 적용 방법 학습

**Image Smoothing (Blurring) 의 활용:**

- 이미지 노이즈 제거 (Noise Reduction)
- 이미지 전처리 (Preprocessing) (예: Edge Detection 전 노이즈 제거)

---

### 10.1 Image Filtering (이미지 필터링)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

이미지 Filtering 은 Kernel (필터 행렬) 을 이용하여 이미지의 특정 주파수 성분을 강조하거나 제거하는 연산입니다.

- **주파수 (Frequency):** 이미지 밝기 변화의 빈도.

  - **고주파 (High Frequency):** 밝기 변화가 잦은 영역 (예: 경계선, 텍스처)
  - **저주파 (Low Frequency):** 밝기 변화가 적은 영역 (예: 배경, 완만한 영역)

- **Low-Pass Filter (LPF, 저주파 통과 필터):** 저주파 성분 통과, 고주파 성분 감쇠 (Blurring, 노이즈 제거)
- **High-Pass Filter (HPF, 고주파 통과 필터):** 고주파 성분 통과, 저주파 성분 감쇠 (Edge Detection, Sharpening)

- **`cv2.filter2D(src, ddepth, kernel[, dst[, anchor[, delta[, borderType]]]]`**: 일반적인 2D Convolution 필터링 함수

| Parameter | Description                                                               |
| :-------- | :------------------------------------------------------------------------ |
| `src`     | 입력 이미지                                                               |
| `ddepth`  | 결과 이미지 Depth (Data Type). `-1` 이면 입력 이미지와 동일한 Depth 사용. |
| `kernel`  | Kernel (필터 행렬). NumPy array. 필터 크기가 클수록 블러링 효과가 강해짐. |

**Kernel (필터 행렬) 예시 (5x5 Averaging Filter):**

\[K = \frac{1}{25} \begin{bmatrix} 1 & 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 1 & 1 \end{bmatrix}\]

**필터링 동작 방식:**

1. 이미지 각 Pixel 에 Kernel 을 적용합니다.
2. Kernel 윈도우 (Window) 내 Pixel 값들과 Kernel 값들을 Convolution (element-wise multiplication 후 합산) 연산합니다.
3. Convolution 연산 결과를 해당 Pixel 의 새로운 값으로 설정합니다.

**샘플 코드 (Trackbar 로 Kernel Size 조절):**

```python
import cv2
import numpy as np

def nothing(x): # Trackbar Callback 함수 (empty function)
    pass

img = cv2.imread('images/lena.jpg')

cv2.namedWindow('image')
cv2.createTrackbar('K', 'image', 1, 20, nothing) # K Trackbar (Kernel Size 조절)

while(1):
    if cv2.waitKey(1) & 0xFF == 27: # ESC 키 입력 시 종료
        break

    k = cv2.getTrackbarPos('K', 'image') # Trackbar 값 얻기

    if k == 0: # Kernel Size 가 0 이면 에러 발생 방지 (최소 1로 설정)
        k = 1

    # Kernel 생성 (k x k Averaging Filter)
    kernel = np.ones((k, k), np.float32) / (k * k)
    dst = cv2.filter2D(img, -1, kernel) # 2D Convolution 필터링 적용

    cv2.imshow('image', dst) # 필터링 결과 이미지 표시

cv2.destroyAllWindows()
```

**실행 결과:** 'image' 윈도우 창에 K Trackbar 가 생성됩니다. Trackbar 를 조절하여 Kernel Size 를 변경하면서 블러링 강도를 실시간으로 조절할 수 있습니다.

</div>

---

### 10.2 Image Blurring (이미지 블러링) 종류

Image Blurring 은 Low-Pass Filter (LPF) 를 이미지에 적용하여 고주파 성분 (경계선, 노이즈) 을 제거하는 기술입니다. OpenCV 는 4가지 블러링 방법을 제공합니다.

1. Averaging (평균 필터)
2. Gaussian Filtering (가우시안 필터)
3. Median Filtering (미디언 필터)
4. Bilateral Filtering (양방향 필터)

---

### 10.3 Averaging (평균 필터)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Box 형태의 Kernel 을 이미지에 적용한 후, Kernel Window 영역 내 Pixel 값들의 평균 값을 Kernel 중심 Pixel 에 적용하는 블러링 방식입니다. `cv2.blur()` 또는 `cv2.boxFilter()` 함수를 사용합니다.

**3x3 Averaging Filter Kernel 예시:**

\[K = \frac{1}{9} \begin{bmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{bmatrix}\]

- **`cv2.blur(src, ksize[, dst[, anchor[, borderType]]])`**: Averaging Blur 함수

| Parameter | Description                                                                                         |
| :-------- | :-------------------------------------------------------------------------------------------------- |
| `src`     | 입력 이미지 (Depth: CV_8U, CV_16U, CV_16S, CV_32F, CV_64F)                                          |
| `ksize`   | Kernel Size (튜플, `(width, height)` 형식). Kernel 크기가 클수록 블러링 효과가 강해짐. 양수 홀수 값 |

**Note:** OpenCV 이미지 Data Type (Depth) 종류:

- `CV_8U`: 8-bit unsigned integer (0 ~ 255)
- `CV_8S`: 8-bit signed integer (-128 ~ 127)
- `CV_16U`: 16-bit unsigned integer (0 ~ 65535)
- `CV_16S`: 16-bit signed integer (-32768 ~ 32767)
- `CV_32S`: 32-bit signed integer (-2147483648 ~ 2147483647)
- `CV_32F`: 32-bit floating-point number (-FLT_MAX ~ FLT_MAX, INF, NAN)
- `CV_64F`: 64-bit floating-point number (-DBL_MAX ~ DBL_MAX, INF, NAN)

일반적으로 이미지 Data Type 과 채널 수 (Channels) 를 함께 표현하여 `CV_8UC1` (8-bit unsigned integer, 1 channel - Grayscale), `CV_8UC3` (8-bit unsigned integer, 3 channels - Color) 와 같이 사용합니다.

</div>

---

### 10.4 Gaussian Filtering (가우시안 필터)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Gaussian Filter 는 Kernel 행렬 값을 Gaussian 함수 (가우시안 분포 함수) 를 이용하여 생성하는 필터입니다. Kernel 중심에 가까울수록 가중치가 높고, 멀어질수록 가중치가 낮아집니다. Gaussian Noise (백색 노이즈) 제거에 효과적입니다.

- **`cv2.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]])`**: Gaussian Blur 함수

| Parameter | Description                                                                                                                                                  |
| :-------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `src`     | 입력 이미지 (Depth: CV_8U, CV_16U, CV_16S, CV_32F, CV_64F)                                                                                                   |
| `ksize`   | Kernel Size (튜플, `(width, height)` 형식). Width 와 Height 는 서로 다를 수 있지만, 양수 홀수 값으로 지정해야 함. Kernel 크기가 클수록 블러링 효과가 강해짐. |
| `sigmaX`  | X 방향 Gaussian Kernel 표준 편차 (Standard Deviation). 0 이면 `ksize` 로부터 자동 계산됨.                                                                    |
| `sigmaY`  | Y 방향 Gaussian Kernel 표준 편차 (Standard Deviation). 0 이면 `sigmaX` 와 동일하게 설정됨.                                                                   |

</div>

---

### 10.5 Median Filtering (미디언 필터)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Median Filter 는 Kernel Window 영역 내 Pixel 값들을 정렬한 후, 중간 값 (Median Value) 을 선택하여 Kernel 중심 Pixel 에 적용하는 블러링 방식입니다. Salt-and-Pepper Noise (소금-후추 노이즈) 제거에 효과적입니다.

**Median Filtering 동작 방식 예시:**

Kernel Window 영역 내 Pixel 값들이 다음과 같다고 가정합니다:

\[\begin{bmatrix} 33 & 54 & 67 \\ 84 & 189 & 224 \\ 102 & 163 & 212 \end{bmatrix}\]

Pixel 값들을 크기 순으로 정렬: `33, 54, 67, 84, 102, 163, 189, 212, 224`

중간 값 (Median Value) 은 `102` 입니다 (9개 값 중 5번째 값). Kernel 중심 Pixel 값 `189` 가 중간 값 `102` 로 변경됩니다.

- **`cv2.medianBlur(src, ksize[, dst]])`**: Median Blur 함수

| Parameter | Description                                                                                                                                              |
| :-------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `src`     | 입력 이미지 (1, 3, 4 채널 이미지. Depth: CV_8U, CV_16U, CV_32F). Depth 가 CV_8U, CV_16U, CV_32F 이면 `ksize` 는 3 또는 5, CV_8U 이면 더 큰 `ksize` 가능. |
| `ksize`   | Kernel Size (정사각형 Kernel). 1 보다 큰 홀수 값. Kernel 크기가 클수록 블러링 효과가 강해짐.                                                             |

</div>

---

### 10.6 Bilateral Filtering (양방향 필터)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Bilateral Filter 는 경계선 (Edge) 을 보존하면서 Gaussian Blur 를 적용하는 블러링 방식입니다. Gaussian Filter 와 유사하지만, 주변 Pixel 과의 색상 유사성 (Color Similarity) 까지 고려하여 블러링 강도를 조절합니다. 경계선 부근에서는 블러링을 약하게 적용하고, 평탄한 영역에서는 블러링을 강하게 적용합니다.

- **`cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace[, dst[, borderType]]])`**: Bilateral Filter 함수

| Parameter    | Description                                                                                                                                                                               |
| :----------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `src`        | 입력 이미지 (8-bit, 1 또는 3 채널 이미지)                                                                                                                                                 |
| `d`          | 필터링 시 고려할 주변 Pixel 지름 (Diameter). 값이 클수록 연산량이 증가하지만, 넓은 영역을 고려하여 블러링 효과가 강해짐. 음수 값 (예: -1) 이면 `sigmaSpace` 값에 의해 자동 결정됨.        |
| `sigmaColor` | Color Gaussian Filter 의 표준 편차 (Standard Deviation). 색 공간 (Color Space) 에서의 가우시안 필터의 σ 값. 값이 클수록 넓은 범위의 색상을 유사한 색상으로 간주하고 블러링 강도가 강해짐. |
| `sigmaSpace` | Space Gaussian Filter 의 표준 편차 (Standard Deviation). 좌표 공간 (Coordinate Space) 에서의 가우시안 필터의 σ 값. 값이 클수록 멀리 있는 Pixel 도 고려하여 블러링 강도가 강해짐.          |

**샘플 코드 (블러링 방법 비교):**

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/lena.jpg')

# Matplotlib 출력을 위해 BGR -> RGB 변환
b, g, r = cv2.split(img)
img_rgb = cv2.merge([r, g, b])

# Averaging Blur (평균 필터)
dst1 = cv2.blur(img_rgb, (7, 7)) # 7x7 Kernel

# Gaussian Blur (가우시안 필터)
dst2 = cv2.GaussianBlur(img_rgb, (5, 5), 0) # 5x5 Kernel, sigmaX = 0 (자동 계산)

# Median Blur (미디언 필터)
dst3 = cv2.medianBlur(img_rgb, 9) # 9x9 Kernel

# Bilateral Filtering (양방향 필터)
dst4 = cv2.bilateralFilter(img_rgb, 9, 75, 75) # d=9, sigmaColor=75, sigmaSpace=75

images = [img_rgb, dst1, dst2, dst3, dst4]
titles = ['Original', 'Blur(7x7)', 'Gaussian Blur(5x5)', 'Median Blur', 'Bilateral']

for i in range(5):
    plt.subplot(3, 2, i + 1), plt.imshow(images[i]), plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
```

**확대하여 보면 Gaussian Blur 와 Bilateral Filter 의 경계선 보존 성능 차이를 확인할 수 있습니다.** Bilateral Filter 는 경계선을 유지하면서 노이즈를 제거하는 데 효과적입니다.

</div>

---

## 11. Morphological Transformations (형태학적 변환)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

**Goal:**

- 형태학적 변환 (Morphological Transformation) 종류 학습:
  - Erosion (침식)
  - Dilation (팽창)
  - Opening (열림 연산) & Closing (닫힘 연산)
- Structuring Element (구조 요소, Kernel) 개념 학습
- `cv2.erode()`, `cv2.dilate()`, `cv2.morphologyEx()` 함수 이해

**형태학적 변환의 활용:**

- 이미지 Segmentation (영역 분할)
- 노이즈 제거 (Noise Removal)
- 객체 분리 (Object Separation)
- 객체 특징 추출 (Feature Extraction)

</div>

---

### 11.1 Theory (이론)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Morphological Transformation 은 이미지의 형태 (Shape) 를 분석하고 단순화, 제거, 보정하는 데 사용되는 이미지 처리 기법입니다. 주로 Binary 이미지 또는 GrayScale 이미지에 적용됩니다.

**주요 연산:**

- **Erosion (침식):** 이미지의 경계 부분을 깎아내는 연산. 작은 객체 제거, 객체 분리에 효과적
- **Dilation (팽창):** 이미지의 경계 부분을 확장하는 연산. 작은 구멍 채우기, 객체 연결에 효과적
- **Opening (열림 연산):** Erosion 후 Dilation 적용. 작은 객체 또는 돌기 제거에 효과적 (노이즈 제거)
- **Closing (닫힘 연산):** Dilation 후 Erosion 적용. 객체 내부의 작은 구멍 채우기, 객체 윤곽 부드럽게 만들기에 효과적

**Input:**

1. **원본 이미지 (Input Image)**
2. **Structuring Element (구조 요소, Kernel)**: 원본 이미지에 적용되는 작은 모양의 Kernel. Kernel 모양과 크기에 따라 형태학적 변환 결과가 달라집니다.

**Structuring Element 종류:**

- 사각형 (Rectangle)
- 타원형 (Ellipse)
- 십자형 (Cross)

</div>

---

### 11.2 Erosion (침식)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Erosion 은 Structuring Element (Kernel) 을 이용하여 이미지의 경계 부분을 깎아내는 연산입니다. Kernel 을 이미지 전체 영역에 Sliding 하면서 Kernel 영역 내에서 Foreground Pixel (흰색) 이 하나라도 없으면 중심 Pixel 을 Background Pixel (검정색) 으로 변경합니다.

**Erosion 효과:**

- 작은 객체 제거
- 객체 크기 축소
- 객체 분리 (객체 사이 간격 넓히기)
- 이미지 경계 부분 깎아내기

**`cv2.erode(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]])`**: Erosion 연산 함수

| Parameter    | Description                                                                   |
| :----------- | :---------------------------------------------------------------------------- |
| `src`        | 입력 이미지 (Depth: CV_8U, CV_16U, CV_16S, CV_32F, CV_64F)                    |
| `kernel`     | Structuring Element (Kernel). `cv2.getStructuringElement()` 함수로 생성 가능. |
| `anchor`     | Kernel 중심점 (Anchor Point). 기본값: `(-1, -1)` (Kernel 중심)                |
| `iterations` | Erosion 반복 횟수. 반복 횟수가 많을수록 Erosion 효과가 강해짐.                |

**Erosion 동작 방식 (십자형 Structuring Element 예시):**

</div>

---

### 11.3 Dilation (팽창)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Dilation 은 Erosion 과 반대로 Structuring Element (Kernel) 을 이용하여 이미지의 경계 부분을 확장하는 연산입니다. Kernel 을 이미지 전체 영역에 Sliding 하면서 Kernel 영역 내에서 Foreground Pixel (흰색) 이 하나라도 있으면 중심 Pixel 을 Foreground Pixel (흰색) 으로 변경합니다.

**Dilation 효과:**

- 작은 구멍 채우기
- 객체 크기 확장
- 객체 연결 (객체 사이 간격 좁히기)
- 이미지 경계 부분 확장

**`cv2.dilate(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]])`**: Dilation 연산 함수

| Parameter    | Description                                                                   |
| :----------- | :---------------------------------------------------------------------------- |
| `src`        | 입력 이미지 (Depth: CV_8U, CV_16U, CV_16S, CV_32F, CV_64F)                    |
| `kernel`     | Structuring Element (Kernel). `cv2.getStructuringElement()` 함수로 생성 가능. |
| `anchor`     | Kernel 중심점 (Anchor Point). 기본값: `(-1, -1)` (Kernel 중심)                |
| `iterations` | Dilation 반복 횟수. 반복 횟수가 많을수록 Dilation 효과가 강해짐.              |

**Dilation 동작 방식 (십자형 Structuring Element 예시):**

</div>

---

### 11.4 Opening & Closing (열림 & 닫힘 연산)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Opening 과 Closing 은 Erosion 과 Dilation 을 조합한 연산입니다. 연산 순서에 따라 효과가 달라집니다.

- **Opening (열림 연산): Erosion -> Dilation 순서**

  - 효과: 작은 객체 또는 돌기 제거, 노이즈 제거, 객체 분리
  - `cv2.MORPH_OPEN` flag 사용

- **Closing (닫힘 연산): Dilation -> Erosion 순서**

  - 효과: 객체 내부의 작은 구멍 채우기, 객체 윤곽 부드럽게 만들기, 객체 연결
  - `cv2.MORPH_CLOSE` flag 사용

- **`cv2.morphologyEx(src, op, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]])`**: Morphological Transformation 함수 (Opening, Closing, Gradient, Top Hat, Black Hat 등 다양한 연산 지원)

| Parameter    | Description                                                                   |
| :----------- | :---------------------------------------------------------------------------- |
| `src`        | 입력 이미지 (Depth: CV_8U, CV_16U, CV_16S, CV_32F, CV_64F)                    |
| `op`         | Morphological 연산 종류 (아래 표 참조)                                        |
| `kernel`     | Structuring Element (Kernel). `cv2.getStructuringElement()` 함수로 생성 가능. |
| `anchor`     | Kernel 중심점 (Anchor Point). 기본값: `(-1, -1)` (Kernel 중심)                |
| `iterations` | Erosion 및 Dilation 반복 횟수.                                                |

**Morphological 연산 종류 (`op` Parameter):**

| 연산 종류              | `op` 상수            | Description                                                                                               |
| :--------------------- | :------------------- | :-------------------------------------------------------------------------------------------------------- |
| Opening (열림 연산)    | `cv2.MORPH_OPEN`     | Erosion 후 Dilation 적용. 작은 객체 또는 돌기 제거                                                        |
| Closing (닫힘 연산)    | `cv2.MORPH_CLOSE`    | Dilation 후 Erosion 적용. 객체 내부의 작은 구멍 채우기                                                    |
| Morphological Gradient | `cv2.MORPH_GRADIENT` | Dilation 과 Erosion 결과의 차이. 객체 경계선 추출                                                         |
| Top Hat                | `cv2.MORPH_TOPHAT`   | Opening 연산 결과와 원본 이미지의 차이. 원본 이미지에서 Opening 으로 제거된 작은 객체 또는 돌기 성분 추출 |
| Black Hat              | `cv2.MORPH_BLACKHAT` | Closing 연산 결과와 원본 이미지의 차이. Closing 으로 채워진 작은 구멍 성분 추출                           |

</div>

---

### 11.5 Structuring Element (구조 요소, Kernel)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Structuring Element (Kernel) 은 형태학적 변환 연산의 핵심 요소입니다. Kernel 의 모양과 크기에 따라 연산 결과가 달라집니다.

**Structuring Element 생성 함수: `cv2.getStructuringElement(shape, ksize[, anchor])`**

| Parameter | Description                                                    |
| :-------- | :------------------------------------------------------------- |
| `shape`   | Kernel 모양 (아래 표 참조)                                     |
| `ksize`   | Kernel 크기 (튜플, `(width, height)` 형식). 양수 홀수 값       |
| `anchor`  | Kernel 중심점 (Anchor Point). 기본값: `(-1, -1)` (Kernel 중심) |

**Kernel 모양 (`shape` Parameter):**

| 모양               | `shape` 상수        | Description        |
| :----------------- | :------------------ | :----------------- |
| 사각형 (Rectangle) | `cv2.MORPH_RECT`    | 사각형 모양 Kernel |
| 타원형 (Ellipse)   | `cv2.MORPH_ELLIPSE` | 타원형 모양 Kernel |
| 십자형 (Cross)     | `cv2.MORPH_CROSS`   | 십자형 모양 Kernel |

**NumPy 를 이용한 사각형 Kernel 생성 (직접 생성):**

```python
import numpy as np
kernel = np.ones((5, 5), np.uint8) # 5x5 사각형 Kernel (모든 요소 값이 1)
```

**`cv2.getStructuringElement()` 함수를 이용한 다양한 모양의 Kernel 생성:**

```python
kernel_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)) # 5x5 사각형 Kernel
kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)) # 5x5 타원형 Kernel
kernel_cross = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5)) # 5x5 십자형 Kernel
```

</div>

---

### 11.6 샘플 코드 (Morphological Transformation 비교)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt

dotImage = cv2.imread('images/dot_image.png', cv2.IMREAD_GRAYSCALE) # 점 노이즈 이미지 (GrayScale)
holeImage = cv2.imread('images/hole_image.png', cv2.IMREAD_GRAYSCALE) # 구멍 노이즈 이미지 (GrayScale)
orig = cv2.imread('images/morph_origin.png', cv2.IMREAD_GRAYSCALE) # 원본 이미지 (GrayScale)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)) # 5x5 사각형 Kernel
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)) # 5x5 타원형 Kernel
# kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5)) # 5x5 십자형 Kernel

# Erosion 연산 (점 노이즈 제거)
erosion = cv2.erode(dotImage, kernel, iterations=1)

# Dilation 연산 (구멍 노이즈 채우기)
dilation = cv2.dilate(holeImage, kernel, iterations=1)

# Opening 연산 (점 노이즈 제거)
opening = cv2.morphologyEx(dotImage, cv2.MORPH_OPEN, kernel)

# Closing 연산 (구멍 노이즈 채우기)
closing = cv2.morphologyEx(holeImage, cv2.MORPH_CLOSE, kernel)

# Morphological Gradient (경계선 추출)
gradient = cv2.morphologyEx(orig, cv2.MORPH_GRADIENT, kernel)

# Top Hat (원본 - Opening, 작은 객체/돌기 추출)
tophat = cv2.morphologyEx(orig, cv2.MORPH_TOPHAT, kernel)

# Black Hat (Closing - 원본, 작은 구멍 추출)
blackhat = cv2.morphologyEx(orig, cv2.MORPH_BLACKHAT, kernel)

images = [dotImage, erosion, opening, holeImage, dilation, closing, gradient, tophat, blackhat]
titles = ['Dot Image', 'Erosion', 'Opening', 'Hole Image', 'Dilation', 'Closing', 'Gradient', 'Tophat', 'Blackhot']

for i in range(9):
    plt.subplot(3, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
```

</div>

---

## 12. Image Gradients (이미지 기울기)

**Goal:**

- Edge Detection (경계선 검출) 개념 학습
- Image Gradient 기반 Edge Detection 방법 학습:
  - Sobel & Scharr Filter
  - Laplacian 함수
  - Canny Edge Detection
- `cv2.Sobel()`, `cv2.Scharr()`, `cv2.Laplacian()`, `cv2.Canny()` 함수 이해

**Image Gradients (이미지 기울기) 의 활용:**

- Edge Detection (경계선 검출)
- 객체 검출 (Object Detection)
- Feature Extraction (특징 추출)

---

### 12.1 Gradient (기울기) 개념

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Gradient (기울기) 는 스칼라장 (Scalar Field, 공간) 에서 최대 증가율을 나타내는 벡터장 (Vector Field, 방향과 크기) 입니다. 이미지 처리에서 Gradient 는 이미지 밝기 변화율 (Intensity Change Rate) 을 의미하며, Edge (경계선) 검출에 활용됩니다.

**이미지 Gradient:**

- 이미지 (x, y) 좌표에서 벡터 값 (크기 및 방향) 을 계산하여 해당 Pixel 이 Edge 에 얼마나 가까운지, Edge 방향이 어디인지 정보를 제공합니다.
- 이미지 밝기 변화가 큰 영역 (Edge) 에서는 Gradient 크기가 크고, 변화가 작은 영역 (평탄한 영역) 에서는 Gradient 크기가 작습니다.

**Edge Detection (경계선 검출):**

- Image Gradient 를 이용하여 이미지에서 Edge (경계선) 을 찾아내는 기술입니다.
- Edge 는 이미지 내에서 밝기, 색상, 텍스처 등 속성이 급격하게 변하는 부분입니다.

</div>

---

### 12.2 Sobel & Scharr Filter

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Sobel Filter 와 Scharr Filter 는 Gaussian Smoothing 과 미분 (Differentiation) 을 이용하여 Edge 를 검출하는 방법입니다. 노이즈 (Noise) 에 강하고, X축 및 Y축 방향 Edge 를 각각 검출할 수 있습니다.

- **미분 (Differentiation):** 직선 미분 -> 상수, 곡선 미분 -> 방정식. Edge 영역 (밝기 급격한 변화) 을 미분하여 경계선 강조 효과를 얻습니다.

- **X축 미분 (Horizontal Derivative):** 수평 방향 Edge (수직선 강조) 검출
- **Y축 미분 (Vertical Derivative):** 수직 방향 Edge (수평선 강조) 검출

- **`cv2.Sobel(src, ddepth, dx, dy[, dst[, ksize[, scale[, delta[, borderType]]]]])`**: Sobel Filter 함수

| Parameter | Description                                                                                                                                                                               |
| :-------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `src`     | 입력 이미지                                                                                                                                                                               |
| `ddepth`  | 결과 이미지 Depth (Data Type). `-1` 이면 입력 이미지와 동일한 Depth 사용. `cv2.CV_8U` 는 Overflow 발생 가능성 있으므로 `cv2.CV_16S`, `cv2.CV_32F`, `cv2.CV_64F` 등 더 큰 Depth 사용 권장. |
| `dx`      | X축 미분 차수 (Derivative Order). 0, 1, 2 중 하나 선택.                                                                                                                                   |
| `dy`      | Y축 미분 차수 (Derivative Order). 0, 1, 2 중 하나 선택.                                                                                                                                   |
| `ksize`   | Kernel Size (Sobel Kernel 크기). 1, 3, 5, 7 또는 `cv2.FILTER_SCHARR` (3x3 Scharr Filter) 사용. `-1` 이면 3x3 Scharr Filter 적용. Kernel 크기가 클수록 Edge 가 두꺼워짐.                   |

- **`cv2.Scharr(src, ddepth, dx, dy[, dst[, scale[, delta[, borderType]]]]])`**: Scharr Filter 함수

- `cv2.Sobel()` 함수와 유사하지만, 3x3 Kernel 에서 Sobel Filter 보다 더 정확한 Edge 검출 결과를 제공합니다. `ksize = cv2.FILTER_SCHARR` 또는 `ksize = -1` 로 지정하여 사용합니다.

</div>

---

### 12.3 Laplacian 함수

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Laplacian 함수는 이미지의 가로 (X축) 및 세로 (Y축) 방향 Gradient 를 2차 미분한 값입니다. Sobel Filter 에 미분 정도를 더한 것과 유사합니다 (Sobel Filter 에서 `dx = 2`, `dy = 2` 인 경우). Blob (주변 Pixel 과 확연한 차이를 나타내는 덩어리) 검출에 주로 사용됩니다.

- **`cv2.Laplacian(src, ddepth[, dst[, ksize[, scale[, delta[, borderType]]]]])`**: Laplacian Filter 함수

| Parameter | Description                                                                                                                                                                               |
| :-------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `src`     | 입력 이미지                                                                                                                                                                               |
| `ddepth`  | 결과 이미지 Depth (Data Type). `-1` 이면 입력 이미지와 동일한 Depth 사용. `cv2.CV_8U` 는 Overflow 발생 가능성 있으므로 `cv2.CV_16S`, `cv2.CV_32F`, `cv2.CV_64F` 등 더 큰 Depth 사용 권장. |
| `ksize`   | Kernel Size (Laplacian Kernel 크기). 양수 홀수 값. 기본값: 1 (3x3 Kernel). Kernel 크기가 클수록 Edge 가 두꺼워짐.                                                                         |

</div>

---

### 12.4 Canny Edge Detection

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Canny Edge Detection 은 가장 널리 사용되는 Edge Detection 알고리즘입니다. 여러 단계의 알고리즘을 거쳐 정확한 Edge 를 검출합니다.

**Canny Edge Detection 단계:**

1. **Noise Reduction (노이즈 제거):** 5x5 Gaussian Filter 를 이용하여 이미지 노이즈를 제거합니다.
2. **Edge Gradient Detection (Edge Gradient 검출):** 이미지 Gradient 의 크기 (Magnitude) 와 방향 (Direction) 을 계산합니다. Edge 후보군 선별.
3. **Non-maximum Suppression (비최대 억제):** Edge 가 아닌 Pixel 을 제거합니다. Edge 방향에 수직인 방향으로 Gradient 크기가 최대인 Pixel 만 Edge 후보로 남기고 나머지는 제거합니다.
4. **Hysteresis Thresholding (Hysteresis 임계값 처리):** Edge 후보 Pixel 들을 실제 Edge 로 최종 판별합니다. `threshold1` (minVal) 과 `threshold2` (maxVal) 두 개의 임계값을 사용합니다.
   - **Strong Edge:** `maxVal` 이상의 Gradient 크기를 갖는 Pixel. 확실한 Edge 로 판별.
   - **Weak Edge:** `minVal` 과 `maxVal` 사이의 Gradient 크기를 갖는 Pixel. Strong Edge 와 연결되어 있으면 Edge 로 판별, 그렇지 않으면 제거.

- **`cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]])`**: Canny Edge Detection 함수

| Parameter      | Description                                                                                                                                   |
| :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| `image`        | 입력 이미지 (8-bit, GrayScale 이미지)                                                                                                         |
| `threshold1`   | Hysteresis Thresholding 의 Min Value (`minVal`). 약한 Edge 후보 Pixel 판별에 사용                                                             |
| `threshold2`   | Hysteresis Thresholding 의 Max Value (`maxVal`). 강한 Edge Pixel 판별 및 Weak Edge 판별 기준에 사용. 일반적으로 `threshold1` 보다 큰 값 사용. |
| `apertureSize` | Sobel Filter Kernel Size. 기본값: 3 (3x3 Kernel).                                                                                             |
| `L2gradient`   | Gradient 계산 방식. `True`: L2 Norm (정확하지만 연산량 증가), `False`: L1 Norm (빠르지만 정확도 감소). 기본값: `False`.                       |

**샘플 코드 (Edge Detection 방법 비교):**

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/dave.png')

# Canny Edge Detection
canny = cv2.Canny(img, 30, 70) # threshold1=30, threshold2=70

# Laplacian Filter
laplacian = cv2.Laplacian(img, cv2.CV_8U)

# Sobel Filter (X축, Y축 Edge 검출)
sobelx = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=3) # X축 미분
sobely = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=3) # Y축 미분

images = [img, laplacian, sobelx, sobely, canny]
titles = ['Original', 'Laplacian', 'Sobel X', 'Sobel Y', 'Canny']

for i in range(5):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], cmap='gray') # GrayScale 이미지 출력
    plt.title([titles[i]])
    plt.xticks([]), plt.yticks([])

plt.show()
```

**Canny Edge Detection 은 다른 Edge Detection 방법들에 비해 더 선명하고 깨끗한 Edge 검출 결과를 제공합니다.**

</div>

---

## 13. Image Pyramids (이미지 피라미드)

**Goal:**

- Image Pyramid (이미지 피라미드) 개념 학습
- Gaussian Pyramid (가우시안 피라미드) 와 Laplacian Pyramid (라플라시안 피라미드) 이해
- `cv2.pyrUp()`, `cv2.pyrDown()` 함수 이해

---

**Image Pyramids (이미지 피라미드) 의 활용:**

- Multi-Scale Image Processing (다중 스케일 이미지 처리)
- Object Detection (객체 검출) (Multi-Scale Object Detection)
- Image Blending (이미지 Blending)
- Image Segmentation (이미지 Segmentation)

---

### 13.1 Theory (이론)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Image Pyramid (이미지 피라미드) 는 하나의 원본 이미지에 대해 서로 다른 해상도 (Resolution) 를 갖는 이미지 Set 입니다. 피라미드 형태처럼 가장 아래층 (Base Level) 에 가장 높은 해상도 (원본 이미지) 를 놓고, 위로 올라갈수록 해상도를 점진적으로 낮춰서 쌓아 올린 형태입니다.

**Image Pyramid 종류:**

1. **Gaussian Pyramid (가우시안 피라미드):** 이미지 Downsampling (해상도 감소) 을 통해 생성. Low-Pass Filter (Gaussian Filter) 와 Downsampling 을 반복적으로 적용하여 이미지 크기를 점진적으로 줄여나갑니다.
2. **Laplacian Pyramid (라플라시안 피라미드):** Gaussian Pyramid 로부터 생성. Gaussian Pyramid Level 간의 차이 (Difference) 를 이용하여 이미지의 Edge 정보 (High Frequency) 를 추출합니다.

**Gaussian Pyramid:**

- **`cv2.pyrDown(src[, dst[, dstsize[, borderType]]])`**: 이미지 Downsampling 함수 (Gaussian Pyramid Level 생성). 이미지 크기를 1/4 배로 줄입니다 (가로, 세로 각각 1/2 배).
- **`cv2.pyrUp(src[, dst[, dstsize[, borderType]]])`**: 이미지 Upsampling 함수 (Gaussian Pyramid Level 확장). 이미지 크기를 4배로 늘립니다 (가로, 세로 각각 2배).

**Laplacian Pyramid:**

- Gaussian Pyramid Level 간의 차이 (Difference) 를 계산하여 생성됩니다.

**샘플 코드 (Gaussian Pyramid 생성 및 확인):**

```python
import cv2

img = cv2.imread('images/lena.jpg')

lower_reso = cv2.pyrDown(img) # 원본 이미지 1/4 크기 (해상도 감소)
higher_reso = cv2.pyrUp(img) # 원본 이미지 4배 크기 (해상도 증가)

cv2.imshow('img', img)
cv2.imshow('lower', lower_reso)
cv2.imshow('higher', higher_reso)

cv2.waitKey(0)

cv2.destroyAllWindows()
```

**`cv2.pyrDown()` 함수는 이미지 크기를 1/4 배로 줄이고, `cv2.pyrUp()` 함수는 이미지 크기를 4배로 늘립니다.**

</div>

---

**Laplacian Pyramid 예제 (외곽선 추출):**

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

```python
import cv2

img = cv2.imread('lena.jpg')

GAD = cv2.pyrDown(img) # Gaussian Pyramid Downsampling
GAU = cv2.pyrUp(GAD) # Gaussian Pyramid Upsampling

temp = cv2.resize(GAU, (img.shape[1], img.shape[0])) # Upsampled 이미지 크기를 원본 이미지 크기로 Resize
res = cv2.subtract(img, temp) # 원본 이미지 - Upsampled 이미지 (Laplacian Pyramid Level)

cv2.imshow('Laplacian Pyramid', res) # Laplacian Pyramid Level 이미지 표시
cv2.waitKey(0)
cv2.destroyAllWindows()
```

**Laplacian Pyramid Level 은 이미지의 외곽선 (Edge) 정보 (고주파 성분) 를 담고 있습니다.**

</div>

---

### 13.2 이미지 Blending with Image Pyramids (이미지 피라미드를 이용한 Blending)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Image Pyramid 를 이용하여 이미지 Blending 을 자연스럽게 처리할 수 있습니다. Laplacian Pyramid 를 이용하여 이미지 경계면을 부드럽게 Blend 하고, Gaussian Pyramid 를 이용하여 이미지 크기를 점진적으로 줄여나가면서 Blending 을 수행합니다.

**이미지 Blending with Image Pyramids 단계:**

1. 두 개의 원본 이미지 (Image A, Image B) 를 Load 합니다.
2. 각 이미지에 대해 Gaussian Pyramid 를 생성합니다 (점점 작아지는 피라미드).
3. Gaussian Pyramid 를 이용하여 Laplacian Pyramid 를 생성합니다.
4. 각 Level 의 Laplacian Pyramid 를 이용하여 이미지의 좌측 (Image A) 과 우측 (Image B) 영역을 결합 (Blend) 합니다.
5. 결합된 결과 이미지 중 가장 작은 이미지 (Base Level) 부터 Upsampling 하면서 상위 Level 의 결합 결과와 Add (덧셈) 연산하여 외곽선을 선명하게 처리합니다.

**샘플 코드 (Image Blending with Image Pyramids):**

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt

# 1단계: 이미지 로드
A = cv2.imread('images/apple.jpg') # Image A (사과)
B = cv2.imread('images/orange.jpg') # Image B (오렌지)

# 2단계: Gaussian Pyramid 생성 (Image A)
G = A.copy()
gpA = [G]
for i in range(6): # 6 Levels Gaussian Pyramid
    G = cv2.pyrDown(G)
    gpA.append(G)

# 2단계: Gaussian Pyramid 생성 (Image B)
G = B.copy()
gpB = [G]
for i in range(6): # 6 Levels Gaussian Pyramid
    G = cv2.pyrDown(G)
    gpB.append(G)

# 3단계: Laplacian Pyramid 생성 (Image A)
lpA = [gpA[5]] # Base Level Laplacian Pyramid = Gaussian Pyramid Level 6
for i in range(5, 0, -1): # Level 5 부터 Level 1 까지 Laplacian Pyramid 생성
    GE = cv2.pyrUp(gpA[i]) # Gaussian Pyramid Level i Upsampling
    temp = cv2.resize(gpA[i - 1], (GE.shape[1], GE.shape[0])) # Upsampling 이미지 크기를 Gaussian Pyramid Level i-1 크기로 Resize
    L = cv2.subtract(temp, GE) # Laplacian Pyramid Level i = Gaussian Pyramid Level i-1 - Upsampled Gaussian Pyramid Level i
    lpA.append(L)

# 3단계: Laplacian Pyramid 생성 (Image B)
lpB = [gpB[5]] # Base Level Laplacian Pyramid = Gaussian Pyramid Level 6
for i in range(5, 0, -1): # Level 5 부터 Level 1 까지 Laplacian Pyramid 생성
    GE = cv2.pyrUp(gpB[i]) # Gaussian Pyramid Level i Upsampling
    temp = cv2.resize(gpB[i - 1], (GE.shape[1], GE.shape[0])) # Upsampling 이미지 크기를 Gaussian Pyramid Level i-1 크기로 Resize
    L = cv2.subtract(temp, GE) # Laplacian Pyramid Level i = Gaussian Pyramid Level i-1 - Upsampled Gaussian Pyramid Level i
    lpB.append(L)

# 4단계: Laplacian Pyramid Level 별 좌우 영역 결합 (Blend)
LS = []
for la, lb in zip(lpA, lpB):
    rows, cols, dpt = la.shape
    ls = np.hstack((la[:, 0:cols // 2], lb[:, cols // 2:])) # 좌측 (Image A) 영역과 우측 (Image B) 영역 결합
    LS.append(ls)

# 5단계: Laplacian Pyramid Blending 결과 재구성
ls_ = LS[0] # Base Level Blending 이미지
for i in range(1, 6): # Level 1 부터 Level 5 까지 Upsampling 및 Add 연산
    ls_ = cv2.pyrUp(ls_) # Upsampling
    temp = cv2.resize(LS[i], (ls_.shape[1], ls_.shape[0])) # Upsampling 이미지 크기를 Laplacian Pyramid Level i 크기로 Resize
    ls_ = cv2.add(ls_, temp) # Upsampling 이미지 + Laplacian Pyramid Level i (외곽선 정보)

# 원본 이미지 단순 결합 (비교용)
real = np.hstack((A[:, :cols // 2], B[:, cols // 2:]))

cv2.imshow('Real Blending', real) # 단순 결합 이미지 표시
cv2.imshow('Pyramid Blending', ls_) # Pyramid Blending 이미지 표시
cv2.waitKey(0)
cv2.destroyAllWindows()
```

**Image Pyramid Blending 은 단순 결합에 비해 경계면이 부드럽고 자연스러운 Blending 결과를 제공합니다.**

</div>

---

## 14. Image Contours (이미지 윤곽선)

**Goal:**

- Contour (윤곽선) 개념 학습
- Contour 찾기 및 그리기 방법 학습
- `cv2.findContours()`, `cv2.drawContours()` 함수 이해

**Image Contours (이미지 윤곽선) 의 활용:**

- 객체 검출 (Object Detection)
- 객체 측정 (Object Measurement) (면적, 둘레 길이, 중심점 등)
- 이미지 Segmentation (영역 분할)
- 패턴 인식 (Pattern Recognition)

---

### 14.1 Contours (윤곽선) 개요

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Contour (윤곽선) 은 동일한 색상 또는 강도 (Intensity) 를 갖는 영역의 경계선을 연결한 선입니다. 등고선 (Contour Line) 또는 일기 예보 등에서 볼 수 있습니다. 객체의 외형 (Shape) 을 파악하는 데 유용하게 사용됩니다.

**Contour 특징:**

- **정확도 향상:** Binary Image (이진화 이미지) 를 입력으로 사용합니다. Thresholding (임계처리) 또는 Canny Edge Detection 등 전처리 과정 수행 필요.
- **검정색 배경, 흰색 객체:** OpenCV 에서 Contour 는 검정색 배경에서 흰색 객체의 경계선을 찾는 방식으로 동작합니다. 객체는 흰색, 배경은 검정색으로 이진화해야 합니다.
- **원본 이미지 보존:** `cv2.findContours()` 함수는 원본 이미지를 직접 수정하므로, 원본 이미지 보존하려면 복사본 (Copy) 을 사용해야 합니다.

</div>

---

### 14.2 Find & Draw Contours (윤곽선 찾기 및 그리기)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

OpenCV 에서 Contour 를 찾고 그리기 위해 다음 두 함수를 사용합니다.

- **`cv2.findContours(image, mode, method[, contours[, hierarchy[, offset]]])`**: Contour 찾기 함수

| Parameter  | Description                                                                                                                                                                               |
| :--------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `image`    | 입력 이미지 (8-bit, Single-channel Binary Image). GrayScale 이미지에 Thresholding 적용하여 Binary 이미지로 변환 후 입력.                                                                  |
| `mode`     | Contour Retrieval Mode (Contour 검색 모드). Contour Line 검색 방식 지정 (아래 표 참조)                                                                                                    |
| `method`   | Contour Approximation Method (Contour 근사화 방법). Contour Point 저장 방식 지정 (아래 표 참조)                                                                                           |
| **Return** | `image` (Contour 를 찾은 이미지, OpenCV 버전 4.X 이상에서는 3개 값 반환, 3.X 이하에서는 2개 값 반환), `contours` (찾은 Contour Line 정보 List), `hierarchy` (Contour Line 계층 구조 정보) |

**Contour Retrieval Mode (`mode` Parameter):**

| Mode                | `mode` 상수         | Description                                                                                                               |
| :------------------ | :------------------ | :------------------------------------------------------------------------------------------------------------------------ |
| `cv2.RETR_EXTERNAL` | `cv2.RETR_EXTERNAL` | 가장 바깥쪽 (External) Contour Line 만 검색. Hierachy (계층 구조) 구성 X                                                  |
| `cv2.RETR_LIST`     | `cv2.RETR_LIST`     | 모든 Contour Line 검색. Hierachy (계층 구조) 구성 X. 선후 관계만 표현                                                     |
| `cv2.RETR_CCOMP`    | `cv2.RETR_CCOMP`    | 모든 Contour Line 검색. Hierachy (계층 구조) 2-Level 로 구성 (Outer Contour 와 Inner Contour).                            |
| `cv2.RETR_TREE`     | `cv2.RETR_TREE`     | 모든 Contour Line 검색. Hierachy (계층 구조) Tree 구조로 완전하게 구성 (Parent-Child 관계, Next-Previous 관계 모두 표현). |

**Contour Approximation Method (`method` Parameter):**

| Method                       | `method` 상수                | Description                                                                                                           |
| :--------------------------- | :--------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `cv2.CHAIN_APPROX_NONE`      | `cv2.CHAIN_APPROX_NONE`      | 모든 Contour Point 저장. Contour Line 을 정확하게 표현하지만, Point 수가 많아 메모리 사용량 증가.                     |
| `cv2.CHAIN_APPROX_SIMPLE`    | `cv2.CHAIN_APPROX_SIMPLE`    | Contour Line 을 그릴 수 있는 Point 만 저장 (예: 사각형 -> 4개 꼭지점 Point 만 저장). 메모리 사용량 감소, Line 근사화. |
| `cv2.CHAIN_APPROX_TC89_L1`   | `cv2.CHAIN_APPROX_TC89_L1`   | Teh-Chin Chain 근사화 알고리즘 L1 버전                                                                                |
| `cv2.CHAIN_APPROX_TC89_KCOS` | `cv2.CHAIN_APPROX_TC89_KCOS` | Teh-Chin Chain 근사화 알고리즘 KCOS 버전                                                                              |

- **`cv2.drawContours(image, contours, contourIdx, color[, thickness[, lineType[, hierarchy[, maxLevel[, offset]]]]])`**: Contour 그리기 함수

| Parameter    | Description                                                                                                        |
| :----------- | :----------------------------------------------------------------------------------------------------------------- |
| `image`      | 원본 이미지 (Contour 를 그릴 이미지)                                                                               |
| `contours`   | Contour Line 정보 List (`cv2.findContours()` 함수 Return 값)                                                       |
| `contourIdx` | Contour Line Index. `contours` List 에서 몇 번째 Contour Line 을 그릴지 지정. `-1` 이면 모든 Contour Line 을 그림. |
| `color`      | Contour Line 색상 (BGR 튜플)                                                                                       |
| `thickness`  | Contour Line 두께 (Pixel 단위). 음수 값 (예: `cv2.FILLED` 또는 `-1`) 이면 Contour Line 내부를 채움.                |

**샘플 코드 (Contour 찾고 그리기):**

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/rectangle.jpg') # 사각형 이미지 로드
img_copy = img.copy() # 원본 이미지 복사 (보존용)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # GrayScale 변환

# Binary Image 변환 (Thresholding)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)

# Contour 찾기
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # RETR_TREE: Hierachy Tree 구조, CHAIN_APPROX_SIMPLE: Line 근사화

# Contour 그리기
image = cv2.drawContours(img, contours, -1, (0, 255, 0), 3) # 모든 Contour Line (index=-1), Green, 두께 3px

cv2.imshow('Original Image', img_copy) # 원본 이미지 표시
cv2.imshow('Contour Image', image) # Contour Image 표시
cv2.waitKey(0)
cv2.destroyAllWindows()
```

**실행 결과:**

[Result Image - Contour 그리기 결과]

**`cv2.findContours()` 함수는 Binary Image 에서 객체의 윤곽선을 찾아 List 형태로 반환합니다. `cv2.drawContours()` 함수는 원본 이미지에 Contour Line 을 그려줍니다.**

**Contour Approximation Method 비교 (`cv2.CHAIN_APPROX_NONE` vs `cv2.CHAIN_APPROX_SIMPLE`):**

```python
contours_simple, hierarchy_simple = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) # CHAIN_APPROX_SIMPLE
contours_none, hierarchy_none = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) # CHAIN_APPROX_NONE

cnt_simple = contours_simple[0]
cnt_none = contours_none[0]

print("CHAIN_APPROX_SIMPLE Contour Points Shape:", cnt_simple.shape) # 출력 예: (4, 1, 2) (사각형 4개 꼭지점)
print("CHAIN_APPROX_NONE Contour Points Shape:", cnt_none.shape) # 출력 예: (750, 1, 2) (사각형 경계선 모든 Point)
```

**`cv2.CHAIN_APPROX_SIMPLE` 은 `cv2.CHAIN_APPROX_NONE` 에 비해 Contour Line 을 표현하는 데 필요한 Point 수를 줄여 메모리를 절약할 수 있습니다.**

</div>

---

## 15. Contour Feature (윤곽선 특징)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

**Goal:**

- Contour 의 다양한 특징 (Feature) 추출 방법 학습:
  - Moments (모멘트)
  - Contour Area (윤곽선 면적)
  - Contour Perimeter (윤곽선 둘레 길이)
  - Contour Approximation (윤곽선 근사화)
  - Convex Hull (Convex Hull)
  - Checking Convexity (Convexity 체크)
  - Bounding Rectangle (Bounding 사각형)
  - Minimum Enclosing Circle (최소 외접 원)
  - Fitting an Ellipse (타원 Fitting)
- Contour 특징 추출 관련 함수 이해

**Contour Feature (윤곽선 특징) 의 활용:**

- 객체 인식 (Object Recognition)
- 객체 분류 (Object Classification)
- 객체 추적 (Object Tracking)
- 이미지 검색 (Image Retrieval)

</div>

---

### 15.1 Moments (모멘트)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Image Moment 는 이미지 또는 Contour 의 특징 (Feature) 을 나타내는 값입니다. Contour 의 면적, 중심점, 방향성 등 다양한 특징을 Moments 로부터 추출할 수 있습니다.

- **`cv2.moments(array[, binaryImage])`**: Image Moments 계산 함수

| Parameter     | Description                                                                                                                                                                                                                         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `array`       | 입력 이미지 (Single-channel, 8-bit 또는 Floating-point 2D array) 또는 Contour Point Array.                                                                                                                                          |
| `binaryImage` | Binary Image Flag. `True`: 입력 Array 가 Binary Image 로 간주, 0 이 아닌 모든 값을 1 로 처리. `False`: 입력 Array 가 GrayScale 또는 Color Image 로 간주. 기본값: `False`.                                                           |
| **Return**    | Moments 값 (Dictionary 형태). Moments 값 종류: `m00`, `m10`, `m01`, `m20`, `m02`, `m11`, `m30`, `m03`, `m21`, `m12`, `mu02`, `mu03`, `mu20`, `mu21`, `mu11`, `mu12`, `nu02`, `nu03`, `nu20`, `nu21`, `nu11`, `nu12`, `nu30`, `nu03` |

**샘플 코드 (Moments 값 추출 및 중심점 계산):**

```python
import cv2
import numpy as np

img = cv2.imread('images/rectangle.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0] # 첫 번째 Contour Line (사각형)
M = cv2.moments(cnt) # Contour Moments 계산

print("Moments Dictionary:", M.items()) # Moments 값 출력

# Contour 중심점 (Centroid) 계산
cx = int(M['m10'] / M['m00']) # 중심점 X 좌표
cy = int(M['m01'] / M['m00']) # 중심점 Y 좌표
print("Centroid: ({}, {})".format(cx, cy)) # 중심점 좌표 출력
```

**Moments Dictionary (M) 주요 값:**

- `m00`: Contour 면적 (Area)
- `m10`, `m01`: 중심점 계산에 사용
- `mu02`, `mu20`, `mu11`: 중심 모멘트 (Central Moments). 이동 변환에 불변 (Translation Invariant)
- `nu02`, `nu20`, `nu11`: 정규화된 중심 모멘트 (Normalized Central Moments). 이동, 크기 변환에 불변 (Translation & Scale Invariant)

</div>

---

### 15.2 Contour Area (윤곽선 면적)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Contour Area (윤곽선 면적) 은 Contour 가 차지하는 영역의 크기를 나타냅니다. Moments 의 `m00` 값 또는 `cv2.contourArea()` 함수로 구할 수 있습니다.

- **`cv2.contourArea(contour[, oriented])`**: Contour Area 계산 함수

| Parameter  | Description                                                                                                                                  |
| :--------- | :------------------------------------------------------------------------------------------------------------------------------------------- |
| `contour`  | Contour Point Array (`cv2.findContours()` 함수 Return 값)                                                                                    |
| `oriented` | 면적 부호 (Sign) 결정 Flag. `True`: 시계 방향 Contour -> 양수 면적, 반시계 방향 Contour -> 음수 면적. `False`: 절대값 면적. 기본값: `False`. |
| **Return** | Contour Area (float 값)                                                                                                                      |

**샘플 코드 (Contour Area 계산):**

```python
area_moments = M['m00'] # Moments m00 값
area_contourArea = cv2.contourArea(cnt) # cv2.contourArea() 함수 사용

print("Contour Area (Moments):", area_moments)
print("Contour Area (contourArea):", area_contourArea)
```

</div>

---

### 15.3 Contour Perimeter (윤곽선 둘레 길이)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Contour Perimeter (윤곽선 둘레 길이) 는 Contour Line 의 전체 길이를 나타냅니다. `cv2.arcLength()` 함수로 구할 수 있습니다.

- **`cv2.arcLength(curve, closed)`**: Contour Perimeter (둘레 길이) 계산 함수

| Parameter  | Description                                                                                                                                                                                           |
| :--------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `curve`    | Contour Point Array (`cv2.findContours()` 함수 Return 값)                                                                                                                                             |
| `closed`   | 폐곡선 여부 Flag. `True`: 폐곡선 (Closed Contour), `False`: 폴리라인 (Polyline, 열린 곡선). `True` 이면 시작점과 끝점을 연결하여 둘레 길이 계산, `False` 이면 시작점과 끝점 연결 없이 둘레 길이 계산. |
| **Return** | Contour Perimeter (float 값)                                                                                                                                                                          |

**샘플 코드 (Contour Perimeter 계산):**

```python
perimeter_closed = cv2.arcLength(cnt, True) # 폐곡선 둘레 길이
perimeter_open = cv2.arcLength(cnt, False) # 열린 곡선 둘레 길이

print("Contour Perimeter (Closed):", perimeter_closed)
print("Contour Perimeter (Open):", perimeter_open)
```

</div>

---

### 15.4 Contour Approximation (윤곽선 근사화)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Contour Approximation (윤곽선 근사화) 는 `cv2.findContours()` 함수로 찾은 Contour Line 의 Point 수를 줄여 근사화된 Line 을 그리는 방법입니다. Douglas-Peucker Algorithm 을 사용합니다. 메모리 사용량을 줄이고, Contour Line 을 단순화하는 데 유용합니다.

- **`cv2.approxPolyDP(curve, epsilon, closed[, approxCurve])`**: Contour Approximation 함수

| Parameter  | Description                                                                                                                                                                                                                                  |
| :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `curve`    | Contour Point Array (`cv2.findContours()` 함수 Return 값)                                                                                                                                                                                    |
| `epsilon`  | 근사치 정확도 (Approximation Accuracy). Original Curve 와 근사 Curve 간의 최대 거리 (Maximum Distance). 값이 클수록 근사 정확도는 낮아지지만, Point 수는 줄어듭니다. 일반적으로 Contour Perimeter (`cv2.arcLength()`) 값의 일정 비율로 설정. |
| `closed`   | 폐곡선 여부 Flag. `True`: 폐곡선 (Closed Contour), `False`: 폴리라인 (Polyline, 열린 곡선).                                                                                                                                                  |
| **Return** | 근사화된 Contour Point Array (NumPy array)                                                                                                                                                                                                   |

**샘플 코드 (Contour Approximation 결과 비교):**

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/bad_rect.png') # 부정확한 사각형 이미지 로드
img1 = img.copy()
img2 = img.copy()

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0] # 첫 번째 Contour Line

# epsilon 값 설정 (Contour Perimeter 비율)
epsilon1 = 0.01 * cv2.arcLength(cnt, True) # 1%
epsilon2 = 0.1 * cv2.arcLength(cnt, True) # 10%

# Contour Approximation 적용
approx1 = cv2.approxPolyDP(cnt, epsilon1, True) # 1% epsilon
approx2 = cv2.approxPolyDP(cnt, epsilon2, True) # 10% epsilon

# Contour 그리기 (Original, 1% Approximation, 10% Approximation)
cv2.drawContours(img, [cnt], 0, (0, 255, 0), 3) # Original Contour (Green)
cv2.drawContours(img1, [approx1], 0, (0, 255, 0), 3) # 1% Approximation Contour (Green)
cv2.drawContours(img2, [approx2], 0, (0, 255, 0), 3) # 10% Approximation Contour (Green)

titles = ['Original', '1%', '10%']
images = [img, img1, img2]

for i in range(3):
    plt.subplot(1, 3, i + 1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])

plt.show()
```

**실행 결과:**

[Result Image - Contour Approximation 결과 비교 (epsilon 값 변화에 따른 Point 수 감소)]

**`epsilon` 값이 커질수록 Contour Approximation 정확도는 낮아지지만, Point 수는 줄어듭니다.**

</div>

---

### 15.5 Convex Hull

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Convex Hull (볼록 껍질) 은 Contour Point 를 모두 포함하는 가장 작은 볼록 다각형입니다. Contour Approximation 과 유사한 외형선 (Outline) 을 얻을 수 있지만, 알고리즘은 다릅니다. Convex Hull 은 항상 볼록 (Convex) 한 형태를 가집니다.

- **`cv2.convexHull(points[, hull[, clockwise[, returnPoints]]])`**: Convex Hull 계산 함수

| Parameter      | Description                                                                                                                        |
| :------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| `points`       | Contour Point Array (`cv2.findContours()` 함수 Return 값)                                                                          |
| `clockwise`    | Convex Hull 방향 Flag. `True`: 시계 방향, `False`: 반시계 방향. 기본값: `False` (반시계 방향).                                     |
| `returnPoints` | 반환 값 Flag. `True`: Convex Hull Point 반환 (기본값), `False`: Convex Hull Point Index 반환.                                      |
| **Return**     | Convex Hull Point Array (NumPy array) 또는 Convex Hull Point Index Array (NumPy array). `returnPoints` 값에 따라 반환 값이 달라짐. |

**Convexity Defect (Convexity 결함):**

Convex Hull 과 Contour 간의 차이 (최대 거리) 를 나타냅니다. Convexity Defect 를 이용하여 Contour 의 오목한 부분 (Concave Part) 을 분석할 수 있습니다.

[Convex Hull Image - Convex Hull 및 Convexity Defect 시각화]

**샘플 코드 (Convex Hull 추출 및 그리기):**

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/hand.png') # 손 모양 이미지 로드
img1 = img.copy()

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[1] # 손 모양 Contour Line (두 번째 Contour)
hull = cv2.convexHull(cnt) # Convex Hull 계산

cv2.drawContours(img1, [hull], 0, (0, 255, 0), 3) # Convex Hull 그리기 (Green)

titles = ['Original', 'Convex Hull']
images = [img, img1]

for i in range(2):
    plt.subplot(1, 2, i + 1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])

plt.show()
```

**실행 결과:**

[Result Image - Convex Hull 그리기 결과]

</div>

---

### 15.6 Checking Convexity (Convexity 체크)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Contour 가 Convex (볼록) 한지 여부를 체크합니다. `cv2.isContourConvex()` 함수는 Contour 가 Convex 하면 `True`, Concave (오목) 하면 `False` 를 반환합니다.

- **`cv2.isContourConvex(contour)`**: Convexity 체크 함수

| Parameter  | Description                                                                   |
| :--------- | :---------------------------------------------------------------------------- |
| `contour`  | Contour Point Array (`cv2.findContours()` 함수 Return 값)                     |
| **Return** | Convexity 여부 (Boolean 값). `True`: Convex Contour, `False`: Concave Contour |

**Convex Contour vs Concave Contour:**

- **Convex Contour (볼록 윤곽선):** 모든 내부 각도가 180도 이하인 Contour. 오목한 부분 없음.
- **Concave Contour (오목 윤곽선):** 내부 각도가 180도 초과인 부분이 하나라도 있는 Contour. 오목한 부분 있음.

**샘플 코드 (Convexity 체크):**

```python
convex_hull_check = cv2.isContourConvex(contours[0]) # 첫 번째 Contour (외곽선 사각형) Convexity 체크
hand_contour_check = cv2.isContourConvex(contours[1]) # 두 번째 Contour (손 모양) Convexity 체크

print("Is Outer Contour Convex?:", convex_hull_check) # 출력 예: True (사각형은 Convex)
print("Is Hand Contour Convex?:", hand_contour_check) # 출력 예: False (손 모양은 Concave)
```

</div>

---

### 15.7 Bounding Rectangle (Bounding 사각형)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Bounding Rectangle (Bounding 사각형) 은 Contour Line 을 둘러싸는 사각형을 그리는 방법입니다.

**Bounding Rectangle 종류:**

1. **Straight Bounding Rectangle (직사각형 Bounding Box):** 객체의 회전 (Rotation) 을 고려하지 않고, 축에 평행한 직사각형 Bounding Box 를 생성합니다.

- `cv2.boundingRect(array)`: 직사각형 Bounding Box 정보 (좌상단 좌표, 너비, 높이) 반환

2. **Rotated Rectangle (회전된 사각형 Bounding Box):** 객체의 회전을 고려하여 객체를 최소 면적으로 감싸는 회전된 사각형 Bounding Box 를 생성합니다.

- `cv2.minAreaRect(points)`: 회전된 사각형 Bounding Box 정보 (중심점, 크기, 회전 각도) 반환
- `cv2.boxPoints(rect)`: 회전된 사각형 Bounding Box 정보를 이용하여 4개의 꼭지점 좌표 반환

**샘플 코드 (Bounding Rectangle 그리기):**

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/lightning.jpg') # 번개 이미지 로드
img1 = img.copy()

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[1] # 번개 Contour Line (두 번째 Contour)

# Straight Bounding Rectangle (직사각형 Bounding Box)
x, y, w, h = cv2.boundingRect(cnt) # Bounding Box 정보
img1 = cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 255, 0), 3) # Green 직사각형 Bounding Box

# Rotated Rectangle (회전된 사각형 Bounding Box)
rect = cv2.minAreaRect(cnt) # 회전된 Bounding Box 정보
box = cv2.boxPoints(rect) # Bounding Box 꼭지점 좌표
box = np.int0(box) # 정수 좌표 변환
img1 = cv2.drawContours(img1, [box], 0, (0, 0, 255), 3) # Blue 회전된 사각형 Bounding Box

titles = ['Original', 'Result']
images = [img, img1]

for i in range(2):
    plt.subplot(1, 2, i + 1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])

plt.show()
```

**실행 결과:**

[Result Image - Bounding Rectangle 그리기 결과 (직사각형, 회전된 사각형 비교)]

</div>

---

### 15.8 Minimum Enclosing Circle (최소 외접 원)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Minimum Enclosing Circle (최소 외접 원) 은 Contour Line 을 완전히 포함하는 가장 작은 원을 그리는 방법입니다.

- **`cv2.minEnclosingCircle(points)`**: 최소 외접 원 정보 (중심점, 반지름) 반환

**샘플 코드 (Minimum Enclosing Circle 그리기):**

```python
# Minimum Enclosing Circle (최소 외접 원)
(x, y), radius = cv2.minEnclosingCircle(cnt) # 최소 외접 원 정보 (중심점, 반지름)
center = (int(x), int(y)) # 중심점 좌표 (정수 변환)
radius = int(radius) # 반지름 (정수 변환)
img1 = cv2.circle(img1, center, radius, (255, 255, 0), 3) # Yellow 최소 외접 원
```

</div>

---

### 15.9 Fitting an Ellipse (타원 Fitting)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Fitting an Ellipse (타원 Fitting) 은 Contour Line 을 가장 잘 근사하는 타원을 Fitting 하는 방법입니다.

- **`cv2.fitEllipse(points)`**: 타원 Fitting 정보 (RotatedRect 객체) 반환

**샘플 코드 (Ellipse Fitting 및 그리기):**

```python
# Fitting an Ellipse (타원 Fitting)
ellipse = cv2.fitEllipse(cnt) # 타원 Fitting 정보
img1 = cv2.ellipse(img1, ellipse, (255, 0, 0), 3) # Red 타원
```

**샘플 코드 (Bounding Rectangle, Minimum Enclosing Circle, Ellipse Fitting 종합):**

```python
# (Bounding Rectangle, Minimum Enclosing Circle, Ellipse Fitting 코드 추가)
# ... (이전 코드에서 Bounding Rectangle 코드까지 포함)

# Minimum Enclosing Circle (최소 외접 원) 코드 추가 (위 코드 참조)
# Fitting an Ellipse (타원 Fitting) 코드 추가 (위 코드 참조)

# ... (Plotting 코드 - titles, images, plt.subplot, plt.imshow, plt.show())
```

**실행 결과:**

[Result Image - Bounding Rectangle, Minimum Enclosing Circle, Ellipse Fitting 결과 비교]

</div>

---

## 16. Contour Property (윤곽선 속성)

**Goal:**

- Contour 의 추가적인 속성 (Property) 학습:
  - Aspect Ratio (가로 세로 비율)
  - Extend (Extend 비율)
  - Solidity (Solidity 비율)
  - Extreme Points (Extream 점)

**Contour Property (윤곽선 속성) 의 활용:**

- 객체 형태 분석 (Shape Analysis)
- 객체 분류 (Object Classification)
- 객체 특징 표현 (Feature Representation)

---

### 16.1 Aspect Ratio (가로 세로 비율)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Aspect Ratio (가로 세로 비율) 은 Contour Line 의 Bounding Box (Bounding 사각형) 의 가로 (Width) 와 세로 (Height) 비율입니다. 객체의 가로 방향으로 길쭉한지, 세로 방향으로 길쭉한지, 정사각형에 가까운지 등을 나타냅니다.

**수학식:**

\[Aspect Ratio = \frac { Width }{ Height }\]

**샘플 코드 (Aspect Ratio 계산):**

```python
import cv2
import numpy as np

img = cv2.imread('images/rectangle.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0] # 첫 번째 Contour Line (사각형)

x, y, w, h = cv2.boundingRect(cnt) # Bounding Box 정보
aspect_ratio = float(w) / h # Aspect Ratio 계산

print("Aspect Ratio:", aspect_ratio) # 출력 예: 1.0 (정사각형에 가까움)
```

</div>

---

### 16.2 Extend (Extend 비율)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Extend (Extend 비율) 은 Contour Area (윤곽선 면적) 를 Bounding Rectangle Area (Bounding 사각형 면적) 로 나눈 비율입니다. Contour 가 Bounding Rectangle 을 얼마나 꽉 채우고 있는지 나타냅니다.

**수학식:**

\[Extend=\frac { Contour Area }{ Bounding Rectangle Area }\]

**샘플 코드 (Extend 비율 계산):**

```python
area = cv2.contourArea(cnt) # Contour Area
x, y, w, h = cv2.boundingRect(cnt) # Bounding Box 정보
rect_area = w * h # Bounding Rectangle Area
extend = float(area) / rect_area # Extend 비율 계산

print("Extend Ratio:", extend) # 출력 예: 1.0 (사각형은 Bounding Box 를 꽉 채움)
```

</div>

---

### 16.3 Solidity (Solidity 비율)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Solidity (Solidity 비율, 고형비) 는 Contour Area (윤곽선 면적) 를 Convex Hull Area (Convex Hull 면적) 로 나눈 비율입니다. Contour 가 얼마나 Convex Hull 에 꽉 차 있는지, 즉 얼마나 볼록한 형태인지 나타냅니다. Convex Hull 에 비해 오목한 부분이 많을수록 Solidity 값은 작아집니다.

**수학식:**

\[Solidity=\frac { Contour Area }{ Convex Hull Area }\]

**샘플 코드 (Solidity 비율 계산):**

```python
area = cv2.contourArea(cnt) # Contour Area
hull = cv2.convexHull(cnt) # Convex Hull
hull_area = cv2.contourArea(hull) # Convex Hull Area
solidity = float(area) / hull_area # Solidity 비율 계산

print("Solidity Ratio:", solidity) # 출력 예: 1.0 (사각형은 Convex Hull 과 동일)
```

</div>

---

### 16.4 Extreme Points (Extream 점)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Extreme Points (Extream 점) 은 Contour Line 에서 가장 좌측, 우측, 상단, 하단 에 위치한 점들을 찾는 방법입니다. 객체의 가장자리 점들을 파악하는 데 유용합니다.

- **`cnt[:,:,0]`**: Contour Point Array (`cnt`) 에서 X 좌표 값만 추출한 배열
- **`cnt[:,:,1]`**: Contour Point Array (`cnt`) 에서 Y 좌표 값만 추출한 배열
- **`argmin()`**: 배열에서 최소값의 Index 반환
- **`argmax()`**: 배열에서 최대값의 Index 반환

**샘플 코드 (Extreme Points 찾기 및 표시):**

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/UK.jpg') # 영국 지도 이미지 로드
img1 = img.copy()

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 125, 255, 0)
image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[14] # 영국 지도 Contour Line (14번째 Contour)

# Extreme Points 찾기
leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0]) # 가장 좌측 점
rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0]) # 가장 우측 점
topmost = tuple(cnt[cnt[:, :, 1].argmin()][0]) # 가장 상단 점
bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0]) # 가장 하단 점

# Extreme Points 좌표 표시 (원 그리기)
cv2.circle(img1, leftmost, 20, (0, 0, 255), -1) # Red
cv2.circle(img1, rightmost, 20, (0, 0, 255), -1) # Red
cv2.circle(img1, topmost, 20, (0, 0, 255), -1) # Red
cv2.circle(img1, bottommost, 20, (0, 0, 255), -1) # Red

img1 = cv2.drawContours(img1, cnt, -1, (255, 0, 0), 5) # Contour Line 그리기 (Blue)

titles = ['Original', 'Result']
images = [img, img1]

for i in range(2):
    plt.subplot(1, 2, i + 1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])

plt.show()
```

**실행 결과:**

[Result Image - Extreme Points 표시 결과 (영국 지도 Contour 에 좌우상하 Extream 점 표시)]

</div>

---

## 17. Contours Hierarchy (윤곽선 계층 구조)

**Goal:**

- Contour Hierarchy (윤곽선 계층 구조) 개념 학습
- Contour Retrieval Mode 에 따른 Hierarchy 정보 변화 이해
- `cv2.RETR_LIST`, `cv2.RETR_EXTERNAL`, `cv2.RETR_CCOMP`, `cv2.RETR_TREE` Contour Retrieval Mode 비교

**Contours Hierarchy (윤곽선 계층 구조) 의 활용:**

- 복잡한 객체 구조 분석 (Nested Object Structure Analysis)
- 이미지 Segmentation (영역 분할)
- 객체 관계 분석 (Object Relation Analysis)

---

### 17.1 Hierarchy (계층 구조) 개요

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Image 내에는 여러 개의 Contour Line 이 존재하고, Contour Line 들 사이에 서로 포함 관계 (Parent-Child Relationship) 가 존재합니다. Contours Hierarchy (윤곽선 계층 구조) 는 이러한 Contour Line 들의 계층적인 관계를 나타냅니다.

**Hierarchy 정보:**

- **Next Contour (다음 Contour):** 동일한 계층 Level 에서 다음 Contour Line
- **Previous Contour (이전 Contour):** 동일한 계층 Level 에서 이전 Contour Line
- **Child Contour (자식 Contour):** 현재 Contour Line 에 포함된 하위 계층 Contour Line
- **Parent Contour (부모 Contour):** 현재 Contour Line 을 포함하는 상위 계층 Contour Line

**`cv2.findContours()` 함수 `mode` Parameter 에 따라 Hierarchy 정보 구성 방식이 달라집니다.**

</div>

---

### 17.2 샘플 이미지 (Hierarchy 예제)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

**Contour Line 번호:** 1, 2, 3, 3a, 4, 4a, 5, 6, 7, 8, 9 (총 9개)

**주의:** 3, 3a 와 4, 4a 는 Child Contour 가 있는 경우 Outer Contour 와 Inner Contour 가 분리되어 Contour Line 을 구성합니다. 이는 포함 관계를 표현하기 위함입니다. (5번 Contour 는 Child Contour 만 있으므로 분리되지 않음)

**샘플 코드 (Contour Line 번호 표시):**

```python
import cv2
import numpy as np
import random
from matplotlib import pyplot as plt

img = cv2.imread('images/imageHierarchy.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 125, 255, 0)

image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # RETR_TREE Mode

for i, cnt in enumerate(contours): # Contour Line 번호 표시
    b = random.randrange(1, 255) # Random Color 생성
    g = random.randrange(1, 255)
    r = random.randrange(1, 255)

    cv2.drawContours(img, [cnt], -1, (b, g, r), 2) # Contour Line 그리기 (Random Color)
    M = cv2.moments(cnt) # Contour Moments 계산
    cx = int(M['m10'] / M['m00']) # 중심점 X 좌표
    cy = int(M['m01'] / M['m00']) # 중심점 Y 좌표
    cv2.putText(img, str(i + 1), (cx - 20, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2) # Contour 번호 텍스트 표시 (White)

titles = ['Result']
images = [img]

for i in range(1):
    plt.subplot(1, 1, i + 1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])

plt.show()
```

**실행 결과:**

[Result Image - Contour Line 번호 표시 결과]

</div>

---

### 17.3 RETR_LIST Mode

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

`cv2.RETR_LIST` Mode 는 Contour Line 의 선후 관계 (Next-Previous Relationship) 만 표현하고, Parent-Child 관계는 표현하지 않는 Mode 입니다.

**Hierarchy Shape:** `(1, N, 4)` (N: Contour Line 개수)

- 3번째 차원 (4개 값): `[Next Contour Index, Previous Contour Index, Child Contour Index, Parent Contour Index]`

**`cv2.RETR_LIST` Mode Hierarchy 정보:**

- **Next Contour Index:** 다음 Contour Line Index. 다음 Contour Line 이 없으면 `-1`
- **Previous Contour Index:** 이전 Contour Line Index. 이전 Contour Line 이 없으면 `-1`
- **Child Contour Index:** Child Contour Line Index. `cv2.RETR_LIST` Mode 에서는 항상 `-1` (Parent-Child 관계 표현 X)
- **Parent Contour Index:** Parent Contour Line Index. `cv2.RETR_LIST` Mode 에서는 항상 `-1` (Parent-Child 관계 표현 X)

**샘플 코드 (RETR_LIST Mode Hierarchy 정보 확인):**

```python
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) # RETR_LIST Mode
print("RETR_LIST Hierarchy:", hierarchy) # Hierarchy 정보 출력
```

**출력 결과:**

```
RETR_LIST Hierarchy: [[[ 1 -1 -1 -1]
  [ 2  0 -1 -1]
  [ 3  1 -1 -1]
  [ 4  2 -1 -1]
  [ 5  3 -1 -1]
  [ 6  4 -1 -1]
  [ 7  5 -1 -1]
  [ 8  6 -1 -1]
  [-1  7 -1 -1]]]
```

**Contour-0:** Next Contour: Contour-1, Previous/Child/Parent Contour: 없음 (`-1`)
**Contour-1:** Next Contour: Contour-2, Previous Contour: Contour-0, Child/Parent Contour: 없음 (`-1`)
...
**Contour-8:** Next/Child/Parent Contour: 없음 (`-1`), Previous Contour: Contour-7

**Hierarchy 정보가 필요 없고, 모든 Contour Line 을 검색해야 하는 경우에 유용합니다.**

</div>

---

### 17.4 RETR_EXTERNAL Mode

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

`cv2.RETR_EXTERNAL` Mode 는 가장 바깥쪽 (External) Contour Line 만 검색합니다. 다른 Contour Line 에 포함되지 않는 Outer Contour Line 만 검색합니다. Parent-Child 관계는 구성하지 않습니다.

**`cv2.RETR_EXTERNAL` Mode Hierarchy 정보:**

- Hierarchy Shape: `(1, N, 4)` (N: External Contour Line 개수)
- Hierarchy 정보는 `cv2.RETR_LIST` Mode 와 유사하지만, Parent-Child 관계 정보는 항상 `-1` 입니다.

**샘플 코드 (RETR_EXTERNAL Mode Hierarchy 정보 확인):**

```python
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # RETR_EXTERNAL Mode
print("RETR_EXTERNAL Hierarchy:", hierarchy) # Hierarchy 정보 출력
```

**출력 결과:**

```
RETR_EXTERNAL Hierarchy: [[[ 1 -1 -1 -1]
  [ 2  0 -1 -1]
  [-1  1 -1 -1]]]
```

**`cv2.RETR_EXTERNAL` Mode 는 가장 바깥쪽 Contour Line (Outer Contour) 만 필요하고, Hierachy 정보가 필요 없는 경우에 유용합니다.**

</div>

---

### 17.5 RETR_CCOMP Mode

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

`cv2.RETR_CCOMP` Mode 는 Hierarchy 를 2-Level 로 표현합니다. Outer Contour 는 1-Level, Inner Contour (Outer Contour 에 포함된 Contour) 는 2-Level 로 계층 구조를 구성합니다.

**`cv2.RETR_CCOMP` Mode Hierarchy 정보:**

- Outer Contour (Level-1): Parent Contour Index = `-1`, Child Contour Index = Inner Contour Index (Level-2)
- Inner Contour (Level-2): Parent Contour Index = Outer Contour Index (Level-1), Child Contour Index = `-1`

**샘플 코드 (RETR_CCOMP Mode Hierarchy 정보 확인):**

```python
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE) # RETR_CCOMP Mode
print("RETR_CCOMP Hierarchy:", hierarchy) # Hierarchy 정보 출력
```

**출력 결과:**

```
RETR_CCOMP Hierarchy: [[[ 3 -1  1 -1]
  [ 2 -1 -1  0]
  [-1  1 -1  0]
  [ 5  0  4 -1]
  [-1 -1 -1  3]
  [ 7  3  6 -1]
  [-1 -1 -1  5]
  [ 8  5 -1 -1]
  [-1  7 -1 -1]]]
```

**Contour-0 (Outer Contour):** Next Contour: Contour-3, Child Contour: Contour-1
**Contour-1 (Inner Contour):** Next Contour: Contour-2, Parent Contour: Contour-0
**Contour-2 (Inner Contour):** Next Contour: 없음 (`-1`), Previous Contour: Contour-1, Parent Contour: Contour-0
**Contour-3 (Outer Contour):** Next Contour: Contour-5, Previous Contour: Contour-0, Child Contour: Contour-4
...

**`cv2.RETR_CCOMP` Mode 는 Outer Contour 와 Inner Contour 의 2-Level Hierachy 정보가 필요한 경우에 유용합니다.**

</div>
