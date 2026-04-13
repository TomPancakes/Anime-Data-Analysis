#Main Python Script
#Responsible for setting up API call

#Import libraries
import requests

def data_init():    
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
            }
        }
    }
    '''

    variables = {'page': 1, 'perPage': 50}

    # Make the HTTP Api request
    response = requests.post(url, json={'query': query, 'variables': variables})
    return response

data_init()
