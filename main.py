#Main Python Script
#Responsible for setting up API call

#Import libraries
import requests

def data_init():  
    print("Attempting to grab api data")  
    #grab data from api. (snippet )
    url = 'https://graphql.anilist.co'

    # Here we define our query as a multi-line string
    query = '''
    query ($page: Int, $perPage: Int) {
        Page(page: $page, perPage: $perPage) {
            media(sort: POPULARITY_DESC, type: ANIME) {
                id
                title {
                    english
                }
                averageScore
                episodes
                season
                seasonYear
                status
                format
                popularity
                genres
            }
        }
    }
    '''

    #API won't allow 1000 anime to be grabbed at once, so must be looped over
    all_anime = [] #set up list to collect all responses. 

    for page in range(1, 21): #20 pages = 1000 anime (50 per) 
        variables = {'page': page, 'perPage': 50}
        response = requests.post(url, json={'query': query, 'variables': variables}) #make api request
        all_anime.extend(response.json()['data']['Page']['media'])
        print(f"Fetched page {page}/20")

    #Since title is returned as a dict (e.g., {English: "Name"}), must replace with str value
    for anime in all_anime:
        if anime['title']:
            anime['title'] = anime['title']['english']
        else:
            anime['title'] = None

    return all_anime #List of 1000 dicts. 

fetched_data = data_init()
