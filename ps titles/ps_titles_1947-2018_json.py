from tkinter import Y
from bs4 import BeautifulSoup
import requests
import json 

#premio_strega = []

scrittori = []

vincitori = ['1947-ennio-flaiano', '1948-vincenzo-cardarelli', '1949-giovanni-battista-angioletti', '1950-cesare-pavese', '1951-corrado-alvaro', '1952-alberto-moravia', '1953-massimo-bontempelli', '1954-mario-soldati', '1955-giovanni-comisso', '1956-giorgio-bassani', '1957-elsa-morante', '1958-dino-buzzati', '1959-giuseppe-tomasi-di-lampedusa', '1960-carlo-cassola', '1961-raffaele-la-capria', '1962-mario-tobino', '1963-natalia-ginzburg', '1964-giovanni-arpino', '1965-paolo-volponi', '1966-michele-prisco', '1967-anna-maria-ortese', '1968-alberto-bevilacqua', '1969-lalla-romano', '1970-guido-piovene', '1971-raffaello-brignetti', '1972-giuseppe-dessi', '1973-manlio-cancogni', '1974-guglielmo-petroni', '1975-tommaso-landolfi', '1976-fausta-cialente', '1977-fulvio-tomizza', '1978-ferdinando-camon', '1979-primo-levi', '1980-vittorio-gorresio', '1981-umberto-eco', '1982-goffredo-parise', '1983-mario-pomilio', '1984-pietro-citati', '1985-carlo-sgorlon', '1986-maria-bellonci', '1987-stanislao-nievo','1988-gesualdo-bufalino', '1989-giuseppe-pontiggia', '1990-sebastiano-vassalli', '1991-paolo-volponi', '1992-vincenzo-consolo', '1993-domenico-rea', '1994-giorgio-montefoschi', '1995-mariateresa-di-lascia', '1996-alessandro-barbero', '1997-claudio-magris', '1998-enzo-siciliano','1999-dacia-maraini', '2000-ernesto-ferrero', '2001-domenico-starnone', '2002-margaret-mazzantini', '2003-melania-g-mazzucco', '2004-ugo-riccarelli', '2005-maurizio-maggiani', '2006-sandro-veronesi', '2007-niccolo-ammaniti', '2008-paolo-giordano', '2009-tiziano-scarpa', '2010-antonio-pennacchi', '2011-edoardo-nesi', '2012-alessandro-piperno', '2013-walter-siti', '2014-francesco-piccolo', '2015-nicola-lagioia', '2016-edoardo-albinati', '2017-paolo-cognetti', '2018-helena-janeczek']

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
        
        title = book.find('span', class_='book-title').text

        publisher = book.find('span', class_='book-editor').text

        image = book.find('img')['src']

        content = book.select('p:nth-of-type(2), p:nth-of-type(3), p:nth-of-type(4)')
        #convert content into text
        summary = '| \n'.join([item.text for item in content])
        
        nominees = book.find('ul').text.split('\n')
    
        #print('{} | {} | {} | {}{}{}{}{}{}'.format(year_author[0], year_author[1], title, publisher, '\n', image, '\n', f'Book/Author Info: {summary}', '\n', f'Nominees: {nominees}'))
        #print('----')
         
        #libri = {}

        nomi = {}

        nomi['year'] = year_author[0]
        #nomi['author'] = year_author[1]
        nomi['title'] = title
        # libri['publisher'] = publisher
        # libri['cover image'] = image
        # libri['book/author info'] = summary
        # libri['nominees'] = nominees

        #premio_strega.append(libri)

        scrittori.append(nomi)

    # with open('ps_all_1947-2018.json', 'w', encoding='utf-8') as outfile:
    #     json.dump(premio_strega, outfile,ensure_ascii=False,indent=2)

    with open('ps_titles_1947-2018.json', 'w', encoding='utf-8') as outfile2:
        json.dump(scrittori, outfile2,ensure_ascii=False,indent=2)

    