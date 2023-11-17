#detail_list > li:nth-child(1) > div.subject > a

import requests
import re
from bs4 import BeautifulSoup

CATE={'A1':'문학',
      'A2':'에세이/산문',
      'A4':'인문',
      'A5':'역사',
      'A7':'사회',
      'A8':'경제/비즈니스 전체',
      'AF':'취미/여행',
      'A9':'자연/과학',
      'AA':'컴퓨터/인터넷'
}
A1_CATE={
    '01':'한국소설',
    '02':'한국근대소설',
    '03':'외국소설',
    '04':'고전',
    '05':'이론과/평론',
    '06':'어른을위한동화',
    '07':'SF'}
#A2 에세이/산문
A2_CATE={
    '01':'산문집',
    '02':'에세이',
    '03':'휴먼스토리',
    '04':'자기계발',
    '05':'기행/답사',
    '06':'명상/잠언',
    '07':'호기심잡학상식'}
A4_CATE={
    '01':'인문학산책',
    '02':'한국/동양철학',
    '03':'서양철학',
    '04':'심리/정신분석'
    }
A5_CATE={
    '01':'한국사',
    '02':'세계사',
    '03':'역사이론/고고학',
    '04':'인물이야기',
    '05':'지리'
    }
A7_CATE={
    '01':'사회과학산책',
    '02':'사회학이해',
    '03':'정치/외교',
    '04':'여성/남성',
    '05':'법률/행정/복지',
    '06':'교육/환경',
    '07':'언론/미디어'}
    #A8 경제/비즈니스 전체
A8_CATE={
    '01':'경제/경영',
    '02':'기업/경영자/리더십',
    '03':'성공철학/자기계발',
    '04':'마케팅/세일즈',
    '05':'벤처&인터넷비즈니스',
    '06':'재테크/투자',
    '07':'창업/취업',
    '08':'기업실무관리',
    '09':'리포트'}
AF_CATE={
    '01':'여행/관광',
    '02':'스포츠',
    '03':'취미서',
    '04':'운세/해몽',
    '05':'기타'
    }
A9_CATE={
    '01':'과학산책',
    '02':'수학/물리',
    '03':'화학/생명',
    '04':'지구/천문'
    }
AA_CATE={
    '01':'컴퓨터입문/활용',
    '02':'인터넷/홈페이지',
    '03':'멀티미디어/게임/그래픽',
    '04':'프로그래밍'
    }
def GET_CATE_NM(category, middlecategory):
    return_str=''
    if category =='A1':
        return_str = A1_CATE[middlecategory]
    elif category =='A2':
        return_str = A2_CATE[middlecategory]
    elif category =='A4':
        return_str = A4_CATE[middlecategory]
    elif category =='A5':
        return_str = A5_CATE[middlecategory]
    elif category =='A7':
        return_str = A7_CATE[middlecategory]
    elif category =='A8':
        return_str = A8_CATE[middlecategory]
    elif category =='AF':
        return_str = AF_CATE[middlecategory]
    elif category =='A9':
        return_str = A9_CATE[middlecategory]
    elif category =='AA':
        return_str = AA_CATE[middlecategory]

    return return_str

def GET_CATE_DTL_DIC(category):
    return_str=''
    if category =='A1':
        return A1_CATE
    elif category =='A2':
        return A2_CATE
    elif category =='A4':
        return A4_CATE
    elif category =='A5':
        return A5_CATE
    elif category =='A7':
        return A7_CATE
    elif category =='A8':
        return A8_CATE
    elif category =='AF':
        return AF_CATE
    elif category =='A9':
        return A9_CATE
    elif category =='AA':
        return AA_CATE

def getBookListCrawl(category_code, middlecategory):
# 크롤링할 웹 페이지의 URL 설정
    url = 'https://ebook.gimpo.go.kr/FxLibrary/product/list/?itemdv=1 \
    &sort=3&page=1&itemCount=10&pageCount=100&category='+category_code+ '\
    &middlecategory='+ middlecategory +'&cateopt=total&group_num=recommand&catenavi=middle&category_type=book& \
    searchoption=&keyoption=&keyoption2=&keyword=&listfilter=lendable_list&selectview=list_on&searchType=&name=&publisher=&author=&terminal=0'  # 크롤링하려는 웹 페이지 URL로 변경해야 합니다.

# 웹 페이지 내용을 가져오기
    response = requests.get(url)

# BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')

# 원하는 요소(여기서는 제목)를 선택하고 추출

    lists = soup.select('#detail_list > li')
    num = 0
# 추출한 데이터 출력 또는 저장
    listA=[]
    for list_item in lists:
        num += 1
        category = soup.select_one('#detail_list > li:nth-child(' + str(num) +') > div.category > span') #카테고리
        title = soup.select_one('#detail_list > li:nth-child(' + str(num) +') > div.subject > a')        #제목
        loan_cnt = soup.select_one('#detail_list > li:nth-child(' + str(num) +') > div.info > ul.i2 > li:nth-child(1) > strong')
        detl_cate_nm = GET_CATE_NM(category_code, middlecategory)
        #print(category.text, detl_cate_nm, title.text, loan_cnt.text)  # 제목 텍스트 출력
        print(title)
        listA.append(title.text)
        input_str = title.get('href')                    # href 속성 값을 가져오기
        #parsing(input_str)
    
    return listA

def parsing(input_str):
# 정규 표현식을 사용하여 함수 호출 부분 추출
    match = re.search(r"goView\('(.*?)','(.*?)','(.*?)','(.*?)'\)", input_str)
# 각 파라미터 값을 추출
    param1 = match.group(1)
    param2 = match.group(2)
    param3 = match.group(3)
    param4 = match.group(4)
    # 파싱된 파라미터 출력
    '''
    print("파라미터 1:", param1)
    print("파라미터 2:", param2)
    print("파라미터 3:", param3)
    print("파라미터 4:", param4)
    '''
def main():
    getBookListCrawl('A2','04')

if __name__ == '__main__':
    main()

























