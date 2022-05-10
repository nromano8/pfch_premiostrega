import pandas as pd

books = {'novel': ['Randagi', 'Nova', 'Mordi e fuggi. Il romanzo delle BR', 'E poi saremo salvi', 'Spatriati', 'Nina sull’argine', 'Divorzio di velluto', 'Il cannocchiale del tenente Dumont', 'Storia aperta','Quel maledetto Vronskij','Niente di vero','Stradario aggiornato di tutti i miei baci'],
        'locations':['Pisa, Madrid', 'Lucca', 'Milano', 'Milano', 'Londra, Milano, Berlino', 'Spina (Pinaura Padana), Sicilia', 'Praga, Bratislava, Verona, Bologna, Londra, Washington', 'Egitto, Marengo, Liguria', 'Etiopia, fronte greco-albanese','Milano', 'Italia', 'Roma']}

df = pd.DataFrame(books)

df.index += 1

pd.set_option('max_colwidth', 100)

#print(df)

df.to_csv('ps_settings_2022.csv', encoding='utf-8')