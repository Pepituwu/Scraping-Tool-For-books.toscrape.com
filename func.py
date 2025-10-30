import requests
import scrapy 
import pandas as pd
#importer les librairie importantes
base_url = 'https://books.toscrape.com/'
selector = scrapy.Selector(text=requests.get(base_url).text)

#Pour une utilisation personnalisé on a mis un ensemble de fonction que l'on peut appeler et personnalisé selon le site 
def get_names(category = "books_1", page: int = 1):
    names = []
    url = f'https://books.toscrape.com/catalogue/category/books/{category}/page-{page}.html'
    if page == 1:
        url = f'https://books.toscrape.com/catalogue/category/books/{category}/index.html'
    if category == "books_1":
        url = f'https://books.toscrape.com/catalogue/category/books_1/page-{page}.html'
    if category == "books_1" and page == 1:
        url = 'https://books.toscrape.com/catalogue/category/books_1/page-1.html'
    response = requests.get(url)

    if response.status_code == 200:
        selector = scrapy.Selector(text=response.text)
        selected = selector.css('article.product_pod h3 a::text').getall()
        names.extend(selected)
    
    return names
#on crée des fonction pour recup tout les elements un peu complexe
def get_prices(category = "books_1", page: int = 1):
    prices = []
    url = f'https://books.toscrape.com/catalogue/category/books/{category}/page-{page}.html'
    if page == 1:
        url = f'https://books.toscrape.com/catalogue/category/books/{category}/index.html'
    if category == "books_1":
        url = f'https://books.toscrape.com/catalogue/category/books_1/page-{page}.html'
    if category == "books_1" and page == 1:
        url = 'https://books.toscrape.com/catalogue/category/books_1/page-1.html'
        
    response = requests.get(url)
    if response.status_code == 200:
        selector = scrapy.Selector(text=response.text)
        selected = selector.css('article.product_pod p.price_color::text').getall()
        prices.extend(selected)
    return prices


def get_availability(category = "books_1", page: int = 1):
    availability = []
    url = f'https://books.toscrape.com/catalogue/category/books/{category}/page-{page}.html'
    if page == 1:
        url = f'https://books.toscrape.com/catalogue/category/books/{category}/index.html'
    if category == "books_1":
        url = f'https://books.toscrape.com/catalogue/category/books_1/page-{page}.html'
    if category == "books_1" and page == 1:
        url = 'https://books.toscrape.com/catalogue/category/books_1/page-1.html'
        
    response = requests.get(url)
    if response.status_code == 200:
        selector = scrapy.Selector(text=response.text)
        selected = selector.css('article.product_pod p.instock.availability::text').getall()
        cleaned = [item.strip() for item in selected if item.strip()]
        availability.extend(cleaned)
    
    return availability

def get_ratings(category = "books_1", page: int = 1):
    ratings = []
    url = f'https://books.toscrape.com/catalogue/category/books/{category}/page-{page}.html'
    if page == 1:
        url = f'https://books.toscrape.com/catalogue/category/books/{category}/index.html'
    if category == "books_1":
        url = f'https://books.toscrape.com/catalogue/category/books_1/page-{page}.html'
    if category == "books_1" and page == 1:
        url = 'https://books.toscrape.com/catalogue/category/books_1/page-1.html'
        
    response = requests.get(url)
    if response.status_code == 200:
        selector = scrapy.Selector(text=response.text)
        selected = selector.css('article.product_pod p.star-rating::attr(class)').re('star-rating (.+)')
        ratings.extend(selected)
    
    return ratings

def get_book_urls(category = "books_1", page: int = 1):
    books_url = []
    url = f'https://books.toscrape.com/catalogue/category/books/{category}/page-{page}.html'
    if page == 1:
        url = f'https://books.toscrape.com/catalogue/category/books/{category}/index.html'
    if category == "books_1":
        url = f'https://books.toscrape.com/catalogue/category/books_1/page-{page}.html'
    if category == "books_1" and page == 1:
        url = 'https://books.toscrape.com/catalogue/category/books_1/page-1.html'
        
    response = requests.get(url)
    if response.status_code == 200:
        selector = scrapy.Selector(text=response.text)
        selected = selector.css('article.product_pod h3 a::attr(href)').getall()
        books_url.extend(selected)
    
    return books_url

