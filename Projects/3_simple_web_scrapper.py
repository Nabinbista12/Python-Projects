import requests
from bs4 import BeautifulSoup


def getData(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print("Error occured:", e)


url = "https://webscraper.io/test-sites/e-commerce/allinone"
html_content = getData(url)

if html_content:
    # print(html_content)
    print("Download successfully")
else:
    print("Download Failed")

soup = BeautifulSoup(html_content, "html.parser")
# print(soup)
# title_element = soup.find("a", class_="title")
# print(title_element)
title_elements = soup.find_all("a", class_="title")

for title_element in title_elements:
  title = title_element.text.strip()
  print(f"Title: {title}")
  
desc_element = soup.find_all("p", class_="description")
for p in desc_element:
    desc = p.text.strip()
    print(desc)