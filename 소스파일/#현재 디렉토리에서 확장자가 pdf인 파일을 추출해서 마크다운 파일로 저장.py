#현재 디렉토리에서 확장자가 pdf인 파일을 추출해서 마크다운 파일로 저장
import os
import glob
import PyPDF2
'''
현재 디렉토리에서 확장자가 pdf인 파일을 추출해서 마크다운 파일로 저장
'''
pdf_files = glob.glob('./*.pdf')

# 각 pdf 파일을 마크다운 파일로 변환합니다.
for pdf_file in pdf_files:
    markdown_output_path = os.path.splitext(pdf_file)[0] + '.md'
    pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        # 각 페이지의 텍스트 추출하여 마크다운 문서 생성
    markdown_content = ""
        
    for page_num, page in enumerate(pdf_reader.pages, start=1):
        page_text = page.extract_text()
        markdown_content += f"# 페이지 {page_num}\n\n{page_text}\n\n"
        
    # 마크다운 파일로 저장
    with open(markdown_output_path, 'w', encoding='utf-8') as markdown_file:
        markdown_file.write(markdown_content)