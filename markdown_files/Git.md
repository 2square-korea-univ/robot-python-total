---
title: "Git"
css: style.css
tags:
  - datetime
---

## Git 강의 자료

**목차:**

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

1. **버전 관리 시스템 (VCS) 이란?**

   - 버전 관리 시스템의 필요성
   - Git의 등장 배경 및 특징
   - 중앙 집중형 vs 분산형 버전 관리 시스템
   - Git의 장점

2. **Git 설치 및 기본 설정**

   - Git 설치 (Windows, macOS, Linux)
   - Git 설정 (사용자 이름, 이메일 설정)
   - Git 명령어 기본 구조

3. **Git 기본 워크플로우 (Local Repository)**

   - 저장소 (Repository) 개념 이해
   - `git init`: 로컬 저장소 생성
   - `git status`: 저장소 상태 확인
   - `git add`: 변경 사항 스테이징 (Staging Area)
   - `git commit`: 커밋 (Commit) - 변경 사항 기록
   - 커밋 메시지 작성 규칙
   - `git log`: 커밋 기록 확인
   - `.gitignore`: 파일 무시 설정

4. **브랜치 (Branch)**

   - 브랜치 개념 및 필요성 (독립적인 작업 공간)
   - `git branch`: 브랜치 확인 및 생성
   - `git checkout`: 브랜치 이동 및 생성
   - `git merge`: 브랜치 병합
   - 브랜치 전략 (Git Flow, GitHub Flow 등) 소개

5. **원격 저장소 (Remote Repository)**

   - 원격 저장소 개념 (GitHub, GitLab, Bitbucket 등)
   - `git clone`: 원격 저장소 복제
   - `git remote`: 원격 저장소 관리
   - `git push`: 로컬 변경 사항 원격 저장소에 반영
   - `git pull`: 원격 저장소 변경 사항 로컬 저장소에 반영
   - 협업 워크플로우 (Pull Request, Merge Request) 기본

6. **Git 심화 활용**

   - `git diff`: 변경 사항 비교
   - `git reset`: 커밋 되돌리기 (다양한 옵션)
   - `git revert`: 특정 커밋 되돌리기 (새로운 커밋 생성)
   - `git stash`: 변경 사항 임시 저장
   - `git tag`: 특정 시점 태그 지정
   - `git rebase`: 브랜치 재정렬 (고급)
   - 충돌 (Conflict) 해결 방법

7. **협업 환경에서의 Git 활용**

   - 팀 협업 워크플로우 구축
   - 코드 리뷰 프로세스
   - 브랜치 전략 활용 심화
   - GitHub/GitLab 프로젝트 활용

8. **Git GUI 툴 소개 (선택 사항)**

   - SourceTree, GitKraken, GitHub Desktop 등 소개 및 간단 사용법

9. **Git 학습 자료 및 추가 정보**
   - 공식 Git 문서
   - 온라인 Git 강좌 및 튜토리얼
   - Git 관련 커뮤니티

</div>

---

### 1. 버전 관리 시스템 (VCS) 이란?

#### 1.1 버전 관리 시스템의 필요성

- **변경 이력 관리:** 파일 변경 사항을 시간 순서대로 기록하고, 특정 시점으로 되돌릴 수 있도록 합니다.
- **협업 효율성 증대:** 여러 사람이 동시에 작업하는 프로젝트에서 변경 사항 충돌을 방지하고, 효율적인 협업을 지원합니다.
- **백업 및 복구:** 예기치 않은 오류나 데이터 손실 발생 시 이전 버전으로 빠르게 복구할 수 있습니다.
- **코드 안정성 향상:** 변경 사항 추적 및 관리를 통해 코드의 안정성을 높이고, 문제 발생 시 원인 파악 및 해결을 용이하게 합니다.

---

#### 1.2 Git의 등장 배경 및 특징

