from re import sub, compile
import os
import requests

from bs4 import BeautifulSoup


URL = os.getenv("AMAZONE_BASE_URL", "https://www.amazon.com/")
HEADERS = (
    {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
        "Accept-Language": "en-US"
    }
)
STORE = 'amazon'


class AmazonProducts():
    """
    Provide title, price, star, url, image of an product on Amazon store.
    """
    def __init__(self, url=URL, store=STORE, *args, **kwargs):
        self.url = url
        self.store = store

    def get_title(self, soup):
        """
        Return list of titles of product from Amazon store
        """
        try:
            titles = soup.find_all("h2", class_=compile(r"a-size-mini a-spacing-none a-color-base *"))
            titles[:] =  [title.a.span.get_text().strip() if title.a.span.get_text() else None for title in titles]
        except AttributeError:
            return []
        return titles


    def get_price(self, soup):
        """
        Return price of product from Amazon store
        """
        try:
            prices = soup.find_all("span", class_="a-offscreen")
            prices[:] =  [price.get_text().strip() if price.get_text() else None for price in prices]
        except AttributeError:
            return []
        return prices

    def get_image(self, soup):
        """
        Return image of product from Amazon store
        """
        try:
            images = soup.find_all("img", class_="s-image")
            images[:] = [image.get('src') if image.get('src') else None for image in images]
        except AttributeError:
            return []
        return images

    def get_all_information(self, soup):
        """
        Return all information of product
        """
        titles = self.get_title(soup)
        images = self.get_image(soup)
        prices = self.get_price(soup)
        search_results = []

        for search_result in zip(titles, images, prices):
            search_results.append({
                'title': search_result[0],
                'image': search_result[1],
                'price': search_result[2],
                'source': self.store,
            })

        return search_results

    def parse(self, search_term=None):
        """
        This function parses the page and return list of products
        """
        search_url = self.url
        sort_param_asc = "&s=price-asc-rank"

        if search_term:
            search_url = self.url + "s?k=" + sub(r"\s+", "+", str(search_term)) + "&ref=nb_sb_noss_2" + sort_param_asc

        try:
            data = requests.get(search_url, headers=HEADERS).text
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)
        soup = BeautifulSoup(data, 'lxml')
        return self.get_all_information(soup)
