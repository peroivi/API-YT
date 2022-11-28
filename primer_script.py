
from googleapiclient.discovery import build
# la indiquem directament pq es publica i no ns preocupa que algu la pugui obtenir
api_key = 'AIzaSyCQnghJSvTkupqj9vMbs6SdESD50lQYDEk'

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
    part='statistics',
    id='UC4PIwddtPs6p3asO433oMdQ'
)

response = request.execute()

print(response)