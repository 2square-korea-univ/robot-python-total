---
title: "객체 추적"
css: style.css
tags:
  - datetime
---

## 강좌 정보

**강좌명:** OpenCV와 Python 기반 객체 추적 이해 및 실습

**강좌 목표:**

- 객체 추적 기본 원리 이해
- 다양한 추적 알고리즘 (KCF, CSRT, MIL 등) 개념 및 특징 학습, 코드 적용
- Python OpenCV 코드를 분석, 객체 추적 시스템 작동 방식 체득
- 객체 추적 성능 영향 요인 이해, 간단한 성능 개선 방법 모색
- 실제 코딩 실습 통해 객체 추적 구현 능력 향상

---

## 수강 대상

- 컴퓨터 비전, 영상 처리 분야 입문 희망자
- Python 프로그래밍 및 OpenCV 활용 경험자 (초급 이상)
- 객체 추적 기술 기초 학습 및 실습 희망자

**필수 조건:**

- Python 기본 문법 이해
- OpenCV 설치 및 기본 사용법 경험 (이미지 입출력 등)

---

## layout: section

# 강의 구성

## layout: section

# 1교시: 객체 추적 개념 및 원리 (이론 강의 - )

---

## 1. 객체 추적이란 무엇인가?

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

### 객체 추적의 정의와 목표

**객체 추적 (Object Tracking):**

- 비디오 영상 속에서 **특정 객체**를 **지속적으로** 따라가는 기술

- **입력:**

  - 비디오 프레임 시퀀스
  - 첫 프레임에서의 객체 위치 (bounding box)

- **출력:**
  - 각 프레임에서 객체의 위치 (bounding box 좌표)

**핵심 목표:**

- **시간 흐름**에 따른 객체의 **위치 변화** 파악
- 객체의 **움직임**, **외형 변화**, **가려짐** 등 다양한 환경 변화에 **robust**하게 추적

</div>

---

### 객체 추적, 왜 중요할까요?

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

**일상 생활 곳곳에 활용되는 핵심 기술**

- **보안 및 감시:**

  - 침입자 감지, 수상한 행동 추적 (CCTV)
  - 특정 물체 도난 방지

- **자율 주행:**

  - 차량, 보행자, 장애물 실시간 추적
  - 안전 운전, 주변 환경 인식

- **로봇 공학:**

  - 로봇 팔 제어, 물류 자동화
  - 목표 객체 추적 및 조작

- **영상 분석:**

  - 스포츠 경기 분석 (선수, 공 추적)
  - 의료 영상 분석 (세포 움직임 추적)

- **AR/VR:**
  - 사용자 시선, 손 움직임 추적
  - 인터랙티브 콘텐츠, 몰입형 경험 제공

**미래 기술 발전에 필수적인 기반 기술**

</div>

---

### 객체 추적, 어떤 어려움이 있을까요?

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

**현실 세계의 복잡성: 추적을 방해하는 다양한 요인**

- **조명 변화 (Illumination Variation):**

  - 그림자, 밝기 변화 → 객체 외형 변화

- **객체 자세 변화 (Pose Variation):**

  - 객체 회전, 변형 → 외형 변화, 추적 어려움 증가

- **가려짐 (Occlusion):**

  - 다른 객체, 배경에 의한 가려짐 → 객체 정보 손실, 추적 실패 가능성

- **배경 복잡성 (Background Clutter):**

  - 객체와 유사한 배경 → 객체 식별 어려움

- **빠른 움직임 (Fast Motion):**

  - 모션 블러 발생 → 객체 외형 흐려짐, 추적 정확도 감소

- **카메라 움직임 (Camera Motion):**

  - 카메라 자체 움직임 → 객체 상대적 움직임 파악 복잡

- **저해상도 (Low Resolution):**
  - 객체 정보 부족 → 특징 추출 어려움

**➡️ 이러한 어려움을 극복하는 것이 객체 추적 알고리즘의 핵심 과제**

</div>

---

## 2. 객체 추적의 기본 원리

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

### 객체 추적 단계: 3단계 파이프라인

1. **초기화 (Initialization):**

   - 첫 프레임에서 추적할 **객체 지정** (bounding box 설정)
   - 객체의 **특징 정보 추출** (색상, 질감, 모양 등)

2. **추적 (Tracking):**

   - 이전 프레임 객체 정보를 기반으로 **현재 프레임에서 객체 위치 예측**
   - 다양한 알고리즘 활용 (외형 기반, 모델 기반 등)

