import openai
from dotenv import load_dotenv
import os
from seo_fetcher import seo_fetcher_for_keyword
load_dotenv()

openai.api_key = os.getenv('API_KEY')

def generate(keyword):
    seo_data = seo_fetcher_for_keyword(keyword)
    prompt = f"""
    You are blog creation master, now generate/write a well structured blog about {keyword}. 
    Format can be in either HTML or markdown
    SEO Metrics:
    - Difficulty: {seo_data['keyword_difficulty']}
    - Search Volume: {seo_data['search_volume']}
    - Avg CPC: ${seo_data['avg_cpc']}

    Include {{AFF_LINK_1}}, {{AFF_LINK_2}} where dummy affiliate links could go.
    """
    try:
        blog_response = openai.ChatCompletion.create(
            model = "gpt-4",
            messages = [
                {
                    "role": "system",
                    "content": "You are a blog assistant"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature = 0.7
        )

        return blog_response.choices[0].message.content
    except Exception as e:
        return f"Error is : {e}"
