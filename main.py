import pdfkit
import requests
from bs4 import BeautifulSoup
from tkinter import filedialog

#asks user for websites and filepath (for saving)
website = input("Enter the websites to be converted (space separated): ")
filepath = filedialog.askdirectory()

urls = website.split()

# gets website title for filename
def get_title(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.title.string.strip() if soup.title else None
    except requests.exceptions.RequestException as e:
         print("Error fetching the webpage:", e)
         return None

for url in urls:
    title = get_title(url)

    # makes the website title appropriate for a filename
    for char in '"?.!/;:': 
        title = title.replace(char, '')

    #saves file
    pdfkit.from_url(url, f'{filepath}/{title}.pdf')
    print(f'Saved {title}.pdf to {filepath}')