3. **업데이트 (Update) (선택 사항):**
   - 추적 결과 기반으로 **객체 모델 갱신** (외형 변화 적응)
   - 장기 추적 성능 향상, 드리프트 방지

**각 단계별 역할과 중요성 이해**

</div>

---

### 2.1. 초기화 (Initialization): 첫 단추를 잘 꿰어야...

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

- **추적 시작점 설정:** 추적 대상 객체를 **정확하게** 지정하는 단계

- **ROI (Region of Interest) 설정:**

  - 추적할 객체 영역을 **bounding box** 형태로 지정
  - **수동 ROI 설정:** 사용자 직접 지정 (본 실습) - 직관적, 간편
  - **자동 ROI 설정:** 객체 탐지 알고리즘 활용 (YOLO, SSD 등) - 자동화, 복잡 시스템

- **초기 객체 특징 추출:**
  - ROI 영역의 **시각적 특징** 분석 (색상 히스토그램, 특징점 등)
  - 추적 알고리즘에 필요한 **기초 정보** 확보

**초기화 품질 ➡️ 전체 추적 성능에 큰 영향**

</div>

---

### 2.2. 추적 (Tracking): 핵심 엔진 작동

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

- **핵심 단계:** 이전 프레임 정보를 바탕으로 **현재 프레임 객체 위치 추정**

- **다양한 추적 알고리즘 존재:** 각 알고리즘은 **강점과 약점** 존재, 상황에 맞는 선택 중요

- **주요 추적 방식:**

  - **외형 기반 추적 (Appearance-based Tracking):**

    - 객체의 **시각적 특징** (색상, 질감, 모양 등) 활용
    - **장점:** 직관적, 비교적 빠름
    - **단점:** 외형 변화, 조명 변화, 가려짐에 취약 가능성
    - **예시:** KCF, CSRT, MIL (본 실습 주요 알고리즘)

  - **모델 기반 추적 (Model-based Tracking):**
    - 객체의 **3D 모델** 또는 **움직임 모델** 활용
    - **장점:** 자세 변화, 3D 공간 추적에 강점
    - **단점:** 복잡도 높음, 실시간 처리 어려울 수 있음
    - **예시:** Particle Filter, Kalman Filter

**본 실습:** 외형 기반 추적 알고리즘 집중 학습 및 실습

</div>

---

### OpenCV 추적 알고리즘: 다양한 선택지 제공

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

**OpenCV, 풍부한 추적 알고리즘 제공:** 목적과 환경에 따라 선택 가능

- **`cv2.TrackerKCF_create()`: KCF (Kernelized Correlation Filter)**

  - **특징:** 매우 빠름, 실시간 추적에 적합, 외형 변화에 강 robust, 가려짐에 다소 취약

- **`cv2.TrackerCSRT_create()`: CSRT (Channel and Spatial Reliability Tracking)**

  - **특징:** 높은 정확도, Occlusion robust, KCF보다 느림, 복잡 환경 적합

- **`cv2.TrackerMIL_create()`: MIL (Multiple Instance Learning)**

  - **특징:** 장기 추적 강점, Occlusion 매우 robust, 느림, 장시간 가려짐 후 재등장 객체 추적 유리

- **`cv2.TrackerBoosting_create()`: Boosting Tracker**

  - **특징:** 초기 알고리즘, 중간 성능, KCF, CSRT, MIL 대비 성능↓

- **`cv2.TrackerMedianFlow_create()`: MedianFlow Tracker**

  - **특징:** 빠름, 움직임 적은 객체 추적 적합, 빠른 움직임, 가려짐에 취약

- **`cv2.TrackerTLD_create()`: TLD (Tracking-Learning-Detection)**

  - **특징:** 장기 추적 유리, 추적 실패 시 재탐지, False Positive 가능성

- **`cv2.TrackerMOSSE_create()`: MOSSE (Minimum Output Sum of Squared Error)**
  - **특징:** 매우 빠름, grayscale 기반, 간단 환경, 빠른 추적, 외형/조명 변화 취약

**➡️ 각 알고리즘 장단점 숙지, 상황 맞춤형 알고리즘 선택 중요**

</div>

---

### 알고리즘 선택 가이드: 나에게 맞는 알고리즘은?

