# MDF 파일 그래프 뷰어_Jeongho Kwon

HTML/CSS/JavaScript로 구현된 MDF(Measurement Data Format) 파일 시각화 도구입니다. 순수 프론트엔드 버전과 Python Backend 연동 버전을 모두 제공합니다.

## 특징

### 공통 기능
- **순수 웹 기술**: HTML, CSS, JavaScript만으로 구현
- **컴팩트한 페이지네이션**: 이미지와 동일한 스타일의 작은 버튼들
- **드래그 앤 드롭**: 파일을 드래그하여 쉽게 업로드
- **실시간 검색**: 채널명으로 실시간 검색 및 필터링
- **반응형 디자인**: 다양한 화면 크기에 대응
- **인터랙티브 차트**: Plotly.js를 사용한 고급 차트

### Backend 연동 추가 기능
- **실제 MDF 처리**: asammdf 라이브러리를 통한 정확한 데이터 파싱
- **차트 유형 선택**: 단일 그래프 또는 복수 그래프 선택 가능
- **범례 하단 배치**: 각 차트 하단에 수평 범례 배치
- **채널 선택 리셋**: 우측 상단 리셋 버튼으로 쉬운 선택 초기화
- **CSV 내보내기**: 선택된 채널 데이터를 CSV 형식으로 내보내기
- **개인 브랜딩**: "Jeongho Kwon" 브랜딩이 적용된 차트 제목

## 파일 구조

### 프론트엔드
```
├── index.html              # 순수 JavaScript 버전 (시뮬레이션)
├── index-backend.html      # Backend 연동 버전 (실제 MDF)
├── chart-popup.html        # 차트 팝업 창
├── mdf-viewer.js          # 순수 JavaScript 로직
├── mdf-viewer-backend.js  # Backend 연동 JavaScript
├── README.md              # 프로젝트 문서
└── Measurement_*.mdf      # 테스트용 MDF 파일들
```

### 백엔드
```
backend/
├── main.py              # FastAPI 메인 서버
├── models.py            # Pydantic 데이터 모델
├── mdf_processor.py     # MDF 파일 처리 로직
├── requirements.txt     # Python 의존성
├── start_server.py      # 서버 시작 스크립트
└── README.md           # Backend 문서
```

## 사용 방법

### 순수 Frontend 버전
1. **파일 실행**: `index.html`을 웹 브라우저에서 열기
2. **파일 업로드**: MDF 파일(.mdf, .mf4)을 드래그하거나 파일 선택 (시뮬레이션 데이터)
3. **채널 선택**: 사이드바에서 원하는 채널들을 체크박스로 선택
4. **그래프 생성**: "그래프 그리기" 버튼 클릭

### Backend 연동 버전
1. **백엔드 서버 시작**: `cd backend && python main.py`
2. **파일 실행**: `index-backend.html`을 웹 브라우저에서 열기
3. **파일 업로드**: 실제 MDF 파일(.mdf, .mf4)을 드래그하거나 파일 선택
4. **차트 유형 선택**: 단일 그래프 또는 복수 그래프 선택
5. **채널 선택**: 사이드바에서 원하는 채널들을 체크박스로 선택
6. **그래프 생성**: "그래프 그리기" 버튼 클릭하면 새 창에서 차트 열림
7. **데이터 내보내기**: "CSV 내보내기" 버튼으로 선택된 채널 데이터 다운로드

## 주요 기능

### 컴팩트한 페이지네이션
- 24px 높이의 작은 버튼들
- `‹prev`, `next›` 텍스트 사용
- 현재 페이지는 파란색 하이라이트
- 2px 간격으로 조밀한 배치

### 채널 관리
- 페이지당 44개 채널 (2열 × 22행)
- 실시간 검색 및 필터링
- 최대 20개 채널 동시 선택 제한
- 채널 선택 리셋 버튼 (우측 상단)

### 차트 기능
- Plotly.js 기반 인터랙티브 차트
- 단일 차트 모드: 모든 채널을 하나의 차트에 표시
- 복수 차트 모드: 각 채널을 개별 차트로 분리 표시
- 줌, 팬, 범위 선택 기능 (단일/복수 모드 모두 지원)
- 범례 하단 배치 (수평 레이아웃)
- 반응형 차트 크기
- 차트 내보내기 (PNG 형식)
- 개인 브랜딩 (Jeongho Kwon)

### 데이터 내보내기
- CSV 형식으로 선택된 채널 데이터 내보내기
- 시간 정보와 채널별 값을 포함한 구조화된 형식
- 자동 파일명 생성 (`mdf_export_{session_id}_{채널수}channels.csv`)

## 기술적 특징

### 현재 구현
- **프론트엔드**: 순수 HTML/CSS/JavaScript
- **차트 라이브러리**: Plotly.js
- **시뮬레이션**: 200개의 가상 채널 데이터 생성

### 실제 MDF 처리를 위한 추가 개발 필요
실제 MDF 파일 처리를 위해서는 다음이 필요합니다:

1. **서버사이드 처리**:
   ```python
   # Python 백엔드 (Flask/FastAPI)
   import asammdf
   from flask import Flask, request, jsonify
   
   @app.route('/upload-mdf', methods=['POST'])
   def process_mdf():
       file = request.files['file']
       mdf = asammdf.MDF(file)
       channels = list(mdf.channels_db.keys())
       return jsonify({'channels': channels})
   ```

2. **WASM 버전**: 
   - Python을 WebAssembly로 컴파일
   - 브라우저에서 직접 MDF 처리 가능

3. **파일 파서**:
   - JavaScript로 MDF 바이너리 파싱 구현

## 브라우저 호환성

- Chrome/Chromium 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## 향후 개선 계획

Backend 연동 버전에서 이미 많은 기능이 구현되었지만, 추가로 고려할 수 있는 개선사항들:

1. ✅ **실제 MDF 파싱**: ~~WebAssembly 또는 서버 API를 통한 실제 MDF 파일 처리~~ (완료)
2. **실시간 스트리밍**: 실시간 데이터 수집 및 시각화 지원
3. **차트 확장**: 히스토그램, 스펙트럼, FFT 분석 등 추가 차트 타입
4. ✅ **데이터 내보내기**: ~~CSV, JSON, Excel 형식으로 데이터 내보내기~~ (CSV 완료)
5. **설정 관리**: 사용자 설정 저장 및 불러오기 기능
6. **성능 최적화**: 대용량 파일 처리를 위한 가상화 및 청크 로딩
7. **추가 내보내기 형식**: JSON, Excel, MATLAB 형식 지원
8. **차트 템플릿**: 사용자 정의 차트 템플릿 저장 및 불러오기