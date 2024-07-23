import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin,urlparse, urlunparse
import os


with open('https___docs_nvidia_com_cuda__links.txt', 'r') as file:
    # Read all lines from the file
    links = file.readlines()

unique_links = set()

for link in links:
    unique_links.add(link)

print(len(unique_links))

with open("unique_links.txt","a",encoding= "utf-8") as f:
    for link in unique_links:
        f.write(link)