| 알고리즘   | 속도 | 정확도 | 가려짐 | 외형 변화 | 장기 추적 | 특징                            |
| ---------- | ---- | ------ | ------ | --------- | --------- | ------------------------------- |
| **KCF**    | 상   | 중     | 하     | 상        | 중        | 실시간 처리, 외형 변화에 강함   |
| **CSRT**   | 하   | 상     | 상     | 중        | 중        | 높은 정확도, 복잡한 환경에 적합 |
| **MIL**    | 하   | 중     | 상     | 중        | 상        | 장기 추적, 가려짐에 강함        |
| Boosting   | 중   | 중     | 중     | 중        | 중        | 기본적인 성능                   |
| MedianFlow | 상   | 하     | 하     | 하        | 하        | 빠른 속도, 단순한 환경에 적합   |
| TLD        | 중   | 중     | 중     | 중        | 상        | 재탐지 기능 포함                |
| MOSSE      | 상   | 하     | 하     | 하        | 하        | 최고 속도, 단순한 환경에만 적합 |

- 상: 매우 좋음, 중: 보통, 하: 약함

**⚠️ 위 표는 일반적인 경향, 실제 성능은 환경에 따라 달라질 수 있음. 직접 테스트 중요**

---

### 2.3. 업데이트 (Update) (선택 사항): 추적 성능 향상

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

- **추적 모델 갱신:** 추적 결과 반영, **모델 점진적 개선** (일부 알고리즘)

- **목적:**

  - **성능 향상:** 객체 외형, 조명 변화 적응, 추적 안정성 유지/향상
  - **드리프트 방지:** 시간 경과에 따른 추적 오류 누적 방지

- **방법:**

  - **온라인 학습:** 매 프레임마다 모델 업데이트 (KCF, CSRT, MIL 등)
  - **오프라인 학습:** 전체 비디오 또는 일부 구간 학습 후 추적 (TLD 등)

- **장단점:**
  - 👍 성능 향상, 장기 추적 안정성
  - 👎 계산 복잡도 증가, 속도 저하 가능성, 잘못된 업데이트 시 성능 저하 위험

**업데이트 유무, 알고리즘 및 환경에 따라 결정. 본 실습에서는 온라인 학습 방식 활용**

</div>

---

## 3. OpenCV를 이용한 객체 추적 파이프라인

### OpenCV 추적 API: 간편하고 강력한 도구

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

**OpenCV, 객체 추적 위한 편리한 API 제공:** 몇 줄의 코드로 추적 시스템 구축 가능

1. **비디오 캡처:** `cv2.VideoCapture` - 영상 입력 (카메라, 비디오 파일)
2. **ROI 설정:** `cv2.selectROI` - 초기 객체 영역 지정 (마우스)
3. **트래커 생성 및 초기화:** `cv2.TrackerXXX_create()`, `tracker.init()` - 알고리즘 선택, 초기화
4. **프레임 단위 추적:** `tracker.update()` - 매 프레임 객체 위치 추적
5. **결과 시각화:** `cv2.rectangle`, `cv2.putText`, `cv2.imshow` - bounding box, 텍스트 표시, 영상 출력
6. **사용자 입력 처리:** `cv2.waitKey` - 키보드 입력 처리 (알고리즘 변경, 종료 등)

**API 조합 ➡️ 효율적인 객체 추적 시스템 구축**

</div>

---

### 3.1. 비디오 캡처: `cv2.VideoCapture`

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

- **`cv2.VideoCapture(source)`:** 비디오 캡처 객체 생성

  - `source`: 입력 소스 지정

    - `0`, `1`, `2`, ... : 카메라 장치 인덱스 (0번: 기본 카메라)
    - `"video.mp4"`, `"path/to/video.avi"` : 비디오 파일 경로

  - 예시:
    ```python
    cap = cv2.VideoCapture(0) # 기본 카메라 연결
    cap = cv2.VideoCapture("my_video.mp4") # 비디오 파일 읽기
    ```

- **`cap.read()`:** 프레임 단위 영상 읽기

  - `ret, frame = cap.read()`
    - `ret`: 프레임 읽기 성공 여부 (True/False)
    - `frame`: 읽어온 프레임 (NumPy 배열)

- **`cap.get(propId)`:** 비디오 속성 정보 획득 (FPS, 해상도 등)

- **`cap.release()`:** 캡처 객체 해제 (자원 반환)

</div>

---

### 3.2. ROI 설정: `cv2.selectROI`

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

