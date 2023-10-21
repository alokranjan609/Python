import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://example.com/blog'

# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the article titles (modify this based on the structure of the website)
    article_titles = soup.find_all('h2', class_='article-title')

    # Print the titles
    for title in article_titles:
        print(title.text)
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
