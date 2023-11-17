#detail_list > li:nth-child(1) > div.subject > a

import requests
import re
import sys
from bs4 import BeautifulSoup

KG_CATE={
		'1111':'소설',									
		'1112':'시/에세이/기행',									
		'1113':'문학',
		'1114':'인문',									
		'1115':'역사/지리/인물',							
		'1116':'예술/대중문화',
		'1117':'사회/정치/법',
		'1118':'경영/경제',
		'1119':'건강/의학',
		'1120':'자연과학/공학',
		'1121':'컴퓨터/인터넷',
		'1122':'가족/생활/요리',
		'1123':'여행/취미',
		'1124':'외국어',									
		'1126':'청소년',									
		'1141':'오디오북',									
		'1161':'영상',									
		'1171':'다문화자료',	
		'1191':'도서관발간자료'
        }
MID_CATE={
         '1111110':'한국소설','1111120':'영미소설','1111130':'아시아소설','1111140':'유럽소설','1111150':'기타나라소설','1111160':'장르소설',
         '1112110':'시','1112120':'에세이','1112130':'인생/교훈','1112140':'기행/답사',
         '1113110':'문학이론/평론','1113114':'한국문학/고전','1113118':'세계문학/고전','1113120':'언어학/국어학','1113140':'희곡/시나리오',
         '1114110':'인문학일반','1114120':'철학','1114130':'논리/윤리','1114140':'종교','1114150':'심리','1114160':'교육','1114190':'독서/작문',
         '1115110':'역사일반','1115120':'세계사','1115130':'서양사','1115140':'동양사','1115150':'한국사','1115160':'풍속/민속','1115170':'역학/사주','1115180':'문화사','1115190':'인류/고고학','1115200':'신화','1115210':'지리학','1115220':'인물',
         '1116110':'예술일반/미학','1116120':'미술','1116130':'음악','1116140':'사진/영상','1116150':'연극/영화/드라마','1116160':'만화/애니메이션','1116170':'대중문화','1116180':'체육/무용','1116190':'건축/디자인',
         '1117110':'사회과학일반','1117120':'사회학/복지학','1117130':'여성학','1117140':'언론/신문/방송','1117150':'정치/외교/행정','1117170':'국방/군사/통일','1117180':'법률/소송','1117190':'문헌정보학',
         '1118110':'경영일반/이론','1118120':'경영관리/전략/비즈니스','1118130':'마케팅/세일즈','1118140':'유통/창업','1118150':'재테크/금융 ','1118160':'경제일반/이론','1118180':'각국경제','1118200':'자기계발','1118204':'성공/처세','1118210':'인간관계','1118220':'취업/상식/진학',
         '1119110':'건강일반','1119120':'질병치료/예방','1119130':'자연요법/대체의학','1119134':'건강식사/식이요법','1119140':'의학/약학/간호학','1119150':'한의학','1119160':'건강/다이어트/미용',
         '1120110':'교양과학','1120120':'과학이론/일반','1120130':'공학일반','1120140':'생활과학','1120150':'수학/물리/화학','1120160':'생물/지구과학/천문학','1120170':'건축/인테리어','1120190':'환경/도시/조경','1120220':'농축산/수의학',
         '1121110':'컴퓨터 활용/입문','1121120':'컴퓨터공학','1121130':'네트워크/DB/프로그래밍언어','1121140':'홈페이지/그래픽/멀티미디어',
         '1122110':'가정경제/생활','1122140':'부모/육아','1122150':'인테리어/홈패션','1122160':'요리','1122170':'와인/커피/차',
         '1123110':'여행일반/관광학','1123120':'국내여행','1123130':'해외여행','1123140':'테마여행','1123160':'이민/유학','1123170':'취미일반',
         '1124110':'일반영어','1124120':'영어교재/문고','1124130':'수험영어','1124150':'중국어','1124154':'일본어','1124160':'프랑스어','1124180':'기타외국어','1124190':'한자',
         '1126110':'공부방법','1126120':'진로','1126130':'청소년교양','1126140':'예술/문화','1126150':'역사/신화','1126160':'정치/사회/경제','1126170':'문학',
         '1141100':'문학/소설','1141150':'시/에세이','1141200':'인문/사회/역사','1141300':'경제/경영','1141400':'가정/건강/실용','1141500':'아동/청소년','1141600':'영어오디오북'
         }
def GET_CATE_NM(category):
    return_str=''
    return_str = KG_CATE[category]
    return return_str

