import requests

# 액세스 토큰을 설정합니다.
access_token = 'secret_8rp93gMC8IweVNqVmZO3vpYlo0gPnm9RkMPePfHx3kK'

# 페이지의 URL을 설정합니다.
page_url2 = 'https://www.notion.so/2022-23-4a87f0d091664c429afdec9ef7949784'
page_url = '4a87f0d091664c429afdec9ef7949784'

# 페이지 내용을 가져오기 위한 요청을 생성합니다.
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json',
    "Notion-Version": "2021-08-16"  # 노션 API 버전 선택
}

response = requests.get(f'https://api.notion.com/v1/pages/{page_url}', headers=headers)

# 응답을 확인하고 페이지 내용을 출력합니다.
if response.status_code == 200:
    page_data = response.json()
    page_contents = page_data['properties']['title']['title'][0]['text']['content']
    print(page_data)
else:
    print(f'페이지 내용을 가져오는 데 실패했습니다. 상태 코드: {response.status_code}')