- **Linux 커널 개발:** 리누스 토르발스가 Linux 커널 개발을 위해 개발한 분산 버전 관리 시스템입니다.
- **빠른 속도와 효율성:** 빠른 속도와 효율적인 브랜치 관리 기능을 제공합니다.
- **분산형 구조:** 각 개발자의 로컬 저장소에 전체 프로젝트 이력을 저장하여 네트워크 연결 없이도 대부분의 작업을 수행 가능하며, 데이터 유실 위험을 줄입니다.
- **오픈 소스:** 오픈 소스 프로젝트로, 자유롭게 사용하고 기여할 수 있습니다.

---

#### 1.3 중앙 집중형 vs 분산형 버전 관리 시스템

| 구분          | 중앙 집중형 (SVN, CVS)                          | 분산형 (Git, Mercurial)                          |
| ------------- | ----------------------------------------------- | ------------------------------------------------ |
| 저장소 구조   | 중앙 서버 저장소 하나                           | 각 개발자 로컬 저장소 + 중앙 (원격) 저장소       |
| 작업 방식     | 중앙 서버에서 최신 버전을 체크아웃하여 작업     | 로컬 저장소에서 작업 후 원격 저장소와 동기화     |
| 오프라인 작업 | 불가능 (중앙 서버 연결 필수)                    | 가능 (로컬 저장소에서 대부분 작업 가능)          |
| 속도          | 상대적으로 느림 (서버 통신 필요)                | 상대적으로 빠름 (로컬 작업 중심)                 |
| 안정성        | 중앙 서버 장애 시 작업 중단 및 데이터 손실 위험 | 분산 저장으로 데이터 유실 위험 감소, 안정성 높음 |

---

#### 1.4 Git의 장점

- **무료 및 오픈 소스:** 자유롭게 사용 가능
- **빠른 속도:** 브랜치 생성, 전환, 커밋 등 작업 속도가 빠름
- **강력한 브랜치 기능:** 효율적인 브랜치 관리 및 병합 기능 제공
- **분산형 구조:** 협업 및 안정성 향상
- **활발한 커뮤니티:** 풍부한 자료와 활발한 커뮤니티 지원

---

### 2. Git 설치 및 기본 설정

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

#### 2.1 Git 설치 (Windows, macOS, Linux)

