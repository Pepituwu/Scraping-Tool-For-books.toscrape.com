import func
import requests
import scrapy 
import pandas as pd
import os

base_url = 'https://books.toscrape.com/'
selector = scrapy.Selector(text=requests.get(base_url).text)

def main():
    categories = func.get_li()
    for category in categories:
        books = func.get_all_books(category)
        if not os.path.exists(f'outputs/{category}'):
            os.makedirs(f'outputs/{category}')
        func.download_images(books, category)
        func.export_csv(books, f'outputs/{category}/books.csv')



if __name__ == '__main__':
    main()


