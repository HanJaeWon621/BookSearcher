#지메일api사용
'''
지메일 api를 사용해서 지메일을 내용을 읽는다.
읽은 내용 번역 API(구글, DEEPL)를 사용해서 번역한다.
'''
import os
from datetime import datetime
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
#from google.cloud import translate_v2 as translate
import requests
# Gmail API 권한 스코프 설정
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
key_file = "경로/서비스계정키.json"
def list_messages(service, user_id, query=''):
    try:
        response = service.users().messages().list(userId=user_id, q=query).execute()
        messages = response.get('messages', [])
        return messages
    except Exception as e:
        print('An error occurred:', e)
        return []

def get_message(service, user_id, msg_id):
    try:
        message = service.users().messages().get(userId=user_id, id=msg_id).execute()
        return message
    except Exception as e:
        print('An error occurred:', e)
        return None
#google 번역 api
def translate_text(text, target_language):
    client = translate.Client.from_service_account_json(key_file)
    result = client.translate(text, target_language=target_language)
    return result["translatedText"]

# DeepL API 인증 토큰
auth_token = "YOUR_AUTH_TOKEN"

def translate_text_deepl(text, target_lang):
    url = "https://api.deepl.com/v2/translate"
    params = {
        "auth_key": auth_token,
        "text": text,
        "target_lang": target_lang
    }
    response = requests.post(url, data=params)
    if response.status_code == 200:
        translated_text = response.json()["translations"][0]["text"]
        return translated_text
    else:
        print("Translation failed. Status code:", response.status_code)
        return None
def main():
    # Gmail API를 사용하기 위한 인증 설정
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Gmail API 서비스 빌드
    service = build('gmail', 'v1', credentials=creds)

    # 이메일 목록 조회
    query = "subject:번역_test"
    messages = list_messages(service, 'me', query=query)
    #messages = list_messages(service, 'me', query='is:unread')  # 읽지 않은 메일 목록 조회
    for msg in messages:
        message = get_message(service, 'me', msg['id'])
        
        if message:
            print('Subject:', message['payload']['headers'][3]['value'])
            print('From:', message['payload']['headers'][4]['value'])
            print('Content:', message['snippet'])
            internal_date_milliseconds = int(message['internalDate'])  # 여기에 Gmail API에서 받아온 internalDate 값을 넣으세요

            # Epoch 시간 (밀리초 단위)을 파이썬의 datetime 형식으로 변환
            internal_date_seconds = internal_date_milliseconds / 1000
            formatted_date = datetime.fromtimestamp(internal_date_seconds).strftime('%Y-%m-%d %H:%M:%S')

            print(formatted_date)
            print('Date:', message['internalDate'])
            print('---')
        
if __name__ == '__main__':
    main()
