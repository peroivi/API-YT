from googleapiclient.discovery import build

api_key = 'AIzaSyCQnghJSvTkupqj9vMbs6SdESD50lQYDEk'

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
    part='statistics',
    id='UC4PIwddtPs6p3asO433oMdQ'
)

response = request.execute()

print(response)