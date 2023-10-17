#FILE_NM:
import os
import glob
import shutil

def get_filename_without_extension(filepath):
    # 파일 경로를 사용하여 파일명과 확장자를 분리합니다.
    filename, file_extension = os.path.splitext(filepath)
    # 파일명만 반환합니다.
    return filename

def is_numeric_filename(filename):
    try:
        # 주어진 문자열을 정수로 변환해보고, 변환이 성공하면 숫자 파일명으로 판단합니다.
        int(filename)
        return True
    except ValueError:
        # 변환 실패 시 숫자 파일명이 아닌 것으로 판단합니다.
        return False

# 현재 디렉토리에서 확장자가 py인 파일을 찾습니다.
py_files = glob.glob('./*.py')

# 각 py 파일의 첫 줄을 읽고 파일명으로 파일을 복사합니다.
for py_file in py_files:
    with open(py_file, 'r', encoding='UTF8') as f:
        first_line = f.readline().strip()
        first_line_arr = first_line.split(':')
        file_nm=first_line_arr[1]
        new_file = first_line + '.py'
        
        
        print("a>>",new_file)
        #py_file = py_file.replace('.\\','')
        filename1 = get_filename_without_extension(py_file)
        if is_numeric_filename(filename1):
          #print(f"'{filename1}'은(는) 숫자 파일명입니다.")
          shutil.copy(py_file, new_file)
        else:
          print(f"'{filename1}'은(는) 숫자 파일명이 아닙니다.")
          #shutil.copy(py_file, new_file)'''