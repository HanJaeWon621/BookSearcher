#PDF 파일 특정 페이지만으로 새로운   pdf 생성
import PyPDF2
'''
PDF 파일 특정 페이지만으로 새로운   pdf 생성
'''
def cut_pdf_page(input_pdf, output_pdf, start_page, end_page):
    pdf_reader = PyPDF2.PdfReader(input_pdf)
    pdf_writer = PyPDF2.PdfWriter()

    for page_num in range(start_page - 1, end_page):
        pdf_writer.add_page(pdf_reader.pages[page_num])

    with open(output_pdf, "wb") as output_file:
        pdf_writer.write(output_file)

input_pdf_path = "시간관리의기술.pdf"  # 입력 PDF 파일 경로
output_pdf_path = "output.pdf"  # 잘라낸 PDF 파일을 저장할 경로
start_page_number = 2  # 잘라낼 시작 페이지 번호
end_page_number = 29  # 잘라낼 마지막 페이지 번호

cut_pdf_page(input_pdf_path, output_pdf_path, start_page_number, end_page_number)
