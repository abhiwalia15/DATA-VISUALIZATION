import json
import pygal
from countries_code import get_country_code

#import the data into a list
filename = 'population_data.json'
with open(filename) as f:
	pop_data = json.load(f)
	#print the 2010 population for each country

#biuld a dictionary of population data
cc_populations={}

for pop_dict in pop_data:
	if pop_dict['Year']=='2010':
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		
		code=get_country_code(country_name)
		if code:
			cc_populations[code] = population
		
wm=pygal.maps.world.World()
wm.title='WORLD POPULATION IN 2010, BY COUNTRY'
wm.add('2010', cc_populations)		
wm.render_to_file('world_population_map.svg')