def get_image_urls(category = "books_1", page: int = 1):
    images_url = []
    url = f'https://books.toscrape.com/catalogue/category/books/{category}/page-{page}.html'
    if page == 1:
        url = f'https://books.toscrape.com/catalogue/category/books/{category}/index.html'
    if category == "books_1":
        url = f'https://books.toscrape.com/catalogue/category/books_1/page-{page}.html'
    if category == "books_1" and page == 1:
        url = 'https://books.toscrape.com/catalogue/category/books_1/page-1.html'
        
    response = requests.get(url)
    if response.status_code == 200:
        selector = scrapy.Selector(text=response.text)
        selected = selector.css('article.product_pod img::attr(src)').getall()
        images_url.extend(selected)
    
    return images_url
#On fait la mise en place de l'ensemble des element obtenus
def get_books_in_page(category = "books_1", page: int = 1):
    books = []
    books.append(get_names(category, page))
    books.append(get_prices(category, page))
    books.append(get_availability(category, page))
    books.append(get_ratings(category, page))
    books.append(get_book_urls(category, page))
    books.append(get_image_urls(category, page))
    return books

def get_all_books(category='books_1'):
    all_books = []
    names = []
    prices = []
    availabilitys = []
    ratings = []
    book_urls = []
    image_urls = []

    if requests.get(f'https://books.toscrape.com/catalogue/category/books/{category}/page-1.html').status_code == 200:
        page = 1
        while requests.get(f'https://books.toscrape.com/catalogue/category/books/{category}/page-{page}.html').status_code == 200:
            url = f'https://books.toscrape.com/catalogue/category/books/{category}/page-{page}.html'
            names.extend(get_names(category, page))
            prices.extend(get_prices(category, page))
            availabilitys.extend(get_availability(category, page))
            ratings.extend(get_ratings(category, page))
            book_urls.extend(get_book_urls(category, page))
            image_urls.extend(get_image_urls(category, page))
            page += 1
        all_books.append(names)
        all_books.append(prices)
        all_books.append(availabilitys)
        all_books.append(ratings)
        all_books.append(book_urls)
        all_books.append(image_urls)
    
    elif category == 'books_1':
        for page in range(1, 51):
            names.extend(get_names(category, page))
            prices.extend(get_prices(category, page))
            availabilitys.extend(get_availability(category, page))
            ratings.extend(get_ratings(category, page))
            book_urls.extend(get_book_urls(category, page))
            image_urls.extend(get_image_urls(category, page))
        all_books.append(names)
        all_books.append(prices)
        all_books.append(availabilitys)
        all_books.append(ratings)
        all_books.append(book_urls)
        all_books.append(image_urls)
    

    else:
        all_books = get_books_in_page(category)

    return all_books


# on va partir chercher les catégories grace au "li" qui les contient
def get_li():
    categories_list = []
    selected = selector.css('div.side_categories li a::attr(href)').getall()
    for category_url in selected:
        parts = category_url.strip().split('/')
        if len(parts) > 0:
            last_part = parts[-2]
            categories_list.append(last_part)
    return categories_list

# Export vers le format csv avec pandas
def export_csv(data, filename='books.csv'):
    formatted_data = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if len(formatted_data) <= j:
                formatted_data.append([])
            formatted_data[j].append(data[i][j])
    df = pd.DataFrame(formatted_data)
    df.to_csv(filename, index=False, header=False)

#fonction de telechargement d'image pour les mettre dans un dossier prevus pour
def download_image(image_url, save_path):
    base_url = 'https://books.toscrape.com/'
    full_url = base_url + image_url.lstrip('../')
    response = requests.get(full_url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)

def download_images(data, category='books_1'):
    for i in range(len(data[5])):
        image_url = data[5][i]
        print(image_url)
        image_name = data[0][i].replace(' ', '-').replace('/', '_') + '.jpg'
        download_image(image_url, f'outputs/{category}/{image_name}')


