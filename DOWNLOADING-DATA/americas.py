import pygal

wm = pygal.maps.world.World()
wm.title = 'NORTH, CENTRAL AND SOUTH AMERICA'

#we use add() method which takes in a label and a list of country codes for the countries we want to focus on
#canada , mexico and united states
wm.add('North America',['ca','mx','us'])
wm.add('Central America',['bz','cr','gt','hn','ni','pa','sv'])
wm.add('South America',['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf','gy', 'pe', 'py', 'sr', 'uy', 've'])

#save the file in a svg format
wm.render_to_file('americas.svg')
