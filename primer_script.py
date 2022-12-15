from googleapiclient.discovery import build

api_key = 'key-publica-api'

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
    part='statistics',
    id='id-canal'
)

response = request.execute()

print(response)
