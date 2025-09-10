# MDF File Viewer Project

MDF (Measurement Data Format) 파일 시각화 도구입니다. 순수 프론트엔드 버전과 Python Backend 연동 버전을 모두 제공합니다.

## Project Structure

### Frontend (프론트엔드)
- `index.html`: 순수 JavaScript 버전 (시뮬레이션 데이터)
- `index-backend.html`: Python Backend 연동 버전 (실제 MDF 데이터)
- `chart-popup.html`: 차트 팝업 창 (단일/복수 차트 지원)
- `mdf-viewer.js`: 순수 JavaScript 로직 (시뮬레이션)
- `mdf-viewer-backend.js`: Backend 연동 JavaScript
- `README.md`: 프로젝트 문서
- `Measurement_*.mdf`: 테스트용 MDF 파일들

### Backend (백엔드)
- `backend/main.py`: FastAPI 메인 서버
- `backend/models.py`: Pydantic 데이터 모델
- `backend/mdf_processor.py`: MDF 파일 처리 로직
- `backend/requirements.txt`: Python 의존성
- `backend/start_server.py`: 서버 시작 스크립트
- `backend/README.md`: Backend 문서
- `start_backend.bat`: Windows 서버 시작 스크립트

## Quick Start

### 순수 Frontend 버전 (시뮬레이션 데이터)
```bash
# 브라우저에서 index.html 열기
open index.html
```

### Python Backend 연동 버전 (실제 MDF 데이터)
```bash
# 1. Backend 서버 시작 (Windows)
start_backend.bat

# 또는 수동으로:
cd backend
pip install -r requirements.txt
python main.py

# 2. 브라우저에서 Backend 연동 버전 열기
open index-backend.html
```

## Features

### 공통 기능
- **컴팩트한 페이지네이션**: 24px 높이의 작은 버튼들  
- **드래그 앤 드롭**: 파일을 드래그하여 쉽게 업로드
- **실시간 검색**: 채널명으로 실시간 검색 및 필터링
- **반응형 디자인**: 다양한 화면 크기에 대응
- **인터랙티브 차트**: Plotly.js를 사용한 고급 차트

### Frontend 전용 (index.html)
- **순수 웹 기술**: HTML/CSS/JavaScript만으로 구현
- **시뮬레이션 데이터**: 실제 라이브러리 없이도 동작

### Backend 연동 (index-backend.html + Python Backend)
- **실제 MDF 처리**: asammdf 라이브러리를 사용한 정확한 데이터 파싱
- **RESTful API**: FastAPI 기반의 강력한 백엔드
- **세션 관리**: 파일 업로드 및 세션 기반 데이터 관리
- **확장성**: 대용량 파일 처리 및 고급 기능 확장 가능
- **차트 유형 선택**: 단일 그래프 또는 복수 그래프 선택 가능
- **범례 위치**: 각 차트 하단에 범례 배치
- **채널 관리**: 선택 리셋 버튼으로 쉬운 채널 선택 초기화
- **CSV 내보내기**: 선택된 채널 데이터를 CSV 형식으로 내보내기
- **개인 브랜딩**: "Jeongho Kwon" 브랜딩이 적용된 차트 제목

## Dependencies
- **Plotly.js**: CDN에서 자동 로드
- **모던 브라우저**: Chrome 60+, Firefox 55+, Safari 12+, Edge 79+

## Channel Management
- 페이지당 44개 채널 (2열 × 22행)
- 실시간 검색 및 필터링
- 최대 20개 채널 동시 선택 제한
- 채널 선택 리셋 버튼 (우측 상단)
- CSV 내보내기 기능 (선택된 채널)

## Chart Features
- Plotly.js 기반 인터랙티브 차트
- 단일 차트 모드: 모든 채널을 하나의 차트에 표시
- 복수 차트 모드: 각 채널을 개별 차트로 분리 표시
- 줌, 팬, 범위 선택 기능 (단일/복수 모드 모두 지원)
- 범례 하단 배치 (수평 레이아웃)
- 반응형 차트 크기
- 차트 내보내기 (PNG 형식)
- 개인 브랜딩 (Jeongho Kwon)

## Browser Compatibility
- Chrome/Chromium 60+
- Firefox 55+
- Safari 12+
- Edge 79+