- **`cv2.selectROI(window_name, img, showCrosshair=True, fromCenter=False)`:** 사용자로부터 ROI 영역 선택

  - `window_name`: ROI 선택 창 제목
  - `img`: ROI 선택 대상 이미지 (프레임)
  - `showCrosshair`: ROI 선택 시 십자선 표시 여부
  - `fromCenter`: ROI 시작점 기준 (False: 좌상단, True: 중심)

  - **반환값:** `(x, y, w, h)` 튜플 (ROI 좌상단 좌표, 폭, 높이)

  - **사용법:**
    ```python
    roi = cv2.selectROI("Select ROI", frame)
    ```
    - 마우스 드래그로 ROI 지정
    - **Space bar** 또는 **Enter key:** ROI 확정
    - **ESC key** 또는 **c key:** ROI 취소

**본 실습 코드:** 스페이스바 입력 시 `cv2.selectROI` 호출, ROI 설정

</div>

---

### 3.3. 트래커 생성 및 초기화: `cv2.TrackerXXX_create()`, `tracker.init()`

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

- **`cv2.TrackerXXX_create()`:** 트래커 객체 생성 (XXX: 알고리즘 이름)

  - 예시:
    ```python
    tracker_kcf = cv2.TrackerKCF_create() # KCF 트래커 생성
    tracker_csrt = cv2.TrackerCSRT_create() # CSRT 트래커 생성
    ```

- **`tracker.init(img, bbox)`:** 트래커 초기화

  - `img`: 초기 프레임 이미지
  - `bbox`: 초기 객체 bounding box (ROI)

  - 예시:
    ```python
    tracker_kcf.init(frame, roi) # KCF 트래커 초기화
    ```

**트래커 객체 생성 후 반드시 초기화 필요 ➡️ 추적 준비 완료**

</div>

---

### 3.4. 프레임 단위 추적: `tracker.update()`

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

- **`tracker.update(img)`:** 새로운 프레임에서 객체 위치 추적

  - `img`: 현재 프레임 이미지

  - **반환값:** `ret, bbox = tracker.update(frame)`

    - `ret`: 추적 성공 여부 (True/False)
    - `bbox`: 추적된 bounding box (튜플), 실패 시 None

  - **사용법:**
    ```python
    success, bbox = tracker.update(frame)
    if success: # 추적 성공
        # bbox 좌표 활용 (객체 위치)
    else: # 추적 실패
        # 오류 처리 또는 재탐색 로직
    ```

**`tracker.update()` 반복 호출 ➡️ 지속적인 객체 위치 추적**

</div>

---

### 3.5. 결과 시각화: `cv2.rectangle`, `cv2.putText`, `cv2.imshow`

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

- **`cv2.rectangle(img, pt1, pt2, color, thickness)`:** 사각형 (bounding box) 그리기

  - `img`: 대상 이미지
  - `pt1`, `pt2`: 사각형 좌상단, 우하단 좌표
  - `color`: 사각형 색상 (BGR 튜플)
  - `thickness`: 선 두께 (음수: 채우기)

- **`cv2.putText(img, text, org, fontFace, fontScale, color, thickness)`:** 텍스트 표시

  - `img`: 대상 이미지
  - `text`: 출력 텍스트
  - `org`: 텍스트 시작 좌표
  - `fontFace`, `fontScale`, `color`, `thickness`: 폰트 스타일, 크기, 색상, 두께

- **`cv2.imshow(window_name, img)`:** 이미지 (프레임) 출력

  - `window_name`: 창 제목
  - `img`: 출력 이미지

**시각화 API 활용 ➡️ 추적 결과 직관적으로 확인**

</div>

---

### 3.6. 사용자 입력 처리: `cv2.waitKey`

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

- **`cv2.waitKey(delay)`:** 키보드 입력 대기

  - `delay`: 대기 시간 (ms, 0: 무한 대기)
  - **반환값:** 눌린 키의 ASCII 코드 값 (키 입력 없으면 -1)

  - **주요 활용:**
    - `key = cv2.waitKey(1)`: 1ms 대기, 연속 프레임 처리
    - `if key == 27:` (ESC 키): 프로그램 종료
    - `if key == ord('s'):` ('s' 키): 특정 기능 실행 (ROI 설정 등)
    - 숫자 키 입력: 알고리즘 변경

- **`cv2.destroyAllWindows()`:** 열린 모든 OpenCV 창 닫기 (프로그램 종료 시)