- **Windows:** [https://git-scm.com/download/win](https://git-scm.com/download/win) 에서 다운로드 후 설치
- **macOS:**
  - Homebrew 설치 후 `brew install git` 명령어 실행
  - 또는 [https://git-scm.com/download/mac](https://git-scm.com/download/mac) 에서 다운로드 후 설치
- **Linux (Debian/Ubuntu):** `sudo apt-get install git` 명령어 실행
- **Linux (Fedora/CentOS):** `sudo yum install git` 명령어 실행

</div>

---

#### 2.2 Git 설정 (사용자 이름, 이메일 설정)

- 터미널 (명령 프롬프트) 실행 후 다음 명령어 실행:
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "your_email@example.com"
  ```
  - `--global` 옵션은 모든 Git 저장소에 적용하는 설정입니다.
  - 특정 저장소에만 설정을 적용하려면 `--local` 옵션을 사용합니다.
- 설정 확인:
  ```bash
  git config --global user.name
  git config --global user.email
  ```

---

#### 2.3 Git 명령어 기본 구조

- Git 명령어는 다음과 같은 구조를 가집니다:
  ```bash
  git [명령어] [옵션] [경로/파일명]
  ```
  - **`git`**: Git 명령어 실행
  - **`[명령어]`**: 수행할 Git 작업 (예: `init`, `add`, `commit` 등)
  - **`[옵션]`**: 명령어의 동작 방식 변경 (예: `--global`, `-m` 등)
  - **`[경로/파일명]`**: 명령어 적용 대상 (생략 가능)

---

### 3. Git 기본 워크플로우 (Local Repository)

#### 3.1 저장소 (Repository) 개념 이해

- **저장소 (Repository):** 프로젝트 파일 및 변경 이력을 저장하는 공간입니다.
- **로컬 저장소 (Local Repository):** 개인 컴퓨터에 생성되는 저장소입니다.
- **원격 저장소 (Remote Repository):** 서버 (GitHub, GitLab 등) 에 위치한 저장소로, 협업을 위해 사용됩니다.

---

#### 3.2 `git init`: 로컬 저장소 생성

- 새로운 폴더를 만들고 해당 폴더로 이동합니다.
- 터미널에서 `git init` 명령어 실행:
  ```bash
  mkdir my-project
  cd my-project
  git init
  ```
  - `.git` 폴더가 생성됩니다. 이 폴더 안에 Git 저장소 관련 정보가 저장됩니다.
  - `.git` 폴더는 숨김 폴더로 표시될 수 있습니다.

---

#### 3.3 `git status`: 저장소 상태 확인

- 저장소의 현재 상태를 확인합니다.
- 명령어 실행:
  ```bash
  git status
  ```
  - **Untracked files:** Git이 관리하지 않는 새로운 파일
  - **Changes to be committed:** 스테이징 영역에 추가된 변경 사항 (커밋 예정)
  - **Changes not staged for commit:** 스테이징 영역에 추가되지 않은 변경 사항 (수정된 파일)
  - **nothing to commit, working tree clean:** 커밋할 변경 사항 없음, 워킹 디렉토리 깨끗함

---

#### 3.4 `git add`: 변경 사항 스테이징 (Staging Area)

- 변경된 파일을 스테이징 영역에 추가하여 커밋 대상으로 만듭니다.
- 명령어 실행:
  ```bash
  git add [파일명]        # 특정 파일 스테이징
  git add .             # 모든 변경 파일 스테이징 (현재 디렉토리 기준)
  git add *             # 모든 변경 파일 스테이징 (전체 디렉토리 기준)
  ```
  - 스테이징 영역은 커밋에 포함될 변경 사항을 준비하는 공간입니다.

---

#### 3.5 `git commit`: 커밋 (Commit) - 변경 사항 기록

- 스테이징 영역에 있는 변경 사항을 저장소에 기록합니다.
- 명령어 실행:
  ```bash
  git commit -m "커밋 메시지"
  ```
  - `-m` 옵션은 커밋 메시지를 바로 작성하는 옵션입니다.
  - 커밋 메시지는 변경 사항을 간결하고 명확하게 설명해야 합니다.
  - 좋은 커밋 메시지 작성은 프로젝트 이력 관리 및 협업에 매우 중요합니다.

---

#### 3.6 커밋 메시지 작성 규칙

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

- **간결하고 명확하게 작성:** 무엇을, 왜 변경했는지 명확하게 설명합니다.
- **제목과 본문 분리 (선택 사항):**
  - 제목 (Subject line): 50자 이내로 요약
  - 본문 (Body): 자세한 설명 (필요한 경우)
- **영어로 작성하는 것을 권장 (국제적인 협업 시):** 프로젝트 표준에 따릅니다.
- **예시:**

  - `Fix: Resolve issue with user login` (제목)
  - `Add: Implement user registration feature` (제목)
  - `Refactor: Improve code readability in user service` (제목 + 본문)

  ```
  Refactor: Improve code readability in user service

  This commit refactors the user service class to improve code readability.
  - Split long methods into smaller, more focused methods.
  - Add comments to clarify complex logic.
  - Improve variable naming for better understanding.
  ```

</div>

---

#### 3.7 `git log`: 커밋 기록 확인

- 저장소의 커밋 기록을 확인합니다.
- 명령어 실행:
  ```bash
  git log
  ```
  - 다양한 옵션을 사용하여 로그를 필터링하고 원하는 정보만 볼 수 있습니다.
  - `git log --oneline`: 한 줄로 간략하게 커밋 로그 표시
  - `git log --graph`: 브랜치 그래프와 함께 커밋 로그 표시
  - `git log --author="Your Name"`: 특정 작성자의 커밋 로그만 표시

---

#### 3.8 `.gitignore`: 파일 무시 설정

- Git이 관리하지 않도록 특정 파일 또는 폴더를 설정합니다.
- 프로젝트 루트 디렉토리에 `.gitignore` 파일을 생성합니다.
- `.gitignore` 파일에 무시할 파일 패턴을 작성합니다.
  - `*.log`: 확장자가 `.log`인 모든 파일 무시
  - `temp/`: `temp` 폴더 및 하위 파일 무시
  - `!important.log`: `important.log` 파일은 무시하지 않음 (예외 규칙)
- 예시 `.gitignore` 파일 내용:
  ```
  *.log
  temp/
  node_modules/
  .idea/
  .DS_Store
  !important.log
  ```

---

### 4. 브랜치 (Branch)

#### 4.1 브랜치 개념 및 필요성 (독립적인 작업 공간)

- **브랜치 (Branch):** 독립적인 개발 라인입니다.
- **메인 브랜치 (master/main):** 기본 브랜치로, 안정적인 버전 관리.
- **기능 브랜치 (feature branch):** 새로운 기능 개발 또는 버그 수정 등 특정 작업을 위한 브랜치.
- **브랜치 사용 이유:**
  - 메인 브랜치를 안정적으로 유지하면서 새로운 기능 개발 또는 실험 가능.
  - 여러 작업을 동시에 독립적으로 진행 가능.
  - 작업 완료 후 메인 브랜치에 병합하여 변경 사항 통합.

---

#### 4.2 `git branch`: 브랜치 확인 및 생성

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

- 브랜치 목록 확인:

  ```bash
  git branch
  ```

  - 현재 브랜치 앞에 `*` 표시
  - `-v` 옵션: 각 브랜치의 마지막 커밋 정보 표시
  - `-a` 옵션: 로컬 및 원격 브랜치 모두 표시
  - `-r` 옵션: 원격 브랜치만 표시

- 새 브랜치 생성:
  ```bash
  git branch [브랜치 이름]
  ```
  - 브랜치 이름은 기능, 작업 내용을 명확하게 나타내도록 짓는 것이 좋습니다. (예: `feature/login-form`, `fix/bug-in-payment`)

</div>

---

#### 4.3 `git checkout`: 브랜치 이동 및 생성

- 브랜치 이동 (전환):

  ```bash
  git checkout [브랜치 이름]
  ```

  - 워킹 디렉토리가 선택한 브랜치의 최신 커밋 상태로 변경됩니다.

- 브랜치 생성 및 이동 (한 번에):
  ```bash
  git checkout -b [새 브랜치 이름]
  ```
  - `-b` 옵션은 브랜치 생성과 동시에 해당 브랜치로 이동하는 옵션입니다.

---

#### 4.4 `git merge`: 브랜치 병합

- 현재 브랜치에 다른 브랜치의 변경 사항을 병합합니다.
- 예시: `feature/login-form` 브랜치를 `main` 브랜치에 병합
  ```bash
  git checkout main      # 병합할 브랜치 (main 브랜치로 이동)
  git merge feature/login-form # 병합할 브랜치 지정 (feature/login-form 브랜치 병합)
  ```
  - 병합 과정에서 충돌 (Conflict) 발생 가능. 충돌 해결 후 커밋 필요.

---

#### 4.5 브랜치 전략 (Git Flow, GitHub Flow 등) 소개

- **브랜치 전략:** 효율적인 브랜치 관리 및 협업을 위한 규칙 및 워크플로우
- **Git Flow:** 복잡한 릴리즈 관리에 적합. `develop`, `release`, `hotfix` 브랜치 등 사용.
- **GitHub Flow:** 단순하고 빠른 릴리즈에 적합. `main` 브랜치, 기능 브랜치 기반 워크플로우.
- **GitLab Flow:** GitHub Flow 확장, 환경별 브랜치 (production, staging) 추가 가능.
- 프로젝트 성격 및 팀 규모에 따라 적절한 브랜치 전략 선택 및 적용.

---

### 5. 원격 저장소 (Remote Repository)

#### 5.1 원격 저장소 개념 (GitHub, GitLab, Bitbucket 등)

- **원격 저장소 (Remote Repository):** 코드 공유 및 협업을 위한 서버 기반 저장소.
- **GitHub:** 가장 인기 있는 Git 원격 저장소 호스팅 서비스. 오픈 소스 프로젝트 및 협업에 널리 사용.
- **GitLab:** GitHub와 유사한 기능 제공, 자체 서버에 설치하여 사용할 수도 있음. CI/CD 기능 통합.
- **Bitbucket:** Atlassian에서 제공하는 Git 원격 저장소 서비스. Jira, Confluence 등 Atlassian 제품과 연동 용이.

---

#### 5.2 `git clone`: 원격 저장소 복제

- 원격 저장소의 코드를 로컬 컴퓨터로 복제합니다.
- 명령어 실행:
  ```bash
  git clone [원격 저장소 URL] [로컬 폴더 이름 (생략 가능)]
  ```
  - 예시: GitHub 저장소 복제
  ```bash
  git clone https://github.com/user/repository.git my-project
  ```

---

#### 5.3 `git remote`: 원격 저장소 관리

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

- 원격 저장소 목록 확인:
  ```bash
  git remote
  git remote -v  # 원격 저장소 URL 함께 표시
  ```
- 원격 저장소 추가:

  ```bash
  git remote add [원격 저장소 이름] [원격 저장소 URL]
  ```

  - `origin` 이라는 이름으로 원격 저장소를 추가하는 것이 일반적입니다.

- 원격 저장소 이름 변경:

  ```bash
  git remote rename [기존 이름] [새로운 이름]
  ```

- 원격 저장소 삭제:
  ```bash
  git remote remove [원격 저장소 이름]
  ```

</div>

---

#### 5.4 `git push`: 로컬 변경 사항 원격 저장소에 반영

- 로컬 저장소의 변경 사항 (커밋)을 원격 저장소에 업로드합니다.
- 명령어 실행:
  ```bash
  git push [원격 저장소 이름] [브랜치 이름]
  ```
  - 예시: `origin` 원격 저장소의 `main` 브랜치에 푸시
  ```bash
  git push origin main
  ```
  - 처음으로 원격 브랜치에 푸시할 때는 `-u` 옵션을 사용하여 로컬 브랜치와 원격 브랜치를 연결 (upstream 설정) 하는 것이 좋습니다.
  ```bash
  git push -u origin main
  ```

---

#### 5.5 `git pull`: 원격 저장소 변경 사항 로컬 저장소에 반영

- 원격 저장소의 최신 변경 사항을 로컬 저장소로 다운로드하여 병합합니다.
- 명령어 실행:
  ```bash
  git pull [원격 저장소 이름] [브랜치 이름]
  ```
  - 예시: `origin` 원격 저장소의 `main` 브랜치에서 풀
  ```bash
  git pull origin main
  ```
  - `git fetch` 와 `git merge` 를 합쳐놓은 명령어입니다.

---

#### 5.6 협업 워크플로우 (Pull Request, Merge Request) 기본

- **Pull Request (GitHub), Merge Request (GitLab, Bitbucket):** 코드 변경 사항을 제안하고 코드 리뷰를 요청하는 협업 방식입니다.
- **워크플로우:**
  1. 기능 브랜치에서 작업 후 원격 저장소에 푸시
  2. GitHub/GitLab 등에서 Pull/Merge Request 생성 (변경 사항 설명, 코드 리뷰 요청)
  3. 코드 리뷰 진행 및 수정
  4. 리뷰 통과 후 Merge (병합)
  5. 변경 사항이 메인 브랜치에 반영

---

### 6. Git 심화 활용

#### 6.1 `git diff`: 변경 사항 비교

- 파일 변경 사항을 비교합니다.
- 명령어 실행:
  ```bash
  git diff                  # 워킹 디렉토리 vs 스테이징 영역 비교
  git diff --staged         # 스테이징 영역 vs 최근 커밋 비교
  git diff [브랜치1] [브랜치2] # 브랜치 간 변경 사항 비교
  git diff [커밋 해시1] [커밋 해시2] # 커밋 간 변경 사항 비교
  git diff [파일명]           # 특정 파일의 변경 사항 비교
  ```

---

#### 6.2 `git reset`: 커밋 되돌리기 (다양한 옵션)

- 커밋을 특정 시점으로 되돌립니다. **주의해서 사용해야 합니다.**
- `git reset --soft [커밋 해시]`: 커밋만 되돌리고 워킹 디렉토리 및 스테이징 영역은 유지 (커밋 이력만 되돌림)
- `git reset --mixed [커밋 해시]`: 커밋 및 스테이징 영역 되돌리고 워킹 디렉토리는 유지 (스테이징 취소) (기본 옵션)
- `git reset --hard [커밋 해시]`: 커밋, 스테이징 영역, 워킹 디렉토리 모두 되돌림 (작업 내용 유실 가능성 높음)

---

#### 6.3 `git revert`: 특정 커밋 되돌리기 (새로운 커밋 생성)

- 특정 커밋의 변경 사항을 되돌리는 새로운 커밋을 생성합니다.
- `git reset` 과 달리 커밋 이력을 유지하면서 변경 사항을 되돌릴 수 있습니다.
- 명령어 실행:
  ```bash
  git revert [커밋 해시]
  ```

---

#### 6.4 `git stash`: 변경 사항 임시 저장

- 현재 작업 중인 변경 사항을 임시로 저장하고 워킹 디렉토리를 깨끗하게 만듭니다.
- 브랜치 전환 등 다른 작업을 해야 할 때 유용합니다.
- 명령어 실행:
  ```bash
  git stash save "stash 메시지"  # 변경 사항 스태시 (메시지 선택 사항)
  git stash list             # 스태시 목록 확인
  git stash apply            # 최근 스태시 적용 (기본)
  git stash apply stash@{n}  # 특정 스태시 적용
  git stash pop              # 스태시 적용 후 목록에서 제거
  git stash drop stash@{n}   # 특정 스태시 삭제
  git stash clear            # 모든 스태시 삭제
  ```

---

#### 6.5 `git tag`: 특정 시점 태그 지정

- 특정 커밋에 태그를 지정하여 릴리즈 버전 등을 표시합니다.
- 명령어 실행:
  ```bash
  git tag [태그 이름] [커밋 해시 (생략 가능, HEAD 기준)]
  git tag -a [태그 이름] -m "태그 메시지" [커밋 해시 (생략 가능)] # 태그 메시지 추가 (Annotated Tag)
  git tag -d [태그 이름]       # 태그 삭제 (로컬)
  git push --tags             # 태그 원격 저장소에 푸시
  ```

#### 6.6 `git rebase`: 브랜치 재정렬 (고급)

- 브랜치 시작점을 변경하여 커밋 이력을 깔끔하게 만듭니다. **주의해서 사용해야 합니다.**
- 기능 브랜치를 메인 브랜치 최신 커밋 위에 다시 시작하도록 합니다.
- 명령어 실행:
  ```bash
  git checkout [기능 브랜치]
  git rebase [메인 브랜치]
  ```
  - **공용 브랜치에는 `rebase` 사용을 지양해야 합니다. (협업 문제 발생 가능성)**

---

#### 6.7 충돌 (Conflict) 해결 방법

- 브랜치 병합 또는 `pull` 시 충돌 발생 가능 (동일 파일의 동일 부분을 서로 다르게 수정한 경우)
- **충돌 발생 시 Git이 충돌 발생 파일에 표시를 추가합니다.**
- **충돌 해결 과정:**
  1. 충돌 발생 파일 열어서 충돌 표시 확인 (`<<<<<<<`, `=======`, `>>>>>>>`)
  2. 충돌된 코드 부분을 직접 수정하여 해결 (어떤 코드를 유지하고 어떤 코드를 제거할지 결정)
  3. 충돌 표시 제거 후 파일 저장
  4. `git add [충돌 해결 파일]` 로 스테이징
  5. `git commit` 으로 커밋 완료

---

### 7. 협업 환경에서의 Git 활용

<div class="overflow-y-auto max-h-[400px] border rounded p-4">

#### 7.1 팀 협업 워크플로우 구축

- 팀 내 Git 사용 규칙 및 브랜치 전략 정의
- 코드 리뷰 프로세스 도입 (Pull Request/Merge Request 활용)
- 커밋 메시지 작성 규칙 팀 내 공유 및 준수
- 정기적인 코드 동기화 및 통합 (잦은 `pull` 및 `merge`)

#### 7.2 코드 리뷰 프로세스

- Pull Request/Merge Request 기반 코드 리뷰
- 코드 리뷰 도구 활용 (GitHub/GitLab 코드 리뷰 기능, Crucible, Review Board 등)
- 코드 리뷰 담당자 지정 또는 순번제/랜덤 방식 리뷰어 선정
- 코드 리뷰 체크리스트 활용
- 건설적인 피드백 및 토론 문화 조성

#### 7.3 브랜치 전략 활용 심화

- Git Flow, GitHub Flow, GitLab Flow 등 브랜치 전략 팀 프로젝트에 맞게 적용 및 개선
- 릴리즈 브랜치, 핫픽스 브랜치 등 전략 브랜치 활용
- 브랜치 네이밍 규칙 통일 및 관리

#### 7.4 GitHub/GitLab 프로젝트 활용

- 이슈 트래커 (Issue Tracker) 활용: 작업 관리, 버그 리포트, 기능 요청 등
- 프로젝트 위키 (Wiki) 활용: 프로젝트 문서화, 팀 협업 정보 공유
- 프로젝트 보드 (Project Board) 활용: 칸반 보드, 스프린트 관리 등
- 마일스톤 (Milestone) 활용: 릴리즈 계획 및 관리
- CI/CD (Continuous Integration/Continuous Delivery) 파이프라인 구축 (GitLab CI 등)

</div>

---

### 8. Git GUI 툴 소개 (선택 사항)

- **GUI 툴 장점:** 시각적인 인터페이스 제공, Git 명령어 숙련도 낮아도 쉽게 사용 가능, 복잡한 브랜치 관리 및 히스토리 확인 용이
- **주요 Git GUI 툴:**
  - **SourceTree:** 무료, Windows/macOS 지원, Atlassian 계정 필요
  - **GitKraken:** 유료 (개인 무료 플랜 존재), Windows/macOS/Linux 지원, 강력한 기능 및 시각화
  - **GitHub Desktop:** 무료, GitHub에서 제공, GitHub 연동 특화, 간단한 기능 중심
  - **TortoiseGit:** 무료, Windows 전용, 윈도우 탐색기 통합, SVN 사용 경험자에게 익숙
- **GUI 툴 사용 시 주의 사항:**
  - GUI 툴에만 의존하지 않고 Git 명령어 기본 개념 이해 필요
  - GUI 툴이 제공하지 않는 고급 기능은 명령어 사용 필요

---

### 9. Git 학습 자료 및 추가 정보

- **공식 Git 문서:** [https://git-scm.com/doc](https://git-scm.com/doc) (영문), [https://git-scm.com/book/ko/v2](https://git-scm.com/book/ko/v2) (한글 번역)
- **Pro Git 책:** 온라인 무료, Git 깊이 있는 학습 자료 (상기 공식 문서 링크에서 접근 가능)
- **생활코딩 Git 강좌:** [https://opentutorials.org/course/1698](https://opentutorials.org/course/1698) (한글, 초보자 친화적)
- **Udemy, Coursera 등 온라인 강의 플랫폼:** 다양한 Git 강좌 제공 (영문/한글)
- **Stack Overflow, Git 관련 커뮤니티:** 문제 해결 및 정보 공유

---
