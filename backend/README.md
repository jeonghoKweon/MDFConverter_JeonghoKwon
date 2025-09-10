# MDF File Viewer Backend API_Jeongho Kwon

Python FastAPI 기반의 MDF (Measurement Data Format) 파일 처리 백엔드 서버입니다.

## 🚀 빠른 시작

### 1. 의존성 설치

```bash
cd backend
pip install -r requirements.txt
```

### 2. 서버 실행

```bash
# 개발 모드로 실행
python main.py

# 또는 uvicorn 직접 사용
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

서버는 http://localhost:8000 에서 실행됩니다.

## 📚 API 문서

서버 실행 후 다음 URL에서 자동 생성된 API 문서를 확인할 수 있습니다:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🛠 주요 기능

### 1. 파일 업로드
- **POST** `/api/upload`
- MDF/MF4 파일 업로드 및 기본 정보 추출
- 세션 ID 생성 및 반환

### 2. 채널 목록 조회
- **GET** `/api/channels/{session_id}`
- 업로드된 MDF 파일의 채널 목록 반환
- 채널명, 단위, 설명, 샘플 수, 데이터 타입 등 포함

### 3. 채널 데이터 조회
- **POST** `/api/data/{session_id}`
- 선택된 채널들의 시계열 데이터 반환
- 최대 20개 채널까지 동시 처리

### 4. CSV 내보내기
- **POST** `/api/export/csv/{session_id}`
- 선택된 채널들의 데이터를 CSV 형식으로 내보내기
- 파일 다운로드로 제공 (StreamingResponse)

### 5. 세션 관리
- **DELETE** `/api/session/{session_id}`: 세션 정리
- **GET** `/api/sessions`: 활성 세션 목록

## 📋 API 사용 예시

### 파일 업로드
```bash
curl -X POST "http://localhost:8000/api/upload" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@your_file.mdf"
```

### 채널 목록 조회
```bash
curl -X GET "http://localhost:8000/api/channels/{session_id}"
```

### 채널 데이터 조회
```bash
curl -X POST "http://localhost:8000/api/data/{session_id}" \
  -H "Content-Type: application/json" \
  -d '["ENGINE_TEMP_001", "VEHICLE_SPEED_002"]'
```

### CSV 내보내기
```bash
curl -X POST "http://localhost:8000/api/export/csv/{session_id}" \
  -H "Content-Type: application/json" \
  -d '["ENGINE_TEMP_001", "VEHICLE_SPEED_002"]' \
  --output exported_data.csv
```

## 🔧 기술 스택

- **FastAPI**: 웹 프레임워크
- **uvicorn**: ASGI 서버
- **asammdf**: MDF 파일 파싱 라이브러리
- **numpy**: 수치 연산
- **pydantic**: 데이터 검증 및 직렬화

## 📁 프로젝트 구조

```
backend/
├── main.py              # FastAPI 애플리케이션 메인
├── models.py            # Pydantic 데이터 모델
├── mdf_processor.py     # MDF 파일 처리 로직
├── requirements.txt     # Python 의존성
└── README.md           # 이 파일
```

## ⚠️ 주의사항

1. **asammdf 라이브러리**: MDF 파일 처리를 위해 필요합니다. 설치되지 않은 경우 시뮬레이션 모드로 동작합니다.

2. **메모리 사용량**: 큰 MDF 파일 처리 시 메모리 사용량이 증가할 수 있습니다.

3. **보안**: 프로덕션 환경에서는 CORS 설정을 구체적인 도메인으로 제한하세요.

4. **임시 파일**: 업로드된 파일은 임시 디렉터리에 저장됩니다. 세션 정리를 통해 정리할 수 있습니다.

## 🚧 개발 모드 vs 프로덕션 모드

### 개발 모드
- asammdf가 없어도 시뮬레이션 데이터로 동작
- CORS 모든 오리진 허용
- 자동 리로드 활성화

### 프로덕션 권장사항
- asammdf 라이브러리 필수 설치
- CORS 설정을 구체적인 도메인으로 제한
- 파일 저장소를 Redis나 데이터베이스로 변경
- 로깅 및 모니터링 추가
- HTTPS 사용

## 🔄 프론트엔드 연동

이 백엔드는 `index-backend.html`과 `mdf-viewer-backend.js`와 완전히 연동됩니다:

### 주요 연동 기능
1. **파일 업로드**: 실제 MDF 파일 업로드 및 처리
2. **채널 목록**: 실제 MDF 채널 정보 표시
3. **차트 생성**: 
   - 단일 차트 모드: 모든 채널을 하나의 차트에 표시
   - 복수 차트 모드: 각 채널을 개별 차트로 분리 표시
4. **CSV 내보내기**: 선택된 채널 데이터를 CSV 파일로 다운로드
5. **세션 관리**: 파일 업로드부터 세션 종료까지 완전한 라이프사이클 관리

### CSV 내보내기 형식
```csv
Time (s), Channel1 (unit), Channel2 (unit), ...
0.000000, 1.234567, 2.345678, ...
0.100000, 1.345678, 2.456789, ...
...
```

### 브랜딩
모든 차트와 내보내기 파일에 "Jeongho Kwon" 브랜딩이 적용됩니다.