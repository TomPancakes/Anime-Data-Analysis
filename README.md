# Anime Data Analysis
By TomPancakes

## Summary: 
Are old or new anime more highly rated? Which genres are most popular? What about movies vs series? 
This projects explores those very questions using data from the GraphQL AniList API. https://docs.anilist.co/


## Tools used
- **Anilist API** - API powered by GraphQL query language
- **Requests** - Library to make API requests.
- **Pandas** - Data Manipulation.
- **Matplotlib** - Data graphing.

## Results/findings
yes. Results were indeed found. I think.
- R value of 0.34 between popularity & score. Not as high as you'd expect. While the most popular shows did tend to be higher in the ratings, there are also many highly rated shows with lower popularity.
- etc

## How to run
- Install dependencies: pip install requests pandas matplotlib jupyter
- Open anime_data.analysis.ipynb and run all cells in order
- NOTE: Not necessary to run, but the program will use the local .json data if available rather than gathering new API data via main.py. If you want the program to fetch more recent data, simply delete the JSON file from the project folder then run all cells. 

## limitations.
- Data limited to only top 1000 popular entries. (whole database is 20,000 approx) Niche entries excluded.
- Score is given to by AniList users. Therefore, popularity & score are skewed towards the typical anilist demographic. (i.e, more casual anime fans won't make an anilist account and contribute to data) 
- Each new season of an anime is considered a separate entry. Low popularity on later seasons may not suggest the series as a whole is unpopular. (e.g., s1 might be popular, s4 less so)

