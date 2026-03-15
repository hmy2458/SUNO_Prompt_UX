# SUNO_Prompt_UX

AI Music Create Prompt Generator (based GUI)

## 실행 방법 (로컬)

핵심은 **반드시 `serve.py`가 있는 프로젝트 폴더에서 실행**하는 것입니다.

### 1) 프로젝트 폴더로 이동

#### macOS / Linux
```bash
cd /workspace/SUNO_Prompt_UX
```

#### Windows (PowerShell 또는 CMD)
```powershell
cd C:\workspace\SUNO_Prompt_UX
```

### 2) 서버 실행

#### 방법 A) 권장 (`serve.py` 사용)
```bash
python serve.py
```

#### 방법 B) 기본 `http.server` 사용
```bash
python -m http.server 4173
```

### 3) 브라우저에서 접속

- <http://localhost:4173/index.html>

## Windows에서 `serve.py` 파일을 못 찾는 오류가 날 때

아래 오류는 **현재 폴더가 프로젝트 폴더가 아닐 때** 주로 발생합니다.

```text
python.exe: can't open file 'C:\workspace\SUNO_Prompt_UX\serve.py': [Errno 2] No such file or directory
```

확인 순서:

1. 현재 경로 확인
   - PowerShell: `pwd`
   - CMD: `cd`
2. 파일 존재 확인
   - `dir serve.py`
3. `serve.py`가 보이는 폴더에서 다시 실행
   - `python serve.py`

## UI가 안 보일 때 체크리스트

- 주소 끝에 `/index.html`을 붙여 접속해보세요.
- 서버를 프로젝트 바깥 폴더에서 실행하면 `index.html` 대신 다른 경로가 열릴 수 있습니다.
- 이미 4173 포트를 다른 프로세스가 사용 중이면 서버가 정상 시작되지 않을 수 있습니다.

## 가사 생성 기능 사용 전 설정

`index.html` 파일의 `apiKey` 값을 본인 Gemini API 키로 변경해야 가사 생성 버튼이 동작합니다.

```js
const apiKey = 'YOUR_GEMINI_API_KEY_HERE';
```

## Notes

- Main UI is implemented in `index.html`.
- This project is a static page, so no build step is required.
