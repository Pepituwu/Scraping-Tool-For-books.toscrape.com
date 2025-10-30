import func
import requests
import scrapy 
import pandas as pd
import os
import argparse
import time

base_url = 'https://books.toscrape.com/'
selector = scrapy.Selector(text=requests.get(base_url).text)

def parse_arguments():
    parser = argparse.ArgumentParser(description='Scraper pour books.toscrape.com')
    parser.add_argument('--categories', help='Liste des catégories à scraper (séparées par des virgules)', type=str)

    parser.add_argument('--max-pages', help='Nombre maximum de pages à scraper par catégorie', type=int, default=None)

    parser.add_argument('--delay', help='Délai entre les requêtes (en secondes)', type=float, default=0)

    parser.add_argument('--outdir', help='Dossier de sortie', default='outputs')

    return parser.parse_args()
def main():
    args = parse_arguments()
    # Gestion des catégories
    all_categories = func.get_li()
    if args.categories:
        categories = args.categories.split(',')
        # Vérifier que les catégories existent
        for cat in categories:
            if cat not in all_categories:
                print(f"Attention: la catégorie '{cat}' n'existe pas")
                return
    else:
        categories = all_categories

    # Pour chaque catégorie
    for category in categories:
        print(f"Traitement de la catégorie {category}")
        
        # Créer le dossier de sortie
        output_path = os.path.join(args.outdir, category)
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        
        books = func.get_all_books(category, max_pages=args.max_pages)
        func.download_images(books, category)
        csv_path = os.path.join(output_path, 'books.csv')
        func.export_csv(books, csv_path)
        
        if args.delay:
            time.sleep(args.delay)
            time.sleep(args.delay)



if __name__ == '__main__':
    main()


