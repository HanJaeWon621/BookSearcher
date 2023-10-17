#detail_list > li:nth-child(1) > div.subject > a

import requests
import re
from bs4 import BeautifulSoup

def getBookListCrawlSrch(keyword):
# 크롤링할 웹 페이지의 URL 설정 %EC%9E%90%EA%B8%B0%EA%B3%84%EB%B0%9C

    url = 'https://www.library.kr/cyber/ebook/ebookList.do?viewType=desc&serviceType=&possibleType=&\
    searchCategoryNm=일반자료&searchFilterCondition1=&searchFilterKeyword1=&searchFilterCondition2=&searchFilterKeyword2=&categoryNo1=&categoryNo2=\
    &categoryNo3=&searchPerfectYn=N&searchCondition=text_idx&searchKeyword=' + keyword +'&recordCountPerPage=10&sortField=PUBLISHEDATE&sortOrder=DESC'

    url2 = 'https://ebook.gimpo.go.kr/FxLibrary/product/list/?page=1&keyoption2=1&category=\
      &searchoption=1&searchType=search&keyword='+ keyword #마음의 평화' 도리의 그림 수업
# 웹 페이지 내용을 가져오기
    response = requests.get(url)
    response2 = requests.get(url2)
# BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')
    soup2 = BeautifulSoup(response2.text, 'html.parser')
# 원하는 요소(여기서는 제목)를 선택하고 추출
    #contents > form > ul.resultList.ebookType.descType > li:nth-child(7) > div.bookDataWrap > strong > a > span
    lists = soup.select('#contents > form > ul.resultList.ebookType.descType > li')
    lists2 = soup2.select('#detail_list > li') #김포
    num = 0
    srchText=''
    if len(lists) >0 :
        srchText = keyword + ' 경기사이버도서관에서 검색되었습니다.'
    else:
        if len(lists2) >0 :
            srchText = keyword + ' 김포도서관에서 검색되었습니다.' 
        else:
            srchText = keyword + ' 존재하지 않습니다.'  
    
    print(srchText)
    return srchText
def main():
    getBookListCrawlSrch('PyQt5 Tutorial - 파이썬으로 만드는 나만의 GUI 프로그램')#링컨 명연설집

if __name__ == '__main__':
    main()