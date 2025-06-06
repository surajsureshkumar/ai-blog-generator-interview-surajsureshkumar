import random

def seo_fetcher_for_keyword(keyword):
    return{
        "keyword_difficulty": random.randint(1000,50000),
        "search_volume": random.randint(10,90),
        "avg_cpc":random.uniform((0.5, 5.0), 2)

    }
