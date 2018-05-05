from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
	'''return pygal's 2 digit code for the given country'''
	for code, name in COUNTRIES.items():
		if name==country_name:
			return code
			
		#if country name wasn't found, return none.
		return None