**`cv2.waitKey` ➡️ 사용자 인터랙션, 프로그램 제어**

</div>

---

## 1. 제공 코드 구조 및 기능 설명

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

### 전체 코드 흐름: 추적 과정 한눈에 보기

**[track_trackingAPI.py] 코드 핵심 로직:**

1. **초기 설정:**

   - 트래커 알고리즘 목록 정의 (`trackers`)
   - 트래커 선택 인덱스 초기화 (`trackerIdx = 0`)
   - 비디오 입력 소스 설정 (`video_src`)

2. **비디오 캡처 시작:** `cv2.VideoCapture(video_src)`

3. **프레임 처리 루프 (while cap.isOpened()):**

   - 프레임 읽기: `cap.read()`
   - **ROI 미설정 상태:** "Press the Space to set ROI!!" 텍스트 표시
   - **ROI 설정 완료:**
     - `tracker.update(frame)`: 객체 추적
     - 추적 성공: 초록색 bounding box 표시
     - 추적 실패: "Tracking fail." 텍스트 표시
   - 현재 트래커 알고리즘 이름 표시
   - 결과 프레임 출력: `cv2.imshow()`
   - 키 입력 처리: `cv2.waitKey()`
     - **Space bar:** ROI 설정 및 트래커 초기화
     - **0~7 숫자 키:** 트래커 알고리즘 변경 및 재초기화
     - **ESC 키:** 프로그램 종료

4. **자원 해제:** `cap.release()`, `cv2.destroyAllWindows()`

**➡️ 순차적인 단계별 처리, 명확한 구조**

</div>

---

### 주요 변수 및 객체: 코드 구성 요소 이해

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

- **`trackers` (list):** 트래커 생성 함수 리스트

  - `[cv2.TrackerKCF_create, cv2.TrackerCSRT_create, cv2.TrackerMIL_create, ...]`
  - 숫자 키 입력으로 선택될 알고리즘 함수 저장

- **`trackerIdx` (int):** 선택된 트래커 알고리즘 인덱스

  - `0`: KCF, `1`: CSRT, `2`: MIL ...

- **`tracker` (cv2.Tracker):** 생성된 트래커 객체

  - `tracker = trackers[trackerIdx]()`: 선택된 알고리즘으로 객체 생성

- **`video_src` (int/str):** 비디오 입력 소스

  - `0`: 카메라, `"video.mp4"`: 비디오 파일 경로

- **`cap` (cv2.VideoCapture):** 비디오 캡처 객체

- **`frame`, `img_draw` (NumPy array):** 프레임 이미지

  - `frame`: 원본 프레임, `img_draw`: 시각화 용 복사본

- **`roi`, `bbox` (tuple):** ROI, 추적된 bounding box 좌표

- **`isFirst` (bool):** 비디오 파일 최초 실행 여부 플래그 (자동 ROI 설정)

**변수 역할 이해 ➡️ 코드 분석 및 수정 용이**

</div>

---

### 주요 함수 및 OpenCV API: 코드 핵심 기능

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

- **비디오 입출력:**

  - `cv2.VideoCapture()`, `cap.isOpened()`, `cap.read()`, `cap.get()`, `cap.release()`

- **ROI 설정:**

  - `cv2.selectROI()`

- **트래커 객체 생성:**

  - `cv2.TrackerKCF_create()`, `cv2.TrackerCSRT_create()`, `cv2.TrackerMIL_create()`

- **트래커 초기화 및 추적:**

  - `tracker.init()`, `tracker.update()`

- **시각화:**

  - `cv2.rectangle()`, `cv2.putText()`, `cv2.imshow()`

- **사용자 입력 및 창 관리:**
  - `cv2.waitKey()`, `cv2.destroyAllWindows()`

**API 기능 숙지 ➡️ 코드 이해도 향상, 응용 가능성 확대**

</div>

---

### 코드 라인별 상세 분석: [track_trackingAPI.py]

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

**(코드 파일과 함께 슬라이드 내용 비교하며 학습)**

- **① 트래커 객체 생성자 함수 리스트 (Line 8-12):**

  ```python
  trackers = [
      cv2.TrackerKCF_create,
      cv2.TrackerCSRT_create,
      cv2.TrackerMIL_create
  ]
  ```

  - `trackers`: 사용 가능한 추적 알고리즘 함수를 리스트에 저장
  - `cv2.TrackerKCF_create`, `cv2.TrackerCSRT_create`, `cv2.TrackerMIL_create`: 각 알고리즘 생성 함수

