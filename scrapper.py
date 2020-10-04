from bs4 import BeautifulSoup
import requests

BASE_URL = "https://www.digikala.com/main/home-and-kitchen/"

def make_text_file(input_array, destination_file):
    file_name = destination_file + ".txt"
    output_file = open(file_name, 'w', encoding='utf-8')
    for member in input_array:
        output_file.write(member + "\n")
    

def scrape(base_url, destination_file="cats"):
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    categories = soup.find_all(attrs = {'class' : 'c-catalog__plain-list-link'})
    categories_list = []
    for category in categories:
        categories_list.append(category.text)

    make_text_file(categories_list, destination_file)

if __name__ == '__main__':
    scrape(BASE_URL)