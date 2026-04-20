# Anime Data Analysis
By TomPancakes

## Summary: 
This project uses explores anime trends (Ratings, popularity) using data from the GraphQL AniList API. https://docs.anilist.co/

## Tools used

- **Anilist API** - API powered by GraphQL query language
- **Requests** - Library to make API requests.
- **Pandas** - Data Manipulation.
- **Matplotlib** - Data graphing.

## Results/findings
yes. Results were indeed found. I think. 

## How to run
Running it usually helps. 

## limitations.
- Data limited to only top 1000 popular entries. (whole database is 20,000 approx) Niche entries excluded.
- Score is given to by AniList users. Therefore, popularity & score are skewed towards the typical anilist demographic. (i.e, more casual anime fans won't make an anilist account and contribute to data) 
- Each new season of an anime is considered a separate entry. Low popularity on later seasons may not suggest the series as a whole is unpopular. (e.g., s1 might be popular, s4 less so)

