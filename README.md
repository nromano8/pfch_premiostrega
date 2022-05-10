Description of the code/workflow:

The **ps_allscraped_1947-2018_json.py** and **ps_allscraped_2019-2021_json.py** scripts scrape the [Premio Strega website](https://premiostrega.it/PS/elenco-dei-vincitori/)’s pages for all the available information on the books, and produce the respective JSON files. They are divided in two files because the 2019-2021 pages had different tags.

The **ps_all_1947-2018_csv.py** and **ps_all_2019-2021_csv.py** scripts convert the two JSON files (**ps_all_1947-2018.json** and **ps_all_2019-2021.json**) into csv files (**ps_all_1947-2018.csv** and **ps_all_1947-2018.csv**). 

I ended up needing only specific information, so I created sub-datasets following the same steps for the authors, nominees, and titles: 

**ps_authors_1947-2018_json.py** -> **ps_authors_1947-2018.json** -> **ps_authors_1947-2018_csv.py** -> **ps_authors_1947-2018.csv**

**ps_authors_2019-2021_json.py** -> **ps_authors_2019-2021.json** -> **ps_authors_2019-2021_csv.py** -> **ps_authors_2019-2021.csv**

**ps_nominees_1947-2018_json.py** -> **ps_nominees_1947-2018.json** -> **ps_nominees_1947-2018_csv.py** -> **ps_nominees_1947-2018.csv**

**ps_nominees_2019-2021_json.py** -> **ps_nominees_2019-2021.json** -> **ps_nominees_1947-2018_csv.py** -> **ps_nominees_2019-2021.csv**

**ps_titles_1947-2018_json.py** -> **ps_titles_1947-2018.json** -> **ps_titles_1947-2018_csv.py** -> **ps_titles_1947-2018.csv**
-**ps_titles_2019-2021_json_csv.py** -> **ps_titles_2019-2021.json** -> **ps_titles_2019-2021_csv.py** -> **ps_titles_2019-2021.csv**

The **merge_ps_authors.py**, **merge_ps_nominees.py**, and **merge_ps_titles.py** scripts use Pandas to combine each csv series into master files (**master_ps_authors.csv**, **master_ps_nominees.csv**, and **master_ps_titles.csv**). 

I then cleaned the data from these master csv files using OpenRefine. 

For the authors, I was able to successfully reconcile all the names through Wikidata and add birthplaces with coordinates to create **ps_all_authors_birthplaces.csv**. 

For the nominees, I was able to reconcile only some of the names through Wikidata to find the birthplaces. Other locations were added manually based on additional searches, and for the candidates with no information the coordinates for the country of Italy were used instead for the **ps_nominees_birthplaces.csv**. 

For the titles, I tried to find the settings or any/all known locations for the novels. I was able to reconcile only some of the novels’ titles to find the “narrative locations” through Wikidata. Others were added manually based on the information I scraped from the Premio Strega website or other searches to create the **ps_titles_narrativelocations.csv**. 

I followed the same steps to create a separate dataset for the 2022 candidates: 

**ps_all_scraped_2022_json.py** -> **ps_all_scraped_2022.json** -> **ps_allscraped_2022_csv.py** -> **ps_all_scraped_2022.csv**

**ps_authors _2022_json.py** -> **ps_authors_2022.json** -> **ps_authors_2022_csv.py** -> **ps_authors_2022.csv**

I also used OpenRefine to clean the data for the authors to create **ps_authors_2022_places.csv**. I wasn’t able to reconcile all the names and birthplaces, so I also manually added some entries and if I couldn’t find the place of birth I would use the author’s known city of residence.

The [Premio Strega page for the 2022 candidates](https://premiostrega.it/PS/libri/) also included links to the [Libreria IBS](https://www.ibs.it/) (an online bookstore), which contained additional information on the 12 books nominated for this year’s edition so I scraped those pages too: 

**ps_2022_ibs.py** -> **ps_2022_ibs.json**

**ps_settings_2022.py** creates a Pandas DataFrame based on the information I found for the settings of these novels and writes to the **ps_settings_2022.csv**. The file was uploaded to OpenRefine to reconcile the locations and retrieve the coordinates (**ps_coordinates_2022.csv**). 

I made an [ArcGIS StoryMap](https://storymaps.arcgis.com/stories/4c64a15ac28947edbe8c46148e4dda68) based on webmaps I created (using ArcGIS Online) to visualize the birthplaces of the winning authors, previous nominees, and the 2022 candidates, as well as the settings for the winning novels and the 12 nominated for this year. 