- **② 비디오 파일과 카메라 선택 (Line 17-20):**

  ```python
  video_src = 0
  video_src = "/Users/string/Downloads/mark2latex/fastapi-project/insightbook.opencv_project_python/img/highway.mp4"
  cap = cv2.VideoCapture(video_src)
  ```

  - `video_src = 0`: 카메라 입력 (기본값)
  - `video_src = "..."`: 비디오 파일 경로 (주석 해제 시 비디오 파일 입력)
  - `cap = cv2.VideoCapture(video_src)`: `video_src`에 따라 카메라 또는 비디오 파일 연결

- **③ 새로운 프레임에서 추적 위치 찾기 (Line 60-66):**
  ```python
  ok, bbox = tracker.update(frame)
  (x,y,w,h) = bbox
  if ok: # 추적 성공
      cv2.rectangle(img_draw, (int(x), int(y)), (int(x + w), int(y + h)),
                     (0,255,0), 2, 1)
  else : # 추적 실패
      cv2.putText(img_draw, "Tracking fail.", (100,80),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2,cv2.LINE_AA)
  ```
  - `ok, bbox = tracker.update(frame)`: `tracker.update()` 호출, 추적 결과 반환
    - `ok`: 추적 성공 여부 (True/False)
    - `bbox`: 추적된 bounding box 좌표
  - 추적 성공 시 초록색 사각형, 실패 시 "Tracking fail." 텍스트 표시

</div>

---

### 코드 라인별 상세 분석 (계속): [track_trackingAPI.py]

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

- **④ 스페이스 바 또는 비디오 파일 최초 실행 (Line 52-57):**

  ```python
  if key == ord(' ') or (video_src != 0 and isFirst):
      isFirst = False
      roi = cv2.selectROI(win_name, frame, False)
      if roi[2] and roi[3]:
          tracker = trackers[trackerIdx]()
          isInit = tracker.init(frame, roi)
  ```

  - `key == ord(' ')`: 스페이스바 입력 시 ROI 설정
  - `(video_src != 0 and isFirst)`: 비디오 파일 최초 실행 시 자동 ROI 설정 (첫 프레임)
  - `roi = cv2.selectROI(...)`: `cv2.selectROI` 호출, ROI 설정
  - ROI 유효성 검사 (`roi[2] and roi[3]`) 후 트래커 생성 및 초기화

- **⑤ 트랙커 객체 생성 (Line 56):**

  ```python
  tracker = trackers[trackerIdx]()
  ```

  - `trackers[trackerIdx]()`: `trackers` 리스트에서 선택된 트래커 생성 함수 호출, 트래커 객체 생성

- **⑥ 0~7 숫자 입력 (Line 47-51):**

  ```python
  elif key in range(48, 56): # 0~7 숫자 입력
      trackerIdx = key-48     # 선택한 숫자로 트랙커 인덱스 수정
      if bbox is not None:
          tracker = trackers[trackerIdx]() # 선택한 숫자의 트랙커 객체 생성
          isInit = tracker.init(frame, bbox) # 이전 추적 위치로 추적 위치 초기화
  ```

  - 숫자 키 (0~7) 입력 시 트래커 알고리즘 변경
  - `trackerIdx = key - 48`: 입력된 숫자에 해당하는 인덱스로 변경
  - 기존 ROI (`bbox`) 존재 시, 새로운 알고리즘으로 트래커 재 생성 및 이전 ROI로 초기화

- **⑦ 선택한 숫자의 트랙커 객체 생성 (Line 50):**
  ```python
  tracker = trackers[trackerIdx]()
  ```
  - 숫자 키 입력에 따라 선택된 알고리즘으로 트래커 객체 생성 (알고리즘 변경)

**라인별 코드 분석 ➡️ 코드 작동 방식 완벽 이해**

</div>

---

## 2. 실습 환경 설정 및 코드 실행

<div class="overflow-y-auto max-h-[400px] border rounded p-4">
### 실습 준비 사항 점검: 필수 라이브러리 설치 확인

- **Python 환경:** Anaconda 또는 가상 환경 활성화 (권장)
- **OpenCV 설치:** `pip install opencv-python` 또는 `conda install opencv-python`
- **NumPy 설치:** `pip install numpy` 또는 `conda install numpy`

