from bs4 import BeautifulSoup
import requests


def scrape_cheap_ebook():

    url = "https://ebookpoint.pl/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:

            soup = BeautifulSoup(response.content, "html.parser")

            # pe_ratio = soup.find(
            #     "fin-streamer", attrs={'data-field': 'trailingPE'})
            # if pe_ratio:
            #     pe_ratio = pe_ratio.text.strip()
            # else:
            #     pe_ratio = None

            # cheap_ebook_response = {
            #    
            # }

            print(soup.contents)

            return None

    except Exception as e:

        print(f"Error during scraping data: {e}.")
        return None
