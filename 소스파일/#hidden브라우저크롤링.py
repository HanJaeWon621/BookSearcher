#hidden브라우저크롤링
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Chrome 브라우저를 "hidden" 모드로 실행
chrome_options = Options()
chrome_options.add_argument('--headless')  # "hidden" 모드 설정
chrome_options.add_argument('--disable-gpu')  # GPU 사용 비활성화
driver = webdriver.Chrome(options=chrome_options)

# 웹 페이지 접속
driver.get('https://www.deepl.com/')

# 입력할 내용 및 selector 설정 #panelTranslateText > 
input_content = "안녕하세요, 이 문장을 번역해주세요."
input_selector = 'textarea.lmt__source_textarea'
input_selector = 'div.lmt__inner_textarea_container > d-textarea > div > p'
input_selector = 'div.lmt__sides_container > div.lmt__sides_wrapper > section.lmt__side_container.lmt__side_container--source > div.lmt__textarea_container > div.lmt__inner_textarea_container > d-textarea > div > p'

# 입력 내용을 선택한 element에 입력
input_element = driver.find_element(By.CSS_SELECTOR, input_selector)
input_element.clear()
input_element.send_keys(input_content)

# 3초 대기
time.sleep(10)

# 번역된 내용 가져오기 #panelTranslateText > 
output_selector = 'div.lmt__translations_as_text__text_btn'
output_selector = 'div.lmt__inner_textarea_container > d-textarea > div > p > span'
output_selector = 'div.lmt__sides_container > div.lmt__sides_wrapper > section.lmt__side_container.lmt__side_container--target > div.lmt__textarea_container.lmt__raise_alternatives_placement > div.lmt__translations_as_text > ul > li:nth-child(3) > button'
output_element = driver.find_element(By.CSS_SELECTOR, output_selector)
translated_text = output_element.text

# 번역 내용 출력
print("입력 내용:", input_content)
print("번역된 내용:", translated_text)

# 브라우저 닫기
driver.quit()
