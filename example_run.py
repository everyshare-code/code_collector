import os
import asyncio
import sys
from code_collector.collector import collect_user_code
from code_collector.utils import get_default_extensions

async def run_example():
    # 현재 스크립트의 디렉토리를 기준으로 상대 경로 설정
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(current_dir, 'example_output.txt')

    # 예제 실행
    extensions = ['.py']  # Python 파일만 수집

    project_dir = '/Users/everyshare/code_collector'
    ignore_file = os.path.join(project_dir, '.gitignore')

    # 프로젝트 디렉토리 존재 여부 확인
    if not os.path.exists(project_dir):
        print(f"프로젝트 디렉토리가 존재하지 않습니다: {project_dir}")
        sys.exit(1)

    # .gitignore 파일 존재 여부 확인
    if not os.path.isfile(ignore_file):
        print(f".gitignore 파일이 존재하지 않습니다: {ignore_file}")
        sys.exit(1)

    print(f"프로젝트 디렉토리: {project_dir}")
    print(f"수집할 파일 확장자: {extensions}")
    print(f"무시할 파일 목록: {ignore_file}")
    print(f"출력 파일: {output_file}")

    # 비동기 함수 실행
    await collect_user_code(project_dir, extensions, ignore_file, output_file)

    print(f"\n예제 실행이 완료되었습니다. 결과는 {output_file}에서 확인할 수 있습니다.")

    # 결과 파일의 내용 출력
    print("\n--- 결과 파일 내용 ---")
    with open(output_file, 'r', encoding='utf-8') as f:
        print(f.read())

if __name__ == "__main__":
    asyncio.run(run_example())