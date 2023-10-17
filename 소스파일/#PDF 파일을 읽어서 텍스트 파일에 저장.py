#PDF 파일을 읽어서 텍스트 파일에 저장
import PyPDF2
'''
PDF 파일을 읽어서 텍스트 파일에 저장
'''
def extract_text_from_pdf(pdf_file_path):
    extracted_text = ''
    
    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)
        
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            extracted_text += page.extract_text()
    
    return extracted_text

def save_text_to_file(text, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(text)

if __name__ == '__main__':
    input_pdf_path = '2022년(제23회) 정보시스템 감리사 필기시험 문제 및 답안.pdf'  # 입력할 PDF 파일 경로 입력
    output_txt_path = 'output.txt'  # 출력할 텍스트 파일 경로 입력
    
    extracted_text = extract_text_from_pdf(input_pdf_path)
    save_text_to_file(extracted_text, output_txt_path)
    
    print('텍스트 추출 및 저장 완료')
