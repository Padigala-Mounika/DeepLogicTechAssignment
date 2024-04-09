from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

def is_valid_url(url):
    """
    Function to check if a URL is valid.
    """
    parsed_url = urlparse(url)
    return parsed_url.scheme in ['http', 'https']

def get_valid_links_from_list_items(list_items):
    """
    Function to get valid links from a list of items.
    """
    valid_links = []
    for item in list_items:
        words = item.split()  # Split the item into words
        for word in words:
            if is_valid_url(word):  # Check if the word is a valid URL
                valid_links.append(word)
    return valid_links
def get_latest_stories():
    # Step 1: Retrieve HTML content
    url = 'https://time.com/'
    response = requests.get(url)
    html_content = response.text

    # Create a BeautifulSoup object 
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extracting text from tags
    heading = soup.find(class_="partial latest-stories").text.strip()

    # Extracting list items
    list_items = [(item.text.strip().split('\n')[0]) for item in soup.find(class_="partial latest-stories").find_all('li')]
        # Find all anchor tags within the latest_stories element
    links = soup.find_all('a')
        
        # Extract href attribute from each anchor tag
    hrefs = [link.get('href') for link in links]
    valid_links = get_valid_links_from_list_items(hrefs)
    result=zip(list_items,valid_links)

    print(dict(result))

get_latest_stories()