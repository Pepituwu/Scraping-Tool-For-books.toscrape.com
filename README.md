# Scraping-Tool-For-books.toscrape.com
A simple scraping tool for books.toscrape.com. Made with demdem!

Pepituwu -> Oscar
Demdem45 -> Adam M

# Avant d'executer
Il faut créer un dossier ```outputs``` au même endroit que les 2 fichiers python.
Dans la console, executez la commande ```pip install requirement.txt```

# Liste des catégories
Nos catégories gardent le nom en dur trouvé dans le html. Soit :

```['books_1', 'travel_2', 'mystery_3', 'historical-fiction_4', 'sequential-art_5', 'classics_6', 'philosophy_7', 'romance_8', 'womens-fiction_9', 'fiction_10', 'childrens_11', 'religion_12', 'nonfiction_13', 'music_14', 'default_15', 'science-fiction_16', 'sports-and-games_17', 'add-a-comment_18', 'fantasy_19', 'new-adult_20', 'young-adult_21', 'science_22', 'poetry_23', 'paranormal_24', 'art_25', 'psychology_26', 'autobiography_27', 'parenting_28', 'adult-fiction_29', 'humor_30', 'horror_31', 'history_32', 'food-and-drink_33', 'christian-fiction_34', 'business_35', 'biography_36', 'thriller_37', 'contemporary_38', 'spirituality_39', 'academic_40', 'self-help_41', 'historical_42', 'christian_43', 'suspense_44', 'short-stories_45', 'novels_46', 'health_47', 'politics_48', 'cultural_49', 'erotica_50', 'crime_51']```

# Flags

```-h, --help              Affiche le message d'aide

--categories CATEGORIES
                        Liste des catégories à scraper (séparées par des virgules)

--max-pages MAX_PAGES
                        Nombre maximum de pages à scraper par catégorie

--delay DELAY           Délai entre les requêtes (en secondes)

--outdir OUTDIR         Dossier de sortie```