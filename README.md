# Code Collector

**Code Collector**는 Python 프로젝트 내에서 사용자가 작성한 코드를 효과적으로 수집할 수 있는 도구입니다. 이 도구는 특정 파일 확장자를 기준으로 코드를 수집하며, `.gitignore` 파일을 활용하여 무시할 파일과 디렉토리를 설정할 수 있습니다.

## 주요 기능

- **코드 수집**: 프로젝트 디렉토리 내의 사용자 작성 코드를 자동으로 수집합니다.
- **확장자 필터링**: Python, JavaScript, Java 등 다양한 프로그래밍 언어의 파일 확장자를 지원합니다.
- **무시 설정**: `.gitignore` 파일을 기반으로 무시할 파일 및 디렉토리를 설정하여 불필요한 파일을 제외합니다.

## 설치

이 프로젝트는 Python 3.7 이상이 필요하며, `aiofiles` 패키지가 필요합니다. 다음 명령어를 사용하여 `aiofiles`를 설치하세요:

```bash
pip install aiofiles
```

## 사용법

### CLI 사용법

Code Collector는 명령줄 인터페이스(CLI)를 통해 쉽게 사용할 수 있습니다. 기본적인 사용법은 다음과 같습니다:

```bash
code-collector [directory] [-e EXTENSIONS] [-i IGNORE] [-o OUTPUT]
```

- `directory`: 프로젝트 디렉토리 경로 (기본값: 현재 디렉토리)
- `-e`, `--extensions`: 포함할 파일 확장자 목록 (기본값: `.py`, `.js`, `.java`, `.cpp`, `.h`, `.css`, `.html`)
- `-i`, `--ignore`: 무시할 파일 목록을 포함한 파일 경로 (기본값: `.gitignore`)
- `-o`, `--output`: 출력 파일 이름 (기본값: `user_code.txt`)

예시:

```bash
code-collector /path/to/project -e .py .js -o collected_code.txt
```

### 스크립트 사용법

`example_run.py` 스크립트를 실행하여 예제 실행을 테스트할 수 있습니다:

```bash
python example_run.py
```

이 스크립트는 지정된 프로젝트 디렉토리에서 Python 파일을 수집하고 결과를 `example_output.txt`에 저장합니다.

## 기여

기여를 환영합니다! 버그 리포트, 기능 제안 또는 풀 리퀘스트를 통해 기여하실 수 있습니다.

1. 이 저장소를 포크합니다.
2. 기능 브랜치를 만듭니다 (`git checkout -b feature/AmazingFeature`).
3. 커밋을 합니다 (`git commit -m 'Add some AmazingFeature'`).
4. 브랜치에 푸시합니다 (`git push origin feature/AmazingFeature`).
5. 풀 리퀘스트를 만듭니다.

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 LICENSE 파일을 참조하세요.