from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

def scrape_cityrhythm():
    scrape_url = 'https://www.cityrhythmfragrance.com/shop'
    base_url = 'https://www.cityrhythmfragrance.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Referer': 'https://www.google.com/',
    }

    response = requests.get(scrape_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = []
    other_keyowrds = ['discover', 'sprays', 'samples', 'sunglasses', 'watch']

    for product in soup.find_all("div", class_="grid-item"):
        title = product.find("div", class_="grid-title").text.strip()
        link = product.find("a", class_="grid-item-link")["href"]
        image_url = product.find("div", class_="grid-image-wrapper").find("img")["data-src"]
        price_text = product.find("div", class_="product-price").text.strip()
        full_link = base_url + link

        sale_price_search = re.search(r'Sale Price:\$([\d\.]+)', price_text)
        original_price_search = re.search(r'Original Price:\$([\d\.]+)', price_text)
        from_price_search = re.search(r'from\s*\$([\d\.]+)', price_text)
        
        category = 'Fragrance Bottle'
        for keyword in other_keyowrds:
            if keyword in title.lower():
                category = 'Other'
                break

        if sale_price_search:
            sale_price = sale_price_search.group(1)
            original_price = original_price_search.group(1) if original_price_search else None
            products.append({
                'title': title,
                'image_url': image_url,
                'link' : full_link,
                'sale_price': sale_price,
                'original_price': original_price,
                'category' : category,
                'is_on_sale' : bool(sale_price_search)
            })

        elif from_price_search:
            from_price = from_price_search.group(1)
            products.append({
                'title': title,
                'image_url': image_url,
                'link' : full_link,
                'from_price': from_price,
                'category ' : category,
                'is_on_sale' : bool(sale_price_search)
            })
    return products
