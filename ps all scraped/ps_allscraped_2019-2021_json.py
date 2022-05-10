from bs4 import BeautifulSoup
import requests
import json 

premio_strega = []

vincitori = ['2019-antonio-scurati', '2020-sandro-veronesi', 'emanuele-trevi-2-2']

for winner in vincitori:
    url = f'https://premiostrega.it/PS/colio/{winner}/?portfolio_id=vincitori'
    #print(url)

    r = requests.get(url)
    page = r.text
    soup = BeautifulSoup(page, 'html.parser')

    #if r.status_code == 200:
        #print('This one is good', url)

    for book in soup.find_all('div', class_='colio-main'):
        year_author = book.find('h3').get_text(strip=True, separator='\n').splitlines()
        
        title = book.find('div', class_='book-title').text

        publisher = book.find('div', class_='book-editor').text

        image = book.find('img')['src']

        content = book.select('p:nth-of-type(2), p:nth-of-type(3), p:nth-of-type(4)')
        #convert content into text
        summary = '| \n'.join([item.text for item in content])
        
        nominees = book.find('ul').text.split('\n')
    
        #print('{} | {} | {} | {}{}{}{}{}{}'.format(year_author[0], year_author[1], title, publisher, '\n', image, '\n', f'Book/Author Info: {summary}', '\n', f'Nominees: {nominees}'))
        #print('----')
         
        libri = {}

        libri['year'] = year_author[0]
        libri['author'] = year_author[1]
        libri['title'] = title
        libri['publisher'] = publisher
        libri['cover image'] = image
        libri['book/author info'] = summary
        libri['nominees'] = nominees

        premio_strega.append(libri)

    with open('ps_all_2019-2021.json', 'w', encoding='utf-8') as outfile:
        json.dump(premio_strega, outfile,ensure_ascii=False,indent=2)