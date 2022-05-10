from bs4 import BeautifulSoup
import requests
import json 

premio_strega_22a = []

candidati = ['randagi', 'nova', 'mordi-e-fuggi-il-romanzo-delle-br', 'e-poi-saremo-salvi', 'spatriati', 'nina-sullargine', 'divorzio-di-velluto', 'il-cannocchiale-del-tenente-dumont', 'storia-aperta', 'quel-maledetto-vronskij', 'niente-di-vero', 'stradario-aggiornato-di-tutti-i-miei-baci']

for candidato in candidati:
    url = f'https://premiostrega.it/PS/libro/{candidato}/'
    #print(url)

    r = requests.get(url)
    page = r.text
    soup = BeautifulSoup(page, 'html.parser')

    #if r.status_code == 200:
        #print('This one is good', url)

    for book in soup.find_all('div', class_='elementor-element elementor-element-310d20ea elementor-widget elementor-widget-theme-post-content'):
        author = book.find('a').text
        
        title = soup.select('strong:nth-of-type(2)')
            #convert 
        titolo = []
        for item in title:
            titolo.append(item.get_text())
        title2 = ''.join(str(x) for x in titolo)

        publisher = soup.select('strong:nth-of-type(3)')
            #convert
        editore = []
        for item in publisher:
            editore.append(item.get_text())
        publisher2 = ''.join(str(x) for x in editore)

        image = book.find('img')['src']

        citazione = book.find('p').text

        #print(title2)

    for book2 in soup.find_all('div', class_='elementor-element elementor-element-62412fe5 elementor-widget elementor-widget-eael-creative-button'):
        ibs = book2.find('a').get('href')

        #print(ibs)

                
        libri = {}

        #libri['title'] = title2
        libri['author'] = author
        # libri['publisher'] = publisher2
        # libri['cover image'] = image
        # libri['presentation quote'] = citazione
        # libri['vendor link'] = ibs


        premio_strega_22a.append(libri)

    with open('ps_authors_2022.json', 'w', encoding='utf-8') as outfile:
        json.dump(premio_strega_22a, outfile,ensure_ascii=False,indent=2)