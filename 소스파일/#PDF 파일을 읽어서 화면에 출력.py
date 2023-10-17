#PDF 파일을 읽어서 화면에 출력
import PyPDF2
'''
PDF 파일을 읽어서 화면에 출력
'''
# PDF 파일 경로 설정
pdf_path = '2022년(제23회) 정보시스템 감리사 필기시험 문제 및 답안.pdf'

# PDF 파일 열기
with open(pdf_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    # 페이지 수 가져오기
    num_pages = len(pdf_reader.pages)
    
    # 각 페이지의 텍스트 추출
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        page_text = page.extract_text()
        
        # 추출한 텍스트 출력 또는 원하는 처리 수행
        print(f"페이지 {page_num + 1}:\n{page_text}\n")