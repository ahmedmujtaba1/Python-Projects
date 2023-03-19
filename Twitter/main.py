import tweepy
import pandas as pd
import os
import datetime as dt

# API key: X4Y7Y04awoRF1MCyQa7GihgnP
# API secret key: 1Df4QFiMAxSmDNx2mpFv1DSLx3CZgHwQWDC4eO3QG8T6vCXv4E
# Bearer token: AAAAAAAAAAAAAAAAAAAAALg8HgEAAAAA39cREsdqUFaFKjLPI10LuDzSOdo%3D58W5NRZXsfjn9DT3s9kJBTuwqkPBnmxZpIdegJSfbfbpy6WYpC
# Access token: 375970946-vtiEnm2V2cv7GehiKclmzglcOXODsiYk4NHAH6Ty
# Access token secret: 4igL12gmSDv9hxmN9Uk87xKaMEbVUYLummFetGrLLHBT2


# Authenticate to Twitter
def run(critera, quantity, language):
    auth = tweepy.OAuthHandler("X4Y7Y04awoRF1MCyQa7GihgnP", 
        "1Df4QFiMAxSmDNx2mpFv1DSLx3CZgHwQWDC4eO3QG8T6vCXv4E")
    auth.set_access_token("375970946-vtiEnm2V2cv7GehiKclmzglcOXODsiYk4NHAH6Ty", 
        "4igL12gmSDv9hxmN9Uk87xKaMEbVUYLummFetGrLLHBT2")
    api = tweepy.API(auth)
    # Realizamos la búsqueda y guardamos en listas la información de nuestro interés.
    test = []
    tweets = []
    username = []
    screen_name = []
    date = []
    hashtags = []
    results = {}
    for tweet in api.search(q=criteria, lang=language, rpp=500, count=quantity):
        tmp = tweet.entities['hashtags']
        test.append(tweet)
        tweets.append(tweet.text)
        username.append(tweet.user.name)
        screen_name.append('@'+tweet.user.screen_name)
        date.append(tweet.created_at)
        hashtags.append(tweet.entities['hashtags'])
        
    # Creamos un dataframe con la busqueda realizada.
    results = pd.DataFrame({'username':username, 'screen_name':screen_name, 'date':date, 'tweet':tweets, 'hashtags': hashtags})

    # Guardando los resultados en una carpeta de búsquedas
    actual_dir = os.getcwd()
    path = os.chdir(actual_dir)
    search_time = dt.datetime.now().strftime('%Y_%m_%d')
    save_directory = f'{criteria}-{search_time}'
    try:
        os.chdir(save_directory)
        _save_file(results)
    except Exception as e:
        print('Creando carpeta de busqueda.')
        os.mkdir(save_directory)
        os.chdir(save_directory)
        _save_file(results)

def _save_file(df):
    return df.to_csv(f'results-{dt.datetime.now().strftime("%Y_%m_%d")}.csv')
    # Windows
    # results.to_excel('D:\\Projects\\tweetsScraper\\results.xlsx')

if __name__ == "__main__":
    print('Programa que te devuelve la cantidad de tweets definida por ti, según tu criterio de búsqueda.')
    select = int(input("""Selecciona el idioma de tu preferencia:
    1. Español
    2. Inglés
    """))
    language = ''
    if select == 1:
        language = 'es'
    elif select == 2:
        language = 'en'
    else:
        print('Selección no válida')
        print('Se selecciona español por defecto')
        language = 'es'
        

    criteria = input('Qué deseas buscar en twitter? ')
    quantity = int(input('Cuántos tweets deseas obtener? '))
    run(criteria, quantity, language)