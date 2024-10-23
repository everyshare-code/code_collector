import os
import fnmatch
import asyncio
import aiofiles
from typing import List, Tuple

async def parse_ignore_file(ignore_file_path: str) -> Tuple[List[str], List[str]]:
    excluded_extensions = []
    excluded_dirs = []
    if os.path.exists(ignore_file_path):
        async with aiofiles.open(ignore_file_path, 'r') as f:
            for line in await f.readlines():
                line = line.strip()
                if line and not line.startswith('#'):
                    # '/'로 끝나는 경우는 디렉토리로 처리
                    if line.endswith('/'):
                        excluded_dirs.append(line.rstrip('/'))  # '/' 제거하고 저장
                    # '*.'으로 시작하는 경우는 확장자로 처리
                    elif line.startswith('*.'):
                        excluded_extensions.append(line)
                    # 그 외의 경우는 디렉토리로 처리
                    else:
                        excluded_dirs.append(line)
    return excluded_extensions, excluded_dirs


async def find_user_files(directory: str, included_extensions: List[str], ignore_file: str = '.gitignore') -> List[str]:
    excluded_extensions, excluded_dirs = await parse_ignore_file(ignore_file)
    matched_files = []

    async def process_file(file_path: str) -> None:
        # 파일의 상대 경로를 계산하여 제외 패턴과 매칭
        relative_path = os.path.relpath(file_path, directory)

        # 파일이 제외 디렉토리에 있는지 확인
        path_parts = relative_path.split(os.sep)
        if any(dir_name in path_parts for dir_name in excluded_dirs):
            return

        # 확장자 매칭 및 제외 패턴 확인
        if any(file_path.endswith(ext) for ext in included_extensions) and not any(
                fnmatch.fnmatch(relative_path, pattern) for pattern in excluded_extensions):
            matched_files.append(file_path)

    tasks = []
    for root, dirs, files in os.walk(directory):
        # 제외할 디렉토리 필터링
        dirs[:] = [d for d in dirs if d not in excluded_dirs]

        for file in files:
            file_path = os.path.join(root, file)
            tasks.append(process_file(file_path))

    await asyncio.gather(*tasks)
    return matched_files

async def collect_user_code(directory: str, included_extensions: List[str], ignore_file: str = '.gitignore', output_file: str = 'user_code.txt') -> str:
    user_files = await find_user_files(directory, included_extensions, ignore_file)

    async with aiofiles.open(output_file, 'w', encoding='utf-8') as out_file:
        for file_path in user_files:
            relative_path = os.path.relpath(file_path, directory)
            await out_file.write(f'--- {relative_path} ---\n')
            async with aiofiles.open(file_path, 'r', encoding='utf-8') as in_file:
                await out_file.write(await in_file.read())
            await out_file.write('\n\n')

    return output_file