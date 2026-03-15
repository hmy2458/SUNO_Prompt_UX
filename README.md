# SUNO_Prompt_UX

AI Music Create Prompt Generator (based GUI)

## GitHub에서 바로 실행 (GitHub Pages)

1. GitHub 저장소로 푸시합니다.
2. 저장소 **Settings → Pages**로 이동합니다.
3. **Build and deployment**에서 Source를 **Deploy from a branch**로 선택합니다.
4. Branch를 `main`(또는 사용하는 기본 브랜치), 폴더를 `/ (root)`로 선택 후 저장합니다.
5. 발급된 Pages URL로 접속하면 `index.html`이 기본 페이지로 열립니다.

예: `https://<github-username>.github.io/<repo-name>/`

---

## 로컬 실행 방법

핵심은 **반드시 `serve.py`가 있는 프로젝트 폴더에서 실행**하는 것입니다.

### 0) 먼저 프로젝트 폴더 위치 확인

- 이 저장소를 내려받은(또는 압축 해제한) 실제 위치를 사용해야 합니다.
- 예: `C:\Users\<사용자명>\Downloads\SUNO_Prompt_UX`

### 1) 프로젝트 폴더로 이동

#### macOS / Linux
```bash
cd /path/to/SUNO_Prompt_UX
```

#### Windows (PowerShell 또는 CMD)
```powershell
cd "C:\Users\<사용자명>\Downloads\SUNO_Prompt_UX"
```

> `cd /workspace/SUNO_Prompt_UX` 는 일부 Linux 환경 전용 예시라서, 일반 Windows PC에서는 동작하지 않을 수 있습니다.

### 2) 파일 존재 확인 (선택)

#### macOS / Linux
```bash
ls
```

#### Windows (PowerShell 또는 CMD)
```powershell
dir
```

출력에 `index.html`, `serve.py`가 보이면 정상입니다.

### 3) 서버 실행

#### 방법 A) 권장 (`serve.py` 사용)
```bash
python serve.py
```

#### 방법 B) 기본 `http.server` 사용
```bash
python -m http.server 4173
```

### 4) 브라우저에서 접속

- <http://localhost:4173/index.html>

## Windows에서 자주 나는 오류와 해결

### 오류 1)
```text
cd /workspace/SUNO_Prompt_UX
지정된 경로를 찾을 수 없습니다.
```
원인: Linux 경로를 Windows에서 사용함.
해결: 본인 PC의 실제 경로로 `cd` 하세요.

### 오류 2)
```text
python.exe: can't open file '...\serve.py': [Errno 2] No such file or directory
```
원인: 현재 폴더가 프로젝트 폴더가 아님.
해결:
1. 현재 경로 확인 (`pwd` 또는 `cd`)
2. `dir serve.py`로 파일 확인
3. `serve.py`가 있는 폴더에서 `python serve.py` 실행

## UI가 안 보일 때 체크리스트

- 주소 끝에 `/index.html`을 붙여 접속해보세요.
- 서버를 프로젝트 바깥 폴더에서 실행하면 `index.html` 대신 다른 경로가 열릴 수 있습니다.
- 이미 4173 포트를 다른 프로세스가 사용 중이면 서버가 정상 시작되지 않을 수 있습니다.

## 가사 생성 기능 사용 전 설정 (필수)

가사 생성은 코드 수정이 아니라, 페이지 상단의 **Gemini API 키 입력란**에 직접 입력 후 **키 저장** 버튼을 누르면 됩니다.

- 키는 브라우저의 `localStorage`에만 저장됩니다.
- 저장 후 `가사생성` 버튼이 동작합니다.

> 이전처럼 `index.html` 내부 코드를 직접 수정할 필요가 없습니다.

## Notes

- Main UI is implemented in `index.html`.
- This project is a static page, so no build step is required.

## Music Style Selection 출력 언어

- `Music Style Selection` 결과는 **선택한 옵션 기반의 영어 문장**으로 출력됩니다.
- 복사 버튼으로 결과를 그대로 복사할 수 있습니다.

## GitHub에 다시 패치 요청(PR)하는 방법

아래 순서대로 하면 GitHub에서 다시 리퀘스트할 수 있습니다.

1. 원격 저장소가 연결되어 있는지 확인
```bash
git remote -v
```

2. 현재 브랜치와 변경사항 확인
```bash
git branch --show-current
git status
```

3. 변경사항 커밋
```bash
git add .
git commit -m "fix: update requested changes"
```

4. 원격 브랜치로 푸시
```bash
git push origin <현재브랜치명>
```

5. GitHub에서 Compare & pull request 버튼으로 PR 재요청
- PR 제목에 "재요청" 또는 "follow-up"을 명시
- 이전 이슈 링크/코멘트를 본문에 함께 첨부
