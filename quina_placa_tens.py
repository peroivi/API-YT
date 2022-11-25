
from googleapiclient.discovery import build
# la indiquem directament pq es publica i no ns preocupa que algu la pugui obtenir
api_key = 'AIzaSyCQnghJSvTkupqj9vMbs6SdESD50lQYDEk'
# id meu canal = UCzvqiTA_OIQC3y33XFl3aYA

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
    part='statistics',
    forUsername='elrubius'
)

response = request.execute()
num_subs = int(response['items'][0]['statistics']['subscriberCount'])

if num_subs > 100000:
    print("Enhorabona tens la placa de plata!")
    if num_subs > 1000000:
        print("Enhorabona tens la placa d'or!")
        if num_subs > 10000000:
            print("Enhorabona tens la placa de diamant!")
            if num_subs > 50000000:
                print("Enhorabona tens la placa de rubi!")
                if num_subs > 100000000:
                    print("Enhorabona tens la placa de diamant vermell!")
else:
    print("No tens cap placa :(")