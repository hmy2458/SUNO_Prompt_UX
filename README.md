# SUNO_Prompt_UX

AI Music Create Prompt Generator (based GUI)

## 실행 방법 (로컬)

### 1) 저장소 이동
```bash
cd /workspace/SUNO_Prompt_UX
```

### 2) 정적 서버 실행
```bash
python3 -m http.server 4173
```

### 3) 브라우저에서 접속
아래 주소를 브라우저로 열면 됩니다.

- <http://localhost:4173>

## 가사 생성 기능 사용 전 설정

`index.html` 파일의 `apiKey` 값을 본인 Gemini API 키로 변경해야 가사 생성 버튼이 동작합니다.

```js
const apiKey = 'YOUR_GEMINI_API_KEY_HERE';
```

## Notes

- Main UI is implemented in `index.html`.
- This project is a static page, so no build step is required.
