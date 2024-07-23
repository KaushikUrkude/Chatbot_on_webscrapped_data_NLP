import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, urlparse, urlunparse
import os

def normalize_url(url):
    parsed_url = urlparse(url)
    normalized_url = urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, '', '', ''))
    return normalized_url

def change_name(url):
    return re.sub(r'[^a-zA-Z0-9_-]', '_', url)

error_website = []

def retrieve_data(url, depth, current_depth=1, visited=set()):
    if current_depth > depth or url in visited:
        return
    
    visited.add(url)

    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to fetch {url}. Status code: {response.status_code}")
            return

        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.content, 'html.parser')
        
        links = set()
        mails = []
        for link in soup.find_all('a'):
            href = link.get('href')
            if href is None:
                continue
            if href.startswith('http'):
                sublink = href
                links.add(normalize_url(sublink))
            elif href.startswith('mailto'):
                mails.append(href)
            elif href.startswith('#'):
                continue
            else:
                sublink = urljoin(url, href)
                links.add(normalize_url(sublink))
                
        with open(links_file_path, 'a', encoding='utf-8') as Lfile:
            for link in links:
                Lfile.write(link + '\n')

        for link in links:
            retrieve_data(link, depth, current_depth + 1, visited)
        
    except Exception as e:
        error_website.append(url)
        with open(error_site, 'a', encoding='utf-8') as Efile:
            Efile.write(url + "\n")
        print(f"Error scraping {url}: {e}")

# Main URL to start crawling
main_url = "https://docs.nvidia.com/cuda/"

output_folder = 'output'
os.makedirs(output_folder, exist_ok=True)

links_file_path = os.path.join(output_folder, f'{change_name(main_url)}_links.txt')
error_site = os.path.join(output_folder, f'{change_name(main_url)}_error.txt')

retrieve_data(main_url, 5, 1)
