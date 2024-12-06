import requests
from bs4 import BeautifulSoup

def scrape_products(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    products = []
    for product in soup.select('.ads-list-photo-item'):  # CSS selector for product items
        # Extract product name
        name_element = product.select_one('.ads-list-photo-title')
        name = name_element.text.strip() if name_element else "Unknown Product"

        # Extract product price
        price_element = product.select_one('.ads-list-price')  # Update to the correct class
        if price_element:
            price_text = price_element.text.strip()
            # Extract only digits from the price
            price = int(''.join(filter(str.isdigit, price_text)))
        else:
            price = None

        # Extract product link
        link_element = product.select_one('a')
        if link_element:
            link = "https://999.md" + link_element['href']
        else:
            link = None

        # Append product data to the list
        products.append({"name": name, "price": price, "link": link})

    return products


if __name__ == "__main__":
    url = "https://999.md/ro/list/musical-instruments/amplifiers"
    products = scrape_products(url)
    for product in products:
        print(product)
