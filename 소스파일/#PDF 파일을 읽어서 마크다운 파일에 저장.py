#PDF 파일을 읽어서 마크다운 파일에 저장
import PyPDF2
'''
PDF 파일을 읽어서 마크다운 파일에 저장
'''
# PDF 파일 경로 설정
file_nm  = '2016년(제17회) 정보시스템 감리사 필기시험 문제 및 답안'
pdf_path = file_nm + '.pdf'
markdown_output_path = file_nm + '.md'

# PDF 파일 열기
with open(pdf_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    # 각 페이지의 텍스트 추출하여 마크다운 문서 생성
    markdown_content = ""
    
    for page_num, page in enumerate(pdf_reader.pages, start=1):
        page_text = page.extract_text()
        markdown_content += f"# 페이지 {page_num}\n\n{page_text}\n\n"
    
    # 마크다운 파일로 저장
    with open(markdown_output_path, 'w', encoding='utf-8') as markdown_file:
        markdown_file.write(markdown_content)