import sys
from PyQt5.QtWidgets import QApplication, QWidget,QLabel, QLineEdit ,QInputDialog,QListWidget, QListWidgetItem, QVBoxLayout, QHBoxLayout, QPushButton
from 김포도서관책목록 import *
from 경기도사이버도서관책목록 import *
from 책검색 import *
def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("도서검색")

    # 수직 레이아웃 생성
    vertical_layout = QVBoxLayout()
    vertical_layout1 = QVBoxLayout()
    vertical_layout2 = QVBoxLayout()

    # 수평 레이아웃 생성
    horizontal_layout = QHBoxLayout()
    horizontal_layout1 = QHBoxLayout()
    horizontal_layout2 = QHBoxLayout()
    horizontal_layout3 = QHBoxLayout()
    horizontal_layout4 = QHBoxLayout()
    horizontal_layout5 = QHBoxLayout()
    # 버튼 생성
    button1 = QPushButton("김포도서관")
    button2 = QPushButton("경기도도서관")
    button3 = QPushButton("검색")
    label = QLineEdit("")
    label2 = QLineEdit("")
    label3 = QLabel("")
    #label.setGeometry(30, 100, 500, 550)
    def add_item():
      list_widget.clear()
      list_widget2.clear()
      list_widget3.clear()
      for key, value in CATE.items():
        list_widget.addItem("{}: {}".format(key, value))
      list_widget.itemClicked.connect(update_selected_item_label)
    # Connect the button click event to the add_item function
    button1.clicked.connect(add_item)

    def add_item2():
      list_widget.clear()
      for key, value in KG_CATE.items():
        list_widget.addItem("{}: {}".format(key, value))
      list_widget.itemClicked.connect(update_selected_item_label)
    # Connect the button click event to the add_item function
    button2.clicked.connect(add_item2)

    def searchBook():
        # 텍스트 입력 대화 상자 열기
        srch_text = label.text()
        srch_result = getBookListCrawlSrch(srch_text)
        
        print("사용자 입력:", srch_text)
        label3.setText(srch_result)
    # 엔터 키에 대한 이벤트 핸들러 등록
    label.returnPressed.connect(searchBook)
    button3.clicked.connect(searchBook)
    list_widget = QListWidget()
    list_widget2 = QListWidget()
    list_widget3 = QListWidget()
    
    def update_selected_item_label(item):
      selected_items = list_widget.selectedItems()
      key = selected_items[0].text().split(":")[0]
      list_widget2.clear()
      list_widget3.clear()
      global flag
      if key=='A1':
        C = GET_CATE_DTL_DIC(key)
        flag='b1'
      elif key=='A2':
        C = GET_CATE_DTL_DIC(key)
        flag='b1'
      elif key=='A4':
        C = GET_CATE_DTL_DIC(key)
        flag='b1'
      elif key=='A5':
        C = GET_CATE_DTL_DIC(key)
        flag='b1'
      elif key=='A7':
        C = GET_CATE_DTL_DIC(key)
        flag='b1'
      elif key=='A8':
        C = GET_CATE_DTL_DIC(key)
        flag='b1'
      elif key=='AF':
        C = GET_CATE_DTL_DIC(key)
        flag='b1'
      elif key=='A9':
        C = GET_CATE_DTL_DIC(key)
        flag='b1'
      elif key=='AA':
        C = GET_CATE_DTL_DIC(key)
        flag='b1'
      else:
        C = SRCH_CATE_MID_LIST(key)
        flag='b2'
      
      list_widget2.clear()
      for key, value in C.items():
            list_widget2.addItem("{}: {}".format(key, value))

    # 두번째 카테고리 선택
    def update_selected_item_label2(item):
      label2.setText('로딩중....')
      selected_items = list_widget.selectedItems()
      selected_items2 = list_widget2.selectedItems()
      key = selected_items[0].text().split(":")[0]
      key2 = selected_items2[0].text().split(":")[0]
      searchCategoryNm = selected_items2[0].text().split(":")[1]
      print(key,key2)
      list_widget3.clear()
      if flag == 'b1':
        bookList = getBookListCrawl(key,key2)
      elif flag == 'b2':
        bookList = getBookListCrawl2(key,key2, searchCategoryNm)
        
      setBookList(bookList)
      
      #label.setText('')
    def setBookList(bookList):
      for list_item in bookList:  
        list_widget3.addItem(list_item)
      
      label2.setText('')
    def update_selected_item_label3(item):
      selected_items = list_widget3.selectedItems()
      
      #key = selected_items[0].text().split(":")[0]

      print(selected_items[0].text())
      label2.setText(selected_items[0].text())
      
    # Connect the itemClicked signal to the update_selected_item_label function
    list_widget.itemClicked.connect(update_selected_item_label)
    list_widget2.itemClicked.connect(update_selected_item_label2)
    list_widget3.itemClicked.connect(update_selected_item_label3)
    # 버튼을 수평 레이아웃에 추가
    horizontal_layout.addWidget(button1)
    horizontal_layout.addWidget(button2)
    horizontal_layout1.addWidget(label)
    horizontal_layout1.addWidget(button3)

    #vertical_layout2.addChildWidget(list_widget)
    #vertical_layout2.addChildWidget(list_widget2)
    horizontal_layout2.addWidget(list_widget)
    horizontal_layout2.addWidget(list_widget2)
    horizontal_layout3.addWidget(list_widget3)

    horizontal_layout4.addWidget(label2)
    horizontal_layout5.addWidget(label3)
    #horizontal_layout2.addWidget(list_widget3)

    horizontal_layout2.insertLayout(1, vertical_layout2)

    vertical_layout.insertLayout(0, horizontal_layout)
    vertical_layout.insertLayout(1, horizontal_layout1)
    vertical_layout.insertLayout(2, horizontal_layout2)
    vertical_layout.insertLayout(3, horizontal_layout3)
    vertical_layout.insertLayout(4, horizontal_layout4)
    vertical_layout.insertLayout(5, horizontal_layout5)
    # 추가적인 위젯 또는 레이아웃을 수직 레이아웃에 추가할 수 있습니다.

    # 윈도우에 수직 레이아웃 설정
    window.setLayout(vertical_layout)

    window.setGeometry(100, 100, 500, 500)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
