import requests
from bs4  import BeautifulSoup

#where am getting the data from
url = 'https://www.latlong.net/category/cities-40-15.html'

response =requests.get(url)
html_content =response.text


soup = BeautifulSoup(html_content, 'html.parser')

# Find the table element
table = soup.find('table')

table_data=[]

if table:
    rows = table.find_all('tr')
    for row in rows:
        # Extract data from each row
        row_data = []
        cells = row.find_all(['th', 'td'])
        for cell in cells:
            row_data.append(cell.text.strip())
        table_data.append(row_data)

# Print the scraped data
#for row in table_data:
   # print(row)
    