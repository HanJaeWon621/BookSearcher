import requests

# 노션 API 토큰
api_token = "secret_8rp93gMC8IweVNqVmZO3vpYlo0gPnm9RkMPePfHx3kK"

# 페이지 목록을 가져올 노션 데이터베이스 ID
database_id = "560536cedb9f46919c3cb637575067c6"

# API 엔드포인트 URL
url = f"https://api.notion.com/v1/databases/{database_id}/query"

# 요청 헤더 설정
headers = {
    "Authorization": f"Bearer {api_token}",
    "Notion-Version": "2021-08-16"  # 노션 API 버전 선택
}

# API 호출
response = requests.post(url, headers=headers)

# 결과 확인
if response.status_code == 200:
    data = response.json()
    # data 변수에 페이지 목록이 포함됩니다.
    print(data)
else:
    print(f"Error: {response.status_code} - {response.text}")
