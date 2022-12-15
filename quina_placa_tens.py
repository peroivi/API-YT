
from googleapiclient.discovery import build

api_key = 'key-publica-api'

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
    part='statistics',
    forUsername='elrubius'
)

response = request.execute()
num_subs = int(response['items'][0]['statistics']['subscriberCount'])
print ("suscriptors:",num_subs)

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
