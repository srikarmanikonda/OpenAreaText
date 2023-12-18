
from bs4 import BeautifulSoup
import requests


def scrape_area_codes():
  url = 'https://en.wikipedia.org/wiki/List_of_North_American_Numbering_Plan_area_codes'
  response = requests.get(url)

  soup = BeautifulSoup(response.text, 'html.parser')
  tables = soup.find_all('table', {'class': 'wikitable'})
  table = tables[8]

  area_codes_dict = {}

  for row in table.find_all('tr')[1:]:
    cells = row.find_all('td')
    if len(cells) > 1:
      state_or_province = cells[0].text.strip().replace(' (list)', '').lower()
      area_codes = cells[1].text.strip().split(', ')
      area_codes = [int(code) for code in area_codes]

      if state_or_province not in area_codes_dict:
        area_codes_dict[state_or_province] = []

      area_codes_dict[state_or_province].extend(area_codes)
  return area_codes_dict