def GET_CATE_MID_NM(category):

    return_str=''
    return_str = MID_CATE[category]
    return return_str

def SRCH_CATE_MID_LIST(search_term):
    # 특정 문자열이 키 중에 포함되어 있는지 확인
    #search_term = '1111'
    matching_items = {}

    for key in MID_CATE.keys():
        if key.startswith(search_term):
        #if search_term in key:
            matching_items[key] = MID_CATE[key]

    # 검색 결과 출력
    print("일치하는 항목:")
    for key, value in matching_items.items():
        print(f"{key}: {value}")

    return matching_items

def getBookListCrawl2(category_code, middlecategory, searchCategoryNm):

    url2 = 'https://www.library.kr/cyber/ebook/ebookList.do?currentPageNo=1&viewType=desc&serviceType=&possibleType=Y& \
           searchCategoryNm='+ searchCategoryNm +'&searchFilterCondition1=&searchFilterKeyword1=&searchFilterCondition2=&searchFilterKeyword2=&\
           categoryNo1=\
            &categoryNo2='+ category_code +'\
            &categoryNo3='+ middlecategory +'\&serviceTypeLoan=LOAN&searchPerfectYn=N\
            &searchCondition=text_idx&searchKeyword=&recordCountPerPage=100\
            &sortField=PUBLISHEDATE&sortOrder=DESC'
    url = 'https://www.library.kr/cyber/ebook/ebookList.do?viewType=desc&serviceType=&possibleType=Y\
    &searchCategoryNm='+ searchCategoryNm +'&searchFilterCondition1=&searchFilterKeyword1=\
    &searchFilterCondition2=&searchFilterKeyword2=&categoryNo1=&categoryNo2='+ category_code +'\&categoryNo3='+ middlecategory +'\
    &serviceTypeLoan=LOAN&searchPerfectYn=\
    N&searchCondition=text_idx&searchKeyword=&recordCountPerPage=100&sortField=PUBLISHEDATE&sortOrder=DESC'
# 웹 페이지 내용을 가져오기
    print(url)
    response = requests.get(url)

# BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')
    # 원하는 요소(여기서는 제목)를 선택하고 추출
    lists = soup.select('#contents > form > ul.resultList.ebookType.descType > li')
    num = 0
# 추출한 데이터 출력 또는 저장
    list =[]
    for list_item in lists:
        num += 1
        title = soup.select_one('#contents > form > ul.resultList.ebookType.descType > li:nth-child(' + str(num) +') > div.bookDataWrap > strong > a > span')        #제목
        link = soup.select_one('#contents > form > ul.resultList.ebookType.descType > li:nth-child(' + str(num) +') > div.bookDataWrap > div > a')        #제목
        cate_nm = GET_CATE_NM(category_code)
        cate_mid_nm = GET_CATE_MID_NM(middlecategory)
        title_v = title.text
          # 제목 텍스트 출력
        input_str = link.get('href')                    # href 속성 값을 가져오기
        if input_str.find('EPUB') != -1:
            book_id = parsing(input_str)
            print(cate_nm, cate_mid_nm, title_v, book_id)
            list.append(title_v)
    return list
def parsing(input_str):
# 정규 표현식을 사용하여 함수 호출 부분 추출
    match = re.search(r"fnProcBorrowEbook\('(.*?)','(.*?)','(.*?)','(.*?)'\)", input_str)
    pattern = r"'(.*?)'"
    result = re.findall(pattern, input_str)
    #print("파라미터 1:", result[1])
    rs = result[1]
    return rs
 
def main():
    #print(CATE)
    #SRCH_CATE_MID_LIST('1112')
    #python myscript.py arg1 arg2 arg3
    try:
        params = sys.argv[0:]
        #print(params[1])
        full_cate_str = params[1]
        if len(full_cate_str)==4:
            SRCH_CATE_MID_LIST(full_cate_str)
        elif len(full_cate_str)==7:
            cate_str= full_cate_str[:4]
            getBookListCrawl2(cate_str,full_cate_str)
        else:
            print('캐티고리 코드 부적합')
        #for param in params:
            #print(param)
    except IndexError as e:
        print("IndexError")
        print(KG_CATE)
    finally:
        print("-----------")
    #getBookListCrawl(cate_str,full_cate_str)
#python 경기도사이버도서관책목록.py 1112120
# 파라미터 출력
    
if __name__ == '__main__':
    main()




















