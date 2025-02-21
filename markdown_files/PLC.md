---
title: "PLC"
css: style.css
tags:
  - datetime
---

## Python 기반 PLC 제어

### 목차

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

**PART 1. 개념 및 구조**

1.  MX Component란?
2.  컨트롤 리스트
3.  .dll 파일 (Python에서는 해당 없음)
4.  Communication Setup Utility

**PART 2. 프로그램**

1. 프로그램 설정
   1. 프로그래밍 과정 (Python 환경)
2. 프로그램 작성
   1. Python에서 사용 가능한 요소 (라이브러리 및 함수)
   2. Python으로 PLC 제어하기
   3. Python으로 PLC 데이터 읽어오기

</div>

---

## PART 1. 개념 및 구조

### 1. PLC 통신 아키텍처의 이해

### PLC 통신의 기본 구조

#### 1. 통신 계층 구조

1. **물리 계층**: Ethernet, RS-232 등의 물리적 연결
2. **데이터 링크 계층**: MC Protocol (MELSEC Communication Protocol)
3. **응용 계층**: MX Component API

---

#### 2. MC Protocol의 이해

- MC Protocol은 미쓰비시 PLC와 통신하기 위한 표준 프로토콜
- 프레임 구조:
  - 헤더 (Header)
  - 커맨드 (Command)
  - 서브커맨드 (Subcommand)
  - 데이터 (Data)
  - 체크섬 (Checksum)

---

### 2. 메모리 구조와 데이터 타입

#### 1. PLC 메모리 구조

- **비트(Bit) 메모리**: X, Y, M, B 등

  - 1비트 단위로 ON/OFF 저장
  - 주로 디지털 입출력에 사용

- **워드(Word) 메모리**: D, W, R 등
  - 16비트 단위로 데이터 저장
  - 아날로그 값, 카운터 값 등 저장

---

#### 2. 데이터 타입과 변환

```python
bit_data = 0 or 1 # 비트 데이터
word_data = -32768 to 32767 # 16비트 정수
dword_data = -2147483648 to 2147483647 # 32비트 정수
```

---

### 2. MX Component 소개

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

#### 2.1. MX Component란?

MX Component는 HOST PC와 미쓰비시 PLC 통신 모듈 간의 통신을 간편하게 만들어주는 툴입니다. 복잡한 통신 프로토콜(MC Protocol)을 직접 다루지 않고도 PLC와 통신할 수 있도록 기능을 제공합니다. RS-232C/485, Ethernet, CC-Link, USB, Modem 등 다양한 통신 방식을 지원합니다.

#### 2.2. 컨트롤 리스트

원문에서는 C# 환경의 ActiveX Control과 .NET Control을 설명하고 있지만, Python에서는 직접적인 컨트롤 개념 대신 **함수** 형태로 MX Component의 기능을 사용합니다.

MX Component는 다양한 기능을 제공하며, Python에서 주로 사용하는 기능은 다음과 같습니다.

**(1) 주요 기능 (Function List)**

| Function name         | Feature                                    |
| --------------------- | ------------------------------------------ |
| `Open()`              | 통신 라인을 엽니다.                        |
| `Close()`             | 통신 라인을 닫습니다.                      |
| `ReadDeviceBlock()`   | 다수의 디바이스 값을 읽어옵니다. (4-byte)  |
| `WriteDeviceBlock()`  | 다수의 디바이스에 값을 씁니다. (4-byte)    |
| `GetDevice()`         | 하나의 디바이스 값을 읽습니다. (4-byte)    |
| `SetDevice()`         | 하나의 디바이스에 값을 씁니다. (4-byte)    |
| `ReadBuffer()`        | 특수 기능 모듈 버퍼 메모리에서 데이터 읽기 |
| `WriteBuffer()`       | 특수 기능 모듈 버퍼 메모리에 값 쓰기       |
| `GetClockData()`      | PLC CPU 시간 데이터 읽기 (년월일시)        |
| `SetClockData()`      | PLC CPU 시간 데이터 쓰기 (년월일시)        |
| `SetCpuStatus()`      | PLC CPU Remote RUN/STOP/PAUSE 설정         |
| `EntryDeviceStatus()` | 상태 모니터링 디바이스 등록                |
| `FreeDeviceStatus()`  | 상태 모니터링 디바이스 등록 취소           |
| `OnDeviceStatus()`    | 등록된 장치 상태에 따른 이벤트 알람 실행   |
| `ReadDeviceBlock2()`  | 다수의 디바이스 값을 읽어옵니다. (2-byte)  |
| `WriteDeviceBlock2()` | 다수의 디바이스에 값을 씁니다. (2-byte)    |
| `GetDevice2()`        | 하나의 디바이스 값을 읽습니다. (2-byte)    |
| `SetDevice2()`        | 하나의 디바이스에 값을 씁니다. (2-byte)    |
| `GetErrorMessage()`   | 오류 설명 및 오류 코드 읽기                |

