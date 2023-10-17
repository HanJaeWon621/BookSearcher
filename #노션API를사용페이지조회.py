#노션API를사용페이지조회
import requests
import json
# 노션 API 토큰
api_token = "secret_8rp93gMC8IweVNqVmZO3vpYlo0gPnm9RkMPePfHx3kK"

# 페이지 목록을 가져올 노션 데이터베이스 ID
page_id = "f5b331054f384e0eaab845da523b4527"

# API 엔드포인트 URL
url = f"https://api.notion.com/v1/databases/{page_id}/query"
#url = f"https://api.notion.com/v1/blocks/{page_id}/children"
# 요청 헤더 설정
headers = {
    "Authorization": f"Bearer {api_token}",
    "Notion-Version": "2021-08-16"  # 노션 API 버전 선택
}

# API 호출
response = requests.get(url, headers=headers)

# 결과 확인
if response.status_code == 200:
    data = response.json()
    
    # data 변수에 페이지 목록이 포함됩니다.
    print(len(data['results']))
    #print(data['results'])
    i = 0
    while i < len(data['results']):
      type = data['results'][i]['type']
      if type == 'paragraph':
        print(data['results'])
        #print(data['results'][i]['paragraph']['text'][0]['text']['content'])
      elif type == 'child_page':
        page_title = data['results'][i]['child_page']['title']
        print(page_title)
      i += 1
    #formatted_json = json.dumps(data['properties']['title']["title"][0]['plain_text'], indent=2)
    #print(data['properties']['title']["title"][0]['plain_text'])
    #print(data['id'])
else:
    print(f"Error: {response.status_code} - {response.text}")
