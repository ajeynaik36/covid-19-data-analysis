import requests
import pandas as pd

#DATA COLLECTION
#We use wikipedia to scrap the detials of covid cases
url = "https://en.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory"

#reuesting web page(scraping)
data = requests.get(url)

#converting text od data into dataframe
text = pd.read_html(data.text)

#second row has our cases table for each countries
target_df = text[2]

#DATA CLEANING
#naming column
target_df.columns = ['col0','country', 'total', 'death', 'recoveries','col5']

#removing unwanted rows
target_df = target_df[['country','total','death','recoveries']]

#removing unwanted last rows
last_index = target_df.index[-1]
target_df = target_df.drop([last_index, last_index-1])

#removing 'No data' from all rows with 0
target_df['total'] = target_df['total'].replace('No data','0')
target_df['death'] = target_df['death'].replace('No data','0')
target_df['recoveries'] = target_df['recoveries'].replace('No data','0')

#Clean country name
target_df['country'] = target_df['country'].str.replace('\[.*\]','')

#convert all values to int/numeric
target_df['death'] = pd.to_numeric(target_df['death'])
target_df['total'] = pd.to_numeric(target_df['total'])
target_df['recoveries'] = pd.to_numeric(target_df['recoveries'])