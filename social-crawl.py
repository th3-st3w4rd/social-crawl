import re

import requests
from bs4 import BeautifulSoup

url = "" # insert URL here.
headers = "" # insert headers here.

def get_social_media_info():
    """Scrapes a site's homepage for common social links: YouTube, FaceBook, Instagram, and Twitter.
    Returns a Dictionary."""
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    soup = soup.find_all("a")
    socials_list = ["youtube", "instagram", "facebook", "twitter", "spotify"]
    social_media_info = {}
    for item in soup:
        item =str(item)
        for social in socials_list: 
            if social in item:
                    social_url = re.findall('(?<=href="https://)(.*?)(?=")', item)
                    if len(social_url) > 0:
                        social_media_info[f'{social}'] = social_url[0]
    if len(social_media_info) > 0:
        return social_media_info
    else:
        return f"No socials found for: {url}"
    
print(get_social_media_info())