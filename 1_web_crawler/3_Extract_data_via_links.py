import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException

def scrape_js_website(url):
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Ensure GUI is off
        chrome_options.add_argument("--disable-gpu")  # Ensure GPU is off

        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        
        driver.get(url)
        
        driver.implicitly_wait(10)
        
        body_text = driver.find_element(By.TAG_NAME, 'body').text
        
        driver.quit()

        return body_text
        
    except WebDriverException as e:
        print(f"Error fetching JavaScript-rendered content from {url}: {e}")
        return None

text_folder = "extracted_text"
error_log_file = "error_links.txt"

os.makedirs(text_folder, exist_ok=True)

with open('unique_links.txt', 'r') as file:
    links = file.readlines()

i = 0
for link in links:
    link = link.strip()
    
    try:
        response = requests.get(link)
        response.encoding = 'utf-8'
        
        if response.status_code != 200:
            print(f"Failed to fetch {link}. Status code: {response.status_code}")
            with open(error_log_file, 'a') as error_file:
                error_file.write(f"Failed to fetch {link}. Status code: {response.status_code}\n")
            continue

        i += 1
        try:
            soup = BeautifulSoup(response.content, 'lxml')
        except Exception as e:
            print(f"lxml HTML parser failed for {link}: {e}")
            # Fall back to html.parser if lxml fails
            try:
                soup = BeautifulSoup(response.content, 'html.parser')
            except Exception as e:
                print(f"html.parser failed for {link}: {e}")
                # If HTML parsing fails, try XML parser
                try:
                    soup = BeautifulSoup(response.content, 'lxml-xml')
                except Exception as e:
                    print(f"lxml XML parser failed for {link}: {e}")
                    continue

        text_file_path = os.path.join(text_folder, f'webtext_{i}.txt')
        print(f"Processing link {i}: {link}")

        extracted_text = soup.get_text()

        if "This site requires Javascript in order to view all its content" in extracted_text:
            print("JavaScript-rendered website")
            extracted_text = scrape_js_website(link)

        if extracted_text is None:
            raise Exception(f"Failed to extract text from {link}")

        with open(text_file_path, "w", encoding='utf-8') as f:
            f.write(extracted_text)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {link}: {e}")
        with open(error_log_file, 'a') as error_file:
            error_file.write(f"Error fetching {link}: {e}\n")
    except Exception as e:
        print(f"Error scraping {link}: {e}")
        with open(error_log_file, 'a') as error_file:
            error_file.write(f"Error scraping {link}: {e}\n")
