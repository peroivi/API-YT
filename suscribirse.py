from googleapiclient.discovery import build
# la indiquem directament pq es publica i no ns preocupa que algu la pugui obtenir
api_key = 'AIzaSyCQnghJSvTkupqj9vMbs6SdESD50lQYDEk'

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.subscriptions().insert(
    part='snippet',
    body=dict(
      snippet=dict(
        resourceId=dict(
          channelId='UCzvqiTA_OIQC3y33XFl3aYA'
        )
      )
))

response = request.execute()

print(response)