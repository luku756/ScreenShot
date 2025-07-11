# Python Screenshot Capture Tool with Shutter Sound

## 개요

이 프로그램은 다중 모니터 환경에서 **F12** 키를 누르면 현재 **활성 윈도우**의 화면을 자동으로 캡처하고,  
찰칵 소리를 내며 지정한 폴더에 저장하는 기능을 제공합니다.

스팀에서 일부 게임이 F12로 인한 스크린샷을 지원하지 않는 게 불편하여 작성했습니다.

---

## 주요 기능

- F12 키 입력 감지 (관리자 권한으로 실행 권장)  
- 현재 활성 윈도우 영역 스크린샷 캡처  
- 스크린샷 자동 저장 (파일명에 타임스탬프 및 프로세스 이름 포함)  
- 찰칵 사운드(mp3) 재생  
- 다중 모니터 환경 지원  
- 윈도우 환경 최적화

---

## 저장되는 파일명 규칙

스크린샷 파일명은 다음 형식으로 자동 생성됩니다:


`프로세스이름\프로세스이름_YYYYMMDD_HHMMSS_mmm.png`


- **프로세스이름** : 활성 윈도우를 실행 중인 프로세스 이름 (예: `gameapp`)  
- **YYYYMMDD** : 년월일 (예: 20250706)  
- **HHMMSS** : 시분초 (예: 142530)  
- **mmm** : 밀리초 (예: 123)  

예시:  
`gameapp_20250706_142530_123.png`

---

## 설치 방법

1. Python 3.x 설치  
2. 필수 라이브러리 설치

```bash
pip install -r requirements.txt
