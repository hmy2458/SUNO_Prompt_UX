# SUNO_Prompt_UX

AI Music Create Prompt Generator (based GUI)

## 실행 방법 (로컬)

### 방법 A) 어디서 실행하든 동작하는 권장 방식

```bash
python3 /workspace/SUNO_Prompt_UX/serve.py
```

브라우저에서 아래 주소로 접속하세요.

- <http://localhost:4173/index.html>

---

### 방법 B) 기본 `http.server` 사용

> 이 방법은 **반드시 저장소 폴더에서 실행**해야 합니다.

```bash
cd /workspace/SUNO_Prompt_UX
python3 -m http.server 4173
```

브라우저에서 아래 주소로 접속하세요.

- <http://localhost:4173/index.html>

## UI가 안 보일 때 체크리스트

- `python3 -m http.server 4173`를 저장소 바깥 폴더에서 실행하면 `index.html` 대신 다른 경로가 열릴 수 있습니다.
- 주소 끝에 `/index.html`을 붙여 접속해보세요.
- 이미 4173 포트를 다른 프로세스가 사용 중이면 서버가 정상 시작되지 않을 수 있습니다.

포트 점유 확인 예시:

```bash
ss -ltnp | rg 4173
```

## 가사 생성 기능 사용 전 설정

`index.html` 파일의 `apiKey` 값을 본인 Gemini API 키로 변경해야 가사 생성 버튼이 동작합니다.

```js
const apiKey = 'YOUR_GEMINI_API_KEY_HERE';
```

## Notes

- Main UI is implemented in `index.html`.
- This project is a static page, so no build step is required.
