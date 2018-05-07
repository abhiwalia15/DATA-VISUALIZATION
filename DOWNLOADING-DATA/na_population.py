import pygal

wm=pygal.maps.world.World()

wm.title=('POPULATION OF NORTH AMERICA')
wm.add('North America',{'ca': 34126000, 'us': 309349000, 'mx': 113423000})

#save it in a svg format file
wm.render_to_file('na_population.svg')