**터미널 또는 Anaconda Prompt 실행 후 다음 명령어로 설치 확인:**

```bash
pip list  # 또는 conda list
```

**OpenCV, numpy 목록에 있는지 확인. 미설치 시 설치 진행**

### 코드 파일 준비 및 실행

1. **코드 파일 다운로드:** `track_trackingAPI.py` 파일 다운로드

2. **실행 경로 이동:** 터미널에서 코드 파일 저장된 폴더로 이동 (`cd 경로`)

3. **코드 실행:**

   ```bash
   python track_trackingAPI.py
   ```

   또는

   ```bash
   python3 track_trackingAPI.py
   ```

**실행 성공 시 "Tracking APIs" 창 생성, 웹캠 영상 (또는 비디오 첫 프레임) 표시**

### 실행 화면 및 기본 조작법 숙지

- **실행 창 확인:** "Tracking APIs" 제목의 창 생성 확인
- **"Press the Space to set ROI!!" 메시지:** 창 상단 텍스트 확인
- **ROI 설정:** 스페이스바 누르고 마우스 드래그, Space 또는 Enter 키로 확정
- **객체 추적:** ROI 설정 후 객체 주변 초록색 사각형 표시, 객체 따라 움직임
- **알고리즘 변경:** 0~2 숫자 키 (KCF, CSRT, MIL) 눌러 알고리즘 변경 (창 상단 알고리즘 이름 변경 확인)
- **프로그램 종료:** ESC 키

**실습 환경 점검 및 기본 조작 숙지 ➡️ 본격적인 실습 준비 완료**

</div>

---

## 1. 기본 실습

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

### 실습 1: 다양한 추적 알고리즘 성능 비교

**목표:** KCF, CSRT, MIL 알고리즘 성능 비교, 장단점 체감

**실습 내용:**

1. `track_trackingAPI.py` 실행 후 ROI 설정
2. **0, 1, 2** 숫자 키 번갈아 누르며 알고리즘 변경 (KCF, CSRT, MIL)
3. 객체를 **다양하게 움직여보며** (천천히, 빠르게, 회전, 크기 변화) 각 알고리즘 추적 성능 관찰
4. **Occlusion 상황** (손으로 가리기, 물체 뒤로 숨기기) 에서 각 알고리즘 robustness 비교
5. **배경 변화** (복잡한 배경, 유사 색상 배경) 에 따른 알고리즘 성능 변화 관찰

**고려 사항:**

- 각 알고리즘별 추적 **성공률, 안정성, 속도** 주관적 비교
- 특정 상황 (빠른 움직임, Occlusion) 에 강한 알고리즘 파악
- 알고리즘 선택 기준 고민

**➡️ 알고리즘 특징 이해, 상황 적합성 판단 능력 향상**

### 실습 2: 비디오 입력 소스 변경

**목표:** 카메라 입력 ↔️ 비디오 파일 입력 변경, 입력 소스 차이 이해

**실습 내용:**

1. `track_trackingAPI.py` 코드 수정:
   - **카메라 입력 → 비디오 파일 입력:**
     ```python
     # video_src = 0  # 주석 처리
     video_src = "/path/to/your/video.mp4" # 비디오 파일 경로 설정, 주석 해제
     ```
   - **비디오 파일 입력 → 카메라 입력:**
     ```python
     video_src = 0  # 주석 해제
     # video_src = "/path/to/your/video.mp4" # 주석 처리
     ```
2. 수정 후 코드 재실행, 입력 소스 변경 확인
3. **다양한 비디오 파일** (움직임, 배경, 조명 변화 다양한 영상) 테스트, 알고리즘 성능 변화 관찰
4. **카메라 vs 비디오 파일 입력** 장단점 비교 분석

**고려 사항:**

- 비디오 파일 경로 정확하게 설정 (오류 발생 주의)
- 입력 소스 변화에 따른 추적 성능 변화, 알고리즘 robustness 차이 관찰
- 실시간 vs 오프라인 추적 차이점 이해

**➡️ 다양한 입력 환경 적응, 실제 응용 가능성 확장**

</div>

---

## 2. 심화 실습

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

### 실습 3: 추적 결과 시각화 개선

**목표:** `cv2.rectangle`, `cv2.putText` 활용, 시각 정보 풍부화

**실습 내용:**

1. **Bounding box 스타일 변경:**

   - 색상 변경: 초록색 → 파란색, 빨간색 등
   - 두께 변경: 2 → 1, 3, 5 등
   - 종류 변경: 실선 → 점선 (dotted rectangle 구현 - 도전 과제)

2. **추적 성공/실패 시각화:**

   - 추적 성공 시 초록색, 실패 시 빨간색 bounding box 표시 (조건문 활용)
   - 추적 실패 시 "Tracking Failed!" 텍스트 추가 표시

3. **FPS (Frame Per Second) 표시:**

   - 현재 FPS 계산하여 화면에 텍스트로 표시 (`cv2.getTickCount`, `cv2.getTickFrequency` 활용)

4. **객체 중심점 및 이동 경로 시각화 (도전 과제):**
   - 객체 중심점 표시 (작은 원 또는 점)
   - 중심점 이동 경로 선으로 연결 (`cv2.line` 활용, 이전 중심점 위치 저장 필요)

**고려 사항:**

- `cv2.rectangle`, `cv2.putText` API 파라미터 조정
- 조건문 활용, 추적 상태 따라 시각화 변경
- FPS 계산, 시간 측정 API 활용
- 도전 과제: 점선 사각형, 이동 경로 시각화

**➡️ 시각적 효과 극대화, 정보 전달력 향상, 사용자 인터페이스 개선**

</div>

---

### 실습 4: 새로운 추적 알고리즘 추가 및 비교

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

**목표:** OpenCV 제공 다른 추적 알고리즘 (Boosting, MedianFlow 등) 추가, 성능 비교

**실습 내용:**

1. `trackers` 리스트에 새로운 알고리즘 생성 함수 추가:
   ```python
   trackers = [
       cv2.TrackerKCF_create,
       cv2.TrackerCSRT_create,
       cv2.TrackerMIL_create,
       cv2.TrackerBoosting_create,  # Boosting 알고리즘 추가
       cv2.TrackerMedianFlow_create # MedianFlow 알고리즘 추가
       # ... 다른 알고리즘 추가 가능
   ]
   ```
2. 숫자 키 (3, 4, ...) 에 새로운 알고리즘 연결:
   ```python
   elif key in range(48, 56 + 추가 알고리즘 수): # 숫자 키 범위 수정
       trackerIdx = key-48
       # ... (트래커 생성 및 초기화 코드)
   ```
3. 추가된 알고리즘으로 객체 추적 실행, 기존 알고리즘과 성능 비교 (실습 1과 동일 방식)
4. 각 알고리즘 특징, 장단점 분석, 적합한 사용 환경 고려

**고려 사항:**

- OpenCV documentation 참고, 다양한 트래커 생성 함수 확인 ([https://docs.opencv.org/master/d9/df8/group\_\_tracking.html](https://docs.opencv.org/master/d9/df8/group__tracking.html))
- 알고리즘별 파라미터 튜닝 (심화 과정)
- 다양한 환경에서 성능 테스트, 객관적인 비교 시도

**➡️ 알고리즘 선택 폭 확대, 심층적인 알고리즘 이해**

</div>

---

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

## 추가 학습 자료

- **OpenCV 공식 문서:** [https://docs.opencv.org/master/](https://docs.opencv.org/master/)

  - **Tracking 모듈:** [https://docs.opencv.org/master/d9/df8/group\_\_tracking.html](https://docs.opencv.org/master/d9/df8/group__tracking.html) - 상세 API 설명, 알고리즘 이론
  - **튜토리얼:** [https://docs.opencv.org/master/d3/dc6/tutorial_py_table_of_contents_tracking.html](https://docs.opencv.org/master/d3/dc6/tutorial_py_table_of_contents_tracking.html) - Python 객체 추적 튜토리얼

- **OpenCV-Python Tutorials:** [https://opencv-python-tutroals.readthedocs.io/en/latest/](https://opencv-python-tutroals.readthedocs.io/en/latest/)

  - **Video Analysis in OpenCV:** 객체 추적, 배경 제거, 영상 분할 등 튜토리얼 제공

- **객체 추적 관련 온라인 강의:**

  - Coursera, Udemy, edX 등 온라인 교육 플랫폼 "object tracking", "computer vision" 검색

- **객체 추적 연구 논문:** Google Scholar ([https://scholar.google.com/](https://scholar.google.com/)) 에서 "object tracking", "visual tracking" 키워드 검색, 최신 연구 동향 파악

</div>
