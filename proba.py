

def main():
    # Creem un ficher per guardar tots el logs
    setup_logger()
    # Query Youtube API for authentication or load from file
    credencials = get_credentials(role)
    # agafem la api de yt amb la que estarem treballant // portal per demanar coses a yt
    youtube = googleapiclient.discovery.build(config.API_SERVICE_NAME, config.API_VERSION, credentials=creds)
    # agafem tots els videos es complicat agafar totrs els videos amb aquesta api, es millor demanar per playlists 13:33 api burocratica, moltes regles i els parametres hand e ser perfectes
    videos = load_videos(youtube)
#  commentThreads es retorna els comentaris principals, es a dir no las respostes a altres comentaris
# podem ficar comentaris -> insert, o listarlos -> list
                                        # podem veure el id del comentari
                                        # podem verure respuestas, replies
                                        #  o la info -> snippet
# la api te moltisimes regles
# podemos hacer 10.000 peticiones al dia 
# ban cuesta -> 50 punts de la api.
# limitan para no saturar el server i si quieres hacer un app que gaste sus datos a pagar, normalmente son de apgo.
# twitter por ejemplo gana mucho dinero con esto.

# soluciones -> no hacer nada
# ejecutar 1 vez al dia para los 5 ultimos videos
# una solucio seria fer que el script treballi sobre la web en comptes de la api