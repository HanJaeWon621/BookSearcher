from airtable import Airtable

base_key = 'patv6fNOpKsY5ftkn'
table_name = 'test'

airtable = Airtable(base_key, table_name, api_key='patv6fNOpKsY5ftkn.5ee4953ccbe16dd627852c0749c7bfc9c6446e4a6b25c9f8ddb2d9b9cc1cb3d6')

# 데이터 읽기
records = airtable.get_all()

# 데이터 쓰기
data = {'Field1': 'Value1', 'Field2': 'Value2'}
airtable.insert(data)
