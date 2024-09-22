

# from bs4 import BeautifulSoup
# import requests
# import csv
# from dotenv import load_dotenv
# import os

# # Load environment variables from .env file
# load_dotenv()

# # Define the TechCrunch URL and Scraper API key
# site_url = "https://techcrunch.com"
# api_key = os.getenv('SCRAPER_API')

# # Set the payload to send a request via Scraper API
# payload = {'api_key': api_key, 'url': site_url, 'render': 'true'}
# response = requests.get('https://api.scraperapi.com/', params=payload)

# # Parse HTML with BeautifulSoup
# soup = BeautifulSoup(response.content, 'html.parser')

# # Find all articles within the relevant class
# articles = soup.find_all('div', class_="wp-block-tc23-post-picker")

# # Open CSV file to store scraped data
# with open('techcrunch_news.csv', 'a', newline='', encoding='utf-8') as csvfile:
#     csv_writer = csv.writer(csvfile)
#     csv_writer.writerow(['Title', 'Author', 'Publication Date', 'URL', 'Category'])

#     if articles:
#         # Iterate over articles
#         for article in articles:
#             # Extract title
#             title_tag = article.find('h2', class_='wp-block-post-title')
#             title = title_tag.get_text(strip=True) if title_tag else "No title"

#             # Extract URL
#             # Extract URL within the <h2> tag
#             if title_tag:
#                 link_tag = title_tag.find('a')
#                 complete_url = link_tag['href'] if link_tag else "No URL"
#             else:
#                 complete_url = "No URL"

#             # Extract author
#             author_tag = article.find('div', class_='wp-block-tc23-author-card-name')
#             author = author_tag.get_text(strip=True) if author_tag else "No author"

#             # Extract category
#             category_tag = article.find('a', class_='is-taxonomy-category')
#             category = category_tag.get_text(strip=True) if category_tag else "No category"

#             # Extract date (if available)
#             date_tag = article.find('time')
#             publication_date = date_tag['datetime'] if date_tag else "No date"

#             # Write the row to CSV
#             csv_writer.writerow([title, author, publication_date, complete_url, category])
#     else:
#         print("No article information found!")


from bs4 import BeautifulSoup
import requests
import csv
from dotenv import load_dotenv
import os
import time  # Add a delay between requests to avoid overwhelming the server

# Load environment variables from .env file
load_dotenv()

# Define the base TechCrunch URL and Scraper API key
base_url = "https://techcrunch.com/page/"
api_key = os.getenv('SCRAPER_API')

# Open CSV file to store scraped data
with open('techcrunch_news.csv', 'a', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Title', 'Author', 'Publication Date', 'URL', 'Category'])

    # Loop through the first 3 pages (or more)
    for page in range(1, 4):  # Change 4 to 6 if you want to scrape up to 5 pages
        print(f"Scraping page {page}...")

        # Set the page-specific URL
        page_url = f"{base_url}{page}/"
        payload = {'api_key': api_key, 'url': page_url, 'render': 'true'}
        response = requests.get('https://api.scraperapi.com/', params=payload)

        # Parse HTML with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all articles within the relevant class
        articles = soup.find_all('div', class_="wp-block-tc23-post-picker")

        if articles:
            # Iterate over articles
            for article in articles:
                # Extract title
                title_tag = article.find('h2', class_='wp-block-post-title')
                title = title_tag.get_text(strip=True) if title_tag else "No title"

                # Extract URL within the <h2> tag
                if title_tag:
                    link_tag = title_tag.find('a')
                    complete_url = link_tag['href'] if link_tag else "No URL"
                else:
                    complete_url = "No URL"

                # Extract author
                author_tag = article.find('div', class_='wp-block-tc23-author-card-name')
                author = author_tag.get_text(strip=True) if author_tag else "No author"

                # Extract category
                category_tag = article.find('a', class_='is-taxonomy-category')
                category = category_tag.get_text(strip=True) if category_tag else "No category"

                # Extract date (if available)
                date_tag = article.find('time')
                publication_date = date_tag['datetime'] if date_tag else "No date"

                # Write the row to CSV
                csv_writer.writerow([title, author, publication_date, complete_url, category])
        else:
            print(f"No article information found on page {page}.")

        # Add a small delay between page requests 
        time.sleep(2)