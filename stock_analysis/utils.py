from bs4 import BeautifulSoup
import requests


def scrape_stock_data(symbol, exchange):

    if exchange == "NASDAQ":
        url = f"https://finance.yahoo.com/quote/{symbol}/"
    elif exchange == "NSE":
        url = f"https://finance.yahoo.com/quote/{symbol}.NS/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:

            soup = BeautifulSoup(response.content, "html.parser")

            current_price = soup.find("span", class_="yf-ipw1h0")
            if current_price:
                current_price = current_price.text.strip()
            else:
                current_price = None

            previous_close = soup.find("fin-streamer", class_="yf-1jj98ts")
            if previous_close:
                previous_close = previous_close.text.strip()
            else:
                previous_close = None

            price_changed = soup.find(
                "span", attrs={'data-testid': 'qsp-price-change'})
            if price_changed:
                price_changed = price_changed.text.strip()
            else:
                price_changed = None

            percentage_changed = soup.find(
                "span", attrs={'data-testid': 'qsp-price-change-percent'})
            if percentage_changed:
                percentage_changed = percentage_changed.text.strip()
            else:
                percentage_changed = None

            week_52_range = soup.find("fin-streamer", attrs={'data-field': 'fiftyTwoWeekRange'})
            if week_52_range:
                week_52_split = week_52_range.text.strip().split(" - ")
                week_52_low = week_52_split[0]
                week_52_high = week_52_split[1]
            else:
                week_52_low = None
                week_52_high = None

            market_cap = soup.find(
                "fin-streamer", attrs={'data-field': 'marketCap'})
            if market_cap:
                market_cap = market_cap.text.strip()
            else:
                market_cap = None

            pe_ratio = soup.find(
                "fin-streamer", attrs={'data-field': 'trailingPE'})
            if pe_ratio:
                pe_ratio = pe_ratio.text.strip()
            else:
                pe_ratio = None


            divident_yield = None
            for li in soup.find_all('li', class_='yf-1jj98ts'):
                label = li.find('span', class_='label')
                if label and label.text.strip() == 'Forward Dividend & Yield':
                    value = li.find('span', class_='value')
                    if value:
                        divident_yield = value.text.strip()
                    break

            stock_response = {
                "current_price": current_price,
                "previous_close": previous_close,
                "price_changed": price_changed,
                "percentage_changed": percentage_changed,
                "week_52_high": week_52_high,
                "week_52_low": week_52_low,
                "market_cap": market_cap,
                "pe_ratio": pe_ratio,
                "divident_yield": divident_yield
            }

            return stock_response

    except Exception as e:

        print(f"Error during scraping data: {e}.")
        return None
