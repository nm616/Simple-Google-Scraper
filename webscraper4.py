from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Query to obtain links
query = input("Enter your Google Search Term: ")
n_pages = int(input("Number of pages to return results for?: "))

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(ChromeDriverManager().install())

links = []  # Initiate empty list to capture final results


# Specify number of pages on google search, each page contains 10 #links

def search(query):
    for page in range(1, n_pages):
        url = "http://www.google.com/search?q=" + query + "&start=" + str((page - 1) * 10)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # soup = BeautifulSoup(r.text, 'html.parser')

        search = soup.find_all('div', class_="yuRUbf")
        for link in search:
            links.append(link.a.get('href'))


def results():
    file_name = ''.join(letter for letter in query if letter.isalnum())
    with open(file_name + ".txt", "a") as file:
        for item in links:
            file.write(item + "\n")


search(query)
results()