> **참고:** `GetDevice`와 `GetDevice2`, `SetDevice`와 `SetDevice2`, `ReadDeviceBlock`와 `ReadDeviceBlock2`, `WriteDeviceBlock`와 `WriteDeviceBlock2` 함수는 데이터 크기에 따라 선택하여 사용합니다. `2`가 붙은 함수는 2-byte (short), 그렇지 않은 함수는 4-byte (int) 데이터를 처리합니다.

</div>

---

#### 2.3 미쓰비시 PLC 디바이스 메모리 종류 및 특징

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

미쓰비시 PLC에서 사용되는 주요 디바이스 메모리 종류와 특징은 다음과 같습니다:

| 디바이스 | 설명               | 특징                                                                                |
| -------- | ------------------ | ----------------------------------------------------------------------------------- |
| X        | 입력 릴레이        | - 외부 입력 신호를 받는 디바이스<br>- 읽기 전용<br>- 16점 단위로 할당               |
| Y        | 출력 릴레이        | - 외부 출력 신호를 제어하는 디바이스<br>- 읽기/쓰기 가능<br>- 16점 단위로 할당      |
| M        | 내부 릴레이        | - PLC 내부에서 사용되는 비트 디바이스<br>- 읽기/쓰기 가능<br>- 래치 영역 설정 가능  |
| L        | 래치 릴레이        | - 전원 OFF 시에도 상태가 유지되는 비트 디바이스<br>- 읽기/쓰기 가능                 |
| F        | 애넌시에이터       | - 알람 표시 등에 사용되는 비트 디바이스<br>- 읽기/쓰기 가능                         |
| B        | 링크 릴레이        | - 네트워크 통신용 비트 디바이스<br>- 읽기/쓰기 가능                                 |
| D        | 데이터 레지스터    | - 16비트 데이터 저장용 워드 디바이스<br>- 읽기/쓰기 가능<br>- 수치 연산에 주로 사용 |
| W        | 링크 레지스터      | - 네트워크 통신용 워드 디바이스<br>- 읽기/쓰기 가능                                 |
| R        | 파일 레지스터      | - 대용량 데이터 저장용 워드 디바이스<br>- 읽기/쓰기 가능<br>- 확장 메모리 영역      |
| ZR       | 확장 파일 레지스터 | - R 디바이스의 확장 영역<br>- 더 큰 용량의 데이터 저장 가능                         |
| T        | 타이머             | - 시간 측정용 디바이스<br>- 현재값(TN)과 접점(TS)으로 구성                          |
| C        | 카운터             | - 개수 계산용 디바이스<br>- 현재값(CN)과 접점(CS)으로 구성                          |

> **참고:**
>
> - 각 디바이스의 사용 가능한 점수는 PLC CPU 기종에 따라 다릅니다.
> - 비트 디바이스(X,Y,M 등)는 ON/OFF 값만 저장할 수 있습니다.
> - 워드 디바이스(D,W,R 등)는 16비트 정수값을 저장할 수 있습니다.

</div>

---

#### 2.3. .dll 파일 (Python 환경)

C#에서는 `.dll` 파일을 참조해야 MX Component를 사용할 수 있지만, Python에서는 **pywin32** 라이브러리를 사용하여 Windows COM (Component Object Model) 객체를 직접 제어하는 방식으로 MX Component를 활용합니다.

따라서 Python 환경에서는 특정 `.dll` 파일을 직접 참조하는 과정은 필요하지 않습니다. 대신, **MX Component가 PC에 설치되어 있어야** Python 코드를 통해 PLC와 통신할 수 있습니다.

---

