#구글 클라이언트 시크리트 파일을 사용해서 토큰json생성

from google_auth_oauthlib.flow import InstalledAppFlow
   
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']  # 필요한 권한 스코프 설정
   
flow = InstalledAppFlow.from_client_secrets_file('client_secret_218459143779-1shvbjqota8fk0cfbkimhc0rnn5fmdti.apps.googleusercontent.com.json', SCOPES)
creds = flow.run_local_server(port=0)
   
with open('token.json', 'w') as token:
  token.write(creds.to_json())