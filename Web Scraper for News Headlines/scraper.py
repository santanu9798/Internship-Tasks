"""
Web Scraper for News Headlines
Author: [Your Name]
Internship Task - Elevate Labs
"""

import requests
from bs4 import BeautifulSoup

def scrape_headlines(url, output_file="headlines.txt"):
    try:
        # Step 1: Send GET request
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()

        # Step 2: Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Step 3: Extract headlines (BBC example: <h3>)
        headlines = soup.find_all([ 'h2'])

        # Step 4: Save headlines into a text file
        with open(output_file, "w", encoding="utf-8") as file:
            for idx, headline in enumerate(headlines, start=1):
                text = headline.get_text(strip=True)
                if text:
                    file.write(f"{idx}. {text}\n")

        print(f" {len(headlines)} Headlines scraped and saved to '{output_file}'")

    except requests.exceptions.RequestException as e:
        print(" Error:", e)


if __name__ == "__main__":
    news_url = "https://www.bbc.com/news"
    scrape_headlines(news_url)

