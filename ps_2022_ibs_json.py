from bs4 import BeautifulSoup
import requests
import json

premio_strega_22b = []

candidati = ['randagi-libro-marco-amerighi', 'nova-libro-fabio-baca','mordi-fuggi-romanzo-delle-br-libro-alessandro-bertante', 'poi-saremo-salvi-libro-alessandra-carati', 'spatriati-libro-mario-desiati', 'nina-sull-argine-libro-veronica-galletta', 'divorzio-di-velluto-libro-jana-karsaiova', 'cannocchiale-del-tenente-dumont-libro-marino-magliani', 'storia-aperta-libro-davide-orecchio', 'quel-maledetto-vronskij-libro-claudio-piersanti', 'niente-di-vero-libro-veronica-raimo','stradario-aggiornato-di-tutti-miei-libro-daniela-ranieri']

isbn_list = ['9788833937366', '9788845935879', '9788893884693', '9788804737308','9788806247416', '9788833892870', '9788807034787', '9788831312677', '9788830105348', '9788817154925', '9788806251895', '9788868331665']

for i, candidati in enumerate(candidati):
    isbn = isbn_list[i]
    url = f'https://www.ibs.it/{candidati}/e/{isbn}/#cc-anchor-descrizione'
    #print(url)

    r = requests.get(url)
    page = r.text
    soup = BeautifulSoup(page, 'html.parser')

    # if r.status_code == 200:
    #     print('This one is good', url)

    #print(url)

    for book in soup.find_all('div', class_='cc-em-accordion-m cc-open'):
        description = book.select('p')

        descrizione = []
        for item in description:
            descrizione.append(item.get_text())
            #strip=True, separator='\n').splitlines()
        descript = ''.join(str(x) for x in descrizione)

        #print(url, '\n', descript)
        #print('---')

        libri = {}

        libri['url'] = url
        libri['info'] = descript

        premio_strega_22b.append(libri)

    with open('ps_2022_ibs.json', 'w', encoding='utf-8') as outfile:
        json.dump(premio_strega_22b, outfile,ensure_ascii=False,indent=2)