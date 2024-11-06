import requests
import pandas as pd
import json
from datetime import datetime

def run_covid19_etl():

	url = "https://covid-193.p.rapidapi.com/statistics"

	headers = {
		"x-rapidapi-key": "5a7eceaf2fmshc5b3709fb9ac51bp1c0f88jsn9819ffedc7fd",
		"x-rapidapi-host": "covid-193.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers)

	covid_stats = response.json()

	covid_cases = []
	for stats in covid_stats['response']:
		continent = stats['continent']
		country = stats['country']
		total_population = stats['population']
		new_cases = stats['cases']['new']
		active_cases = stats['cases']['active']
		critical_cases = stats['cases']['critical']
		recovered_cases = stats['cases']['recovered']
		total_cases = stats['cases']['total']
		cases_per_1M_pop = stats['cases']['1M_pop']
		new_deaths = stats['deaths']['new']
		total_deaths = stats['deaths']['total']
		deaths_per_1M_pop = stats['deaths']['1M_pop']
		total_tests = stats['tests']['total']
		tests_per_1M_pop = stats['tests']['1M_pop']
		stats_date = stats['time']

		complete_stats = {'continent':continent,'country':country,'total_population':total_population,'new_cases':new_cases,
						'active_cases':active_cases,'critical_cases':critical_cases,'recovered_cases':recovered_cases,
						'total_cases':total_cases,'cases_per_1M_pop':cases_per_1M_pop,'new_deaths':new_deaths,
						'total_deaths':total_deaths,'total_tests':total_tests,'tests_per_1M_pop':tests_per_1M_pop,
						'stats_date':stats_date}

		covid_cases.append(complete_stats)

	covid_cases_df = pd.DataFrame.from_dict(covid_cases)

	covid_cases_df.to_csv("Covid_statistics.csv")

	#print(covid_cases_df)