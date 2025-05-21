from bs4 import BeautifulSoup
import requests
import time


def scrape_cheap_ebook():

    url = "https://ebookpoint.pl"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        time.sleep(3)

        if response.status_code == 200:

            soup = BeautifulSoup(response.content, "html.parser")

            div_to_details = soup.find("div", attrs={'class': 'promotion-book'})
            link_to_details = div_to_details.p.a["href"]
            link_to_details = url + link_to_details
            if link_to_details:
                response = requests.get(link_to_details, headers=headers)

                if response.status_code == 200:

                    soup = BeautifulSoup(response.content, "html.parser")

                    # Tytuł książki
                    title_tag = soup.find("h1")
                    title = title_tag.span.text.strip() if title_tag and title_tag.span else None

                    # Cena
                    price_tag = soup.find("ins", attrs={'id': 'cena_e'})
                    price = price_tag.text.strip() if price_tag else None

                    # Autor
                    spans = title_tag.find_all("span") if title_tag else []
                    author_name = spans[1].text.strip() if len(spans) > 1 else None

                    # Liczba stron
                    pages_tag = soup.find("dd", attrs={'class': 'select_druk select_ebook select_bundle'})
                    pages = pages_tag.text.strip() if pages_tag else None


                    # Czy dostępny w formacie EPUB
                    is_epub = soup.find("div", attrs={'class': 'epubFormat'}) is not None

                     # URL okładki
                    image_tag = soup.find("p", attrs={'id': 'mainBookCover'})
                    image_url = image_tag.img["src"] if image_tag and image_tag.img else None

                    # Opis książki
                    div = soup.find('div', id='center-body-opis')
                    paragraphs = div.find_all('p')
                    description = [p.get_text(strip=True) for p in paragraphs]

                    cheap_ebook_data = {
                       "title": title,
                       "price": price,
                       "author_name": author_name,
                       "pages": pages,
                       "is_epub": is_epub,
                       "image_url": image_url,
                       "description": description
                    }

                    return cheap_ebook_data
            else:
                link_to_details = None

            return None

    except Exception as e:

        print(f"Error during scraping data: {e}.")
        return None
