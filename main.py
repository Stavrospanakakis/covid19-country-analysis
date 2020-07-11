import pandas as pd 
import matplotlib
import matplotlib.pyplot as plt 

##Read the data
data = pd.read_excel('COVID-19-geographic-disbtribution-worldwide.xlsx')

#Change it to the country of your choice
country = 'Greece' 

##Reverse the data
data = data.reindex(index=data.index[::-1])

##Remove the dates with no cases
data = data[data.cases != 0]

##Remove useless columns
data = data.drop(columns=['day', 'month', 'year', 'geoId', 'countryterritoryCode', 'popData2018'])

## Make the name of the columns more clean
data.rename(columns={"countriesAndTerritories": "Country", 'dateRep': 'Date', 'cases': 'Cases', 'deaths': 'Deaths'}, inplace=True)

##Use only data for specific country
data = data[data['Country'].str.contains(country)]

## Total Death Percentage
total_death_percentage = data.Deaths.sum() / data.Cases.sum() * 100
print('\nTotal Death Percentage: ' + str(total_death_percentage) + '%')

## Total Cases and Deaths
print('Total Cases: ', data.Cases.sum())
print('Total Deaths: ', data.Deaths.sum())

## Calculate Death Percentage for Each Day
percentage = []
for i in data.index : 
    percentage.append(data['Deaths'][i] / data['Cases'][i] * 100)
data['Percentage'] = percentage 

## Print the minimized dataframe
print(data)

## Plot size
matplotlib.rcParams['figure.figsize'] = (10.0, 4.0)

## Plot for Death Percentage
ax = plt.subplot()
ax.plot(data.set_index('Date')['Percentage'])
ax.set(xlabel='Date', ylabel='Percentage', title='Death Percentage')
ax.grid()
plt.show()

## Plot for Cases And Deaths(Greece)
ax = plt.subplot()
ax.set(xlabel='Date', ylabel='People', title='Cases And Deaths')
ax.plot(data.set_index('Date')['Cases'],color='blue', label='Cases')
ax.plot(data.set_index('Date')['Deaths'], color='orange',label='Deaths')
ax.grid()
ax.legend()
plt.show()

