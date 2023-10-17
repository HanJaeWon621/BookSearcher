import os
import glob
import shutil


# 현재 디렉토리에서 확장자가 py인 파일을 찾습니다.
py_files = glob.glob('./*.py')

# 각 py 파일의 첫 줄을 읽고 파일명으로 파일을 복사합니다.
for py_file in py_files:
    with open(py_file, 'r', encoding='UTF8') as f:
        first_line = f.readline().strip()
        new_file = first_line + '.py'
        shutil.copy(py_file, new_file)