#### 2.4. Communication Setup Utility

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Communication Setup Utility는 MX Component를 설정하는 프로그램으로, Python에서 PLC와 통신하기 전에 반드시 설정을 완료해야 합니다.

**(1) 프로그램 실행**

Communication Setup Utility는 MX Component 설치 시 함께 설치됩니다. **반드시 관리자 권한으로 실행**해야 모든 기능을 정상적으로 사용할 수 있습니다.

**(2) 프로그램 구성 요소**

- **Menu**
  - **Target setting**: MX Component로 통신할 PLC Target을 생성하는 화면을 표시합니다.
  - **List view**: Target setting에서 생성한 PLC target 목록을 보여줍니다.
  - **Connection test**: Target setting에서 생성한 PLC target과의 통신을 테스트합니다.
- **Help**: 설치된 MX Component 정보를 표시합니다.
- **Target setting**: 생성된 Target PLC 목록을 표시합니다.
  - **Logical station number**: Target PLC 번호 (Wizard 생성 시 설정).
  - **Wizard**: Target PLC 생성을 위한 마법사 실행.
  - **Delete**: 생성한 Target PLC 삭제.
- **List view**: 생성된 Target PLC 목록을 리스트 형태로 보여줍니다.
  - **Wizard**: Target PLC 생성을 위한 마법사 실행.
  - **Delete**: 생성한 Target PLC 삭제.
- **Connection test**: Target PLC와의 통신 테스트를 수행합니다.
  - **Logical station number**: 테스트할 Target PLC 번호 선택.
  - **test**: 통신 테스트 실행.
  - **Result**: 통신 결과 표시.

</div>

---

**(3) Target PLC 생성하기**

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

1. **Wizard** 버튼을 클릭합니다. (Target setting 또는 List view에서 클릭 가능)

2. **Logical station number**를 입력하고 **Next**를 클릭합니다.

   > **Logical station number**: Target PLC를 식별하는 주소 역할을 합니다. Python 프로그램에서 PLC를 지정할 때 사용됩니다.

3. **Target PLC와의 통신 방법**을 설정합니다.

   - **PC side I/F**: **Ethernet**으로 설정합니다. (PC가 Ethernet으로 PLC와 통신하므로)
     > USB 또는 RS-232C 통신 시 해당 방식으로 선택합니다.
   - **Connect module**: **CPU module** 선택 (Q03UDV는 Ethernet 포트 내장 CPU).
   - **Protocol**: **TCP** 선택.
   - **Time out**: 적절한 시간 설정 (기본값 60000ms (60초), 예시에서는 6000ms (6초)로 설정).

4. **PLC side I/F**를 설정합니다.

   - **PLC side I/F**: **CPU module**로 지정 (Q03UDV PLC 자체 Ethernet 포트 사용).
   - **IP address**: PLC의 IP 주소를 입력합니다. (미쓰비시 PLC 기본 IP: 192.168.3.39)
     > 실제 PLC의 IP 주소에 맞게 설정해야 합니다.

5. **Station type**과 **CPU type**을 설정합니다.

   - **Station type**: **Host station** 선택 (Q03UDV PLC CPU 단독 사용).
   - **CPU type**: **Q03UDV** 선택 (사용하는 PLC CPU 모델에 맞게 선택).
   - **Multiple CPU**: **None** 선택 (해당 없음).

6. **Comment**를 입력합니다. (선택 사항, 연결에 대한 설명을 적으면 편리합니다.)

7. **Finish**를 클릭하여 Target PLC 등록을 완료합니다.

</div>

---

**(4) GX Simulator2를 Target PLC로 사용 (PLC 없이 테스트)**

실제 PLC 장비가 없는 경우, GX-Works2의 시뮬레이션 툴인 **GX-Simulator2**를 Target PLC로 설정하여 통신 테스트를 할 수 있습니다.

Target PLC 생성 과정에서 **PC side I/F**를 **GX Simulator2**로 지정하고, **Target Simulator**를 **Simulator A**로 선택합니다.

---

## PART 2. 프로그램

### 1. 프로그램 설정

#### 1.1. 프로그래밍 과정 (Python 환경)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

1. **Python 개발 환경 설정**: 32bit 기반의 Python과 `pywin32` 라이브러리가 설치되어 있어야 합니다.

   ```bash
   $ set CONDA_FORCE_32BIT=1
   $ conda create -n plc python=3.9
   $ conda activate plc
   $ pip install pywin32
   $ python
   ```

> 32bit가 나타나는지 확인! 안 될 시 재설치

1. **MX Component 설치 및 Communication Setup Utility 설정**: PC에 MX Component를 설치하고, Communication Setup Utility를 통해 Target PLC를 설정합니다.

1. **Python 코드 작성**: Python 스크립트 파일(`.py`)을 생성하고, `pywin32` 라이브러리를 사용하여 MX Component COM 객체를 제어하는 코드를 작성합니다.

</div>

---

### 2. 프로그램 작성

#### 2.1. Python에서 사용 가능한 요소 (라이브러리 및 함수)

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Python에서 MX Component를 제어하기 위해 `pywin32` 라이브러리를 사용합니다.

| 요소              | 주요 명령어                                            | 기능                                |
| ----------------- | ------------------------------------------------------ | ----------------------------------- |
| **COM 객체 생성** | `win32com.client.Dispatch("ActUtlTypeLib.ActUtlType")` | MX Component COM 객체를 생성합니다. |
| **통신 접속**     | `ActUtlType.Open()`                                    | PLC와 통신을 시작합니다.            |
| **디바이스 제어** | `ActUtlType.SetDevice("디바이스", 값)`                 | PLC 디바이스 값을 설정합니다.       |
| **디바이스 읽기** | `ActUtlType.GetDevice("디바이스")`                     | PLC 디바이스 값을 읽어옵니다.       |
| **통신 종료**     | `ActUtlType.Close()`                                   | PLC와의 통신을 종료합니다.          |

</div>

---

#### 2.2. Python으로 PLC 제어하기

Python으로 PLC를 제어하는 기본적인 예제 코드를 살펴보겠습니다.

##### 2.2.1 PLC 연결 코드

```python
import win32com.client

# COM 객체 생성
act = win32com.client.Dispatch("ActUtlType.ActUtlType")

# 논리 국번 설정 (Communication Setup Utility에서 설정한 번호)
act.ActLogicalStationNumber = 0

# 연결 시도
result = act.Open()

if result == 0:
    print("PLC 연결 성공!")
```

---

##### 2.2.2 PLC 메모리 읽기 코드

```python
import win32com.client

act = win32com.client.Dispatch("ActUtlType.ActUtlType")
act.ActLogicalStationNumber = 0
result = act.Open()

if result == 0:
    # 입력 상태 읽기
    x0_status = act.GetDevice("X0")    # X0 입력 상태 읽기
    x1_status = act.GetDevice("X1")    # X1 입력 상태 읽기
    print(f"X0 상태: {x0_status}")
    print(f"X1 상태: {x1_status}")
```

---

##### 2.2.3 PLC 메모리 쓰기 코드

```python
import win32com.client

act = win32com.client.Dispatch("ActUtlType.ActUtlType")
act.ActLogicalStationNumber = 0
result = act.Open()

if result == 0:
    # 입력 상태 읽기
    x0_status = act.GetDevice("X0")    # X0 입력 상태 읽기
    x1_status = act.GetDevice("X1")    # X1 입력 상태 읽기
    print(f"X0 상태: {x0_status}")
    print(f"X1 상태: {x1_status}")

    # 출력 제어
    act.SetDevice("Y0", 1)    # Y0 출력 ON
    act.SetDevice("Y1", 0)    # Y1 출력 OFF


    # 출력 상태 읽기
    y0_status = act.GetDevice("Y0")
    y1_status = act.GetDevice("Y1")
    print(f"Y0 상태: {y0_status}")
    print(f"Y1 상태: {y1_status}")

act.Close()
```

---

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

**코드 설명:**

1. **`import win32com.client`**: `pywin32` 라이브러리에서 COM 클라이언트 모듈을 임포트합니다.
2. **`ActUtlType = win32com.client.Dispatch("ActUtlTypeLib.ActUtlType")`**: MX Component의 `ActUtlType` COM 객체를 생성합니다. 이 객체를 통해 PLC 제어 기능을 사용할 수 있습니다.
3. **`ActUtlType.ActLogicalStationNumber = 0`**: Communication Setup Utility에서 설정한 **Logical Station Number**를 설정합니다. **반드시 실제 설정한 번호와 일치해야 합니다.**
4. **`ActUtlType.Open()`**: PLC와 통신을 시작합니다. 반환값(`ret`)이 0이면 성공, 0이 아니면 에러입니다.
5. **`ActUtlType.SetDevice("M0", 1)` / `ActUtlType.SetDevice("M1", 0)`**: `SetDevice()` 함수를 사용하여 PLC의 **M0 디바이스를 ON (값 1)**, **M1 디바이스를 OFF (값 0)** 합니다. 첫 번째 인자는 디바이스 주소, 두 번째 인자는 설정할 값입니다. 반환값(`ret`)으로 성공 여부를 확인합니다.
6. **`ActUtlType.Close()`**: PLC와의 통신을 종료합니다.

