import requests
from bs4 import BeautifulSoup

def scrape_latest_articles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = soup.find_all('h3')  # Assuming articles are in <h3> tags
    for article in articles[:5]:  # Limiting to 5 latest articles
        title = article.text
        link = article.find('a')['href']
        print(f"Title: {title}, URL: {link}")

if __name__ == "__main__":
    scrape_latest_articles('https://edition.cnn.com')
