#pygal's country codes are sorted in a module caleed i18n short for internationalization
from pygal.maps.world import COUNTRIES

#sort the keys in alphabetical order.
for country_code in sorted(COUNTRIES.keys()):
	#now print each country code along with its name.
	print(country_code, COUNTRIES[country_code])