> **주의:**
>
> - **Logical Station Number**: Communication Setup Utility에서 설정한 값을 정확하게 입력해야 합니다.
> - **에러 처리**: `Open()`, `SetDevice()`, `Close()` 등의 함수는 반환값으로 작업 성공 여부를 알려줍니다. 반환값이 0이 아니면 에러가 발생한 것이므로, 에러 코드를 확인하여 문제 해결에 참고해야 합니다. MX Component 매뉴얼에서 에러 코드에 대한 자세한 정보를 확인할 수 있습니다.

</div>

---

##### 2.2.4 PLC 메모리 버퍼 접근 코드

```python
import win32com.client
import array

# ActUtlType COM 객체 생성
act = win32com.client.Dispatch("ActUtlType.ActUtlType")
act.ActLogicalStationNumber = 0
result = act.Open()

if result == 0:
    # 버퍼 메모리 읽기/쓰기
    buffer_size = 10
    # Convert list to array of integers
    write_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Use regular list instead of array
    read_data = []
    for i in range(buffer_size):
        read_data.append(act.GetDevice(f"D{i}"))
    print(f"읽은 데이터: {read_data}")
    # D0부터 10개의 워드 데이터 쓰기
    for i, value in enumerate(write_data):
        result = act.SetDevice(f"D{i}", value)  # Write values one by one
        if result != 0:
            print(f"D{i} 쓰기 실패, 에러 코드: {result}")
            break
    else:  # Only runs if no break occurred
        print("버퍼 메모리 쓰기 성공")

        # D0부터 10개의 워드 데이터 읽기
        read_data = []
        for i in range(buffer_size):
            read_data.append(act.GetDevice(f"D{i}"))
        print(f"읽은 데이터: {read_data}")

    act.Close()
else:
    print(f"PLC 연결 실패, 에러 코드: {result}")
```

---

```python
import win32com.client
import array

# ActUtlType COM 객체 생성
act = win32com.client.Dispatch("ActUtlType.ActUtlType")
act.ActLogicalStationNumber = 0
result = act.Open()

if result == 0:
    # 버퍼 메모리 읽기/쓰기
    buffer_size = 10
    write_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    read_data = array.array('h', [0] * buffer_size)  # 읽기용 버퍼 생성

    # ReadBuffer로 한번에 읽기
    result = act.ReadBuffer(0, buffer_size, read_data)
    if result == 0:
        print(f"읽은 데이터: {list(read_data)}")
    else:
        print(f"읽기 실패, 에러 코드: {result}")

    # WriteBuffer로 한번에 쓰기
    write_buffer = array.array('h', write_data)
    result = act.WriteBuffer(0, buffer_size, write_buffer)
    if result == 0:
        print("버퍼 메모리 쓰기 성공")

        # 쓴 데이터 다시 읽기
        result = act.ReadBuffer(0, buffer_size, read_data)
        if result == 0:
            print(f"읽은 데이터: {list(read_data)}")
        else:
            print(f"읽기 실패, 에러 코드: {result}")
    else:
        print(f"쓰기 실패, 에러 코드: {result}")

    act.Close()
else:
    print(f"PLC 연결 실패, 에러 코드: {result}")
```

---

##### 2.2.5 그외 예제

```python
import win32com.client

# COM 객체 생성 및 연결
act = win32com.client.Dispatch("ActUtlType.ActUtlType")
act.ActLogicalStationNumber = 0
result = act.Open()

if result == 0:
    try:
        # 1. X (입력 릴레이) - 읽기 전용
        x0_status = act.GetDevice("X0")    # X0 입력 상태 읽기
        print(f"X0 상태: {x0_status}")

        # 2. Y (출력 릴레이) - 읽기/쓰기
        y0_status = act.GetDevice("Y0")    # Y0 상태 읽기
        print(f"Y0 상태: {y0_status}")
        act.SetDevice("Y0", 1)             # Y0 출력 ON
        y0_status = act.GetDevice("Y0")    # Y0 상태 읽기
        print(f"Y0 상태: {y0_status}")

        # 3. M (내부 릴레이) - 읽기/쓰기
        m0_status = act.GetDevice("M0")    # M0 상태 읽기
        print(f"M0 상태: {m0_status}")
        act.SetDevice("M0", 1)             # M0 ON
        m0_status = act.GetDevice("M0")    # M0 상태 읽기
        print(f"M0 상태: {m0_status}")

        # 4. L (래치 릴레이) - 읽기/쓰기 (전원 OFF 시에도 유지)
        l0_status = act.GetDevice("L0")    # L0 상태 읽기
        print(f"L0 상태: {l0_status}")
        act.SetDevice("L0", 1)             # L0 ON
        l0_status = act.GetDevice("L0")    # L0 상태 읽기
        print(f"L0 상태: {l0_status}")

        # 5. F (애넌시에이터) - 읽기/쓰기
        f0_status = act.GetDevice("F0")    # F0 상태 읽기
        print(f"F0 상태: {f0_status}")
        act.SetDevice("F0", 1)             # F0 ON
        f0_status = act.GetDevice("F0")    # F0 상태 읽기
        print(f"F0 상태: {f0_status}")

        # 6. B (링크 릴레이) - 읽기/쓰기
        b0_status = act.GetDevice("B0")    # B0 상태 읽기
        print(f"B0 상태: {b0_status}")
        act.SetDevice("B0", 1)             # B0 ON
        b0_status = act.GetDevice("B0")    # B0 상태 읽기
        print(f"B0 상태: {b0_status}")

        # 7. D (데이터 레지스터) - 읽기/쓰기 (16비트 정수)
        d0_value = act.GetDevice("D0")     # D0 값 읽기
        print(f"D0 값: {d0_value}")
        act.SetDevice("D0", 12345)         # D0에 값 쓰기
        d0_value = act.GetDevice("D0")     # D0 값 읽기
        print(f"D0 값: {d0_value}")

        # 8. W (링크 레지스터) - 읽기/쓰기
        w0_value = act.GetDevice("W0")     # W0 값 읽기
        print(f"W0 값: {w0_value}")
        act.SetDevice("W0", 100)           # W0에 값 쓰기
        w0_value = act.GetDevice("W0")     # W0 값 읽기
        print(f"W0 값: {w0_value}")

        # 9. R (파일 레지스터) - 읽기/쓰기
        r0_value = act.GetDevice("R0")     # R0 값 읽기
        print(f"R0 값: {r0_value}")
        act.SetDevice("R0", 500)           # R0에 값 쓰기
        r0_value = act.GetDevice("R0")     # R0 값 읽기
        print(f"R0 값: {r0_value}")

        # 10. ZR (확장 파일 레지스터) - 읽기/쓰기
        zr0_value = act.GetDevice("ZR0")   # ZR0 값 읽기
        print(f"ZR0 값: {zr0_value}")
        act.SetDevice("ZR0", 1000)         # ZR0에 값 쓰기
        zr0_value = act.GetDevice("ZR0")   # ZR0 값 읽기
        print(f"ZR0 값: {zr0_value}")

        # 11. T (타이머) - 현재값(TN)과 접점(TS) 읽기/쓰기
        t0_current = act.GetDevice("TN0")  # T0 타이머 현재값
        # 타이머 접점 상태 읽기
        t0_status = act.GetDevice("TS0")   # T0 타이머 접점 상태
        print(f"T0 현재값: {t0_current}, 접점상태: {t0_status}")

        # 타이머 설정값 쓰기
        t0_current = act.GetDevice("TN0")  # T0 타이머 현재값
        # 타이머 접점 상태 읽기
        t0_status = act.GetDevice("TS0")   # T0 타이머 접점 상태
        print(f"T0 현재값: {t0_current}, 접점상태: {t0_status}")

        act.SetDevice("T0", 100)           # T0 타이머 설정값 쓰기
        # 타이머 현재값 읽기
        t0_current = act.GetDevice("TN0")  # T0 타이머 현재값
        # 타이머 접점 상태 읽기
        t0_status = act.GetDevice("TS0")   # T0 타이머 접점 상태
        print(f"T0 현재값: {t0_current}, 접점상태: {t0_status}")

        # 12. C (카운터) - 현재값(CN)과 접점(CS) 읽기/쓰기
        # 카운터 설정값 쓰기
        # 카운터 현재값 읽기
        c0_current = act.GetDevice("CN0")  # C0 카운터 현재값
        # 카운터 접점 상태 읽기
        c0_status = act.GetDevice("CS0")   # C0 카운터 접점 상태
        print(f"C0 현재값: {c0_current}, 접점상태: {c0_status}")

        act.SetDevice("C0", 10)            # C0 카운터 설정값 쓰기
        # 카운터 현재값 읽기
        c0_current = act.GetDevice("CN0")  # C0 카운터 현재값
        # 카운터 접점 상태 읽기
        c0_status = act.GetDevice("CS0")   # C0 카운터 접점 상태
        print(f"C0 현재값: {c0_current}, 접점상태: {c0_status}")

    except Exception as e:
        print(f"에러 발생: {e}")
    finally:
        act.Close()  # 연결 종료
else:
    print(f"PLC 연결 실패, 에러 코드: {result}")
```

---

그외 코드 구조 및 참고 사항

> **`try...except`**: `GetDevice()` 함수 실행 중 오류가 발생할 수 있으므로 `try...except` 블록으로 감싸서 예외 처리를 합니다. 오류 발생 시 오류 메시지를 출력합니다.

> **실시간 데이터 읽기**: PLC 데이터를 실시간으로 주기적으로 읽어오려면, Python의 `time.sleep()` 함수와 `while` 루프 또는 스레딩, 비동기 프로그래밍 등을 활용하여 주기적인 데이터 갱신 코드를 작성할 수 있습니다.

---

**다음 단계**:

- **예제 프로젝트**: 위에서 설명한 내용을 바탕으로, 버튼 클릭으로 PLC 램프를 ON/OFF 하거나, PLC 데이터 값을 읽어와서 화면에 표시하는 간단한 GUI 프로그램을 Python (Tkinter, PyQt 등) 라이브러리를 사용하여 만들어 볼 수 있습니다.
- **심화 학습**: MX Component의 다양한 기능 (다수의 디바이스 읽기/쓰기, 버퍼 메모리 접근, 시간 데이터 처리 등)을 학습하고, 실제 산업 현장에서 필요한 PLC 제어 프로그램을 개발해 볼 수 있습니다.

---

##### Tkinter 사용 예제

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

Python의 Tkinter를 사용하여 간단한 GUI 기반의 PLC 제어 프로그램을 만들어보겠습니다. 이 예제는 다음과 같은 기능을 포함합니다:

1. **PLC 연결/해제**: GUI 버튼으로 PLC와의 연결을 제어
2. **연결 상태 표시**: 현재 PLC 연결 상태를 실시간으로 표시
3. **M0 디바이스 제어**: 버튼으로 M0 디바이스를 ON/OFF 제어
4. **실시간 상태 모니터링**: M0 디바이스의 상태를 주기적으로 업데이트

**주요 클래스 및 함수 설명:**

- **`MXComponent` 클래스**: PLC 통신을 담당하는 클래스

  - `connect()`: PLC 연결 설정
  - `disconnect()`: PLC 연결 해제
  - `set_device()`: PLC 디바이스 값 쓰기
  - `get_device()`: PLC 디바이스 값 읽기

- **GUI 요소:**

  - `status_label`: PLC 연결 상태 표시
  - `connect_btn`: PLC 연결/해제 버튼
  - `m0_btn`: M0 디바이스 ON/OFF 토글 버튼
  - `m0_label`: M0 디바이스 현재 상태 표시

- **주기적 업데이트:**
  - `update_m0_status()` 함수가 100ms 간격으로 M0 상태를 갱신

</div>

---

```python
import win32com.client
import time
import tkinter as tk
from tkinter import ttk

class MXComponent:
    def __init__(self):
        # ActUtlType COM 객체 생성
        self.act = win32com.client.Dispatch("ActUtlType.ActUtlType")

        # 통신 상태 변수
        self.connected = False

        # 논리 스테이션 번호
        self.station_number = 1

    def connect(self):
        """PLC 연결"""
        if not self.connected:
            # 논리 스테이션 번호 설정
            self.act.ActLogicalStationNumber = self.station_number

            # 통신 열기
            ret = self.act.Open()
            if ret == 0:
                self.connected = True
                # M0 디바이스 ON
                self.set_device("M0", 1)
                return True
        return False

    def disconnect(self):
        """PLC 연결 해제"""
        if self.connected:
            # M0 디바이스 OFF
            self.set_device("M0", 0)

            # 통신 닫기
            self.act.Close()
            self.connected = False
            return True
        return False

    def set_device(self, device, value):
        """PLC 디바이스 값 쓰기"""
        if self.connected:
            ret = self.act.SetDevice(device, value)
            return ret == 0
        return False

    def get_device(self, device):
        """PLC 디바이스 값 읽기"""
        if self.connected:
            ret = self.act.GetDevice(device)
            if isinstance(ret, tuple):
                return ret
            return ret
        return None

if __name__ == "__main__":
    # GUI 생성
    root = tk.Tk()
    root.title("PLC Control")
    root.geometry("300x200")

    # MXComponent 인스턴스 생성
    plc = MXComponent()

    # 연결 상태 표시 라벨
    status_label = ttk.Label(root, text="연결 상태: 미연결")
    status_label.pack(pady=10)

    # 연결/해제 버튼
    def toggle_connection():
        if not plc.connected:
            if plc.connect():
                status_label.config(text="연결 상태: 연결됨")
                connect_btn.config(text="연결 해제")
        else:
            if plc.disconnect():
                status_label.config(text="연결 상태: 미연결")
                connect_btn.config(text="연결")

    connect_btn = ttk.Button(root, text="연결", command=toggle_connection)
    connect_btn.pack(pady=10)

    # M0 상태 제어
    def toggle_m0():
        if plc.connected:
            current_value = plc.get_device("M0")
            if current_value is not None:  # None 체크 추가
                new_value = 0 if current_value == (0,1) else 1
                plc.set_device("M0", new_value)
                update_m0_status()

    def update_m0_status():
        if plc.connected:
            value = plc.get_device("M0")
            if value is not None:  # None 체크 추가
                m0_label.config(text=f"M0 상태: {value}")
        root.after(100, update_m0_status)  # 100ms마다 상태 업데이트

    m0_btn = ttk.Button(root, text="M0 토글", command=toggle_m0)
    m0_btn.pack(pady=10)

    m0_label = ttk.Label(root, text="M0 상태: -")
    m0_label.pack(pady=10)

    # 초기 상태 업데이트 시작
    update_m0_status()

    root.mainloop()
```

---

##### 4. tkinter 사용 방법

```python
import tkinter as tk
from tkinter import ttk

# 메인 윈도우 생성
root = tk.Tk()
root.title("PLC 제어 프로그램")
root.geometry("400x300")  # 윈도우 크기 설정

# 라벨 생성
label = ttk.Label(root, text="안녕하세요")
label.pack(pady=10)

# 버튼 생성
def button_click():
    print("버튼이 클릭되었습니다!")

button = ttk.Button(root, text="클릭하세요", command=button_click)
button.pack(pady=10)

# 입력 필드 생성
entry = ttk.Entry(root)
entry.pack(pady=10)

# 콤보박스 생성
combo = ttk.Combobox(root, values=["옵션1", "옵션2", "옵션3"])
combo.pack(pady=10)

# 프레임 생성
frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

# 체크박스 생성
check_var = tk.BooleanVar()
checkbox = ttk.Checkbutton(frame, text="체크박스", variable=check_var)
checkbox.pack(pady=5)

# 메인 이벤트 루프 시작
root.mainloop()
```

---

<div class="overflow-y-auto max-h-[400px] border rounded p-4">
주요 위젯 설명:

- Label: 텍스트나 이미지를 표시
- Button: 클릭 가능한 버튼
- Entry: 한 줄 텍스트 입력 필드
- Combobox: 드롭다운 선택 메뉴
- Frame: 다른 위젯을 그룹화하는 컨테이너
- Checkbutton: 체크박스

배치 관리자:

- pack(): 위젯을 순차적으로 배치
- grid(): 행과 열로 위젯을 배치
- place(): 절대 좌표로 위젯을 배치

</div>
