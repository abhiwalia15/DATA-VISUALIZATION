import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style = LCS)
chart = pygal.Bar(style = my_style, x_label_rotation = 45, show_legend = False)

chart.title = 'PYTHON-PROJECTS'
chart.x_labels = ['awesome-python', 'public-apis', 'youtube-dl']

plot_dicts = [
	{'value':51431, 'label':'DESCRIPTION OF AWESOME-PYTHON'},
	{'value':37959, 'label':'DESCRIPTION OF PUBLIC-APIS'},
	{'value':37789, 'label':'DESCRIPTION OF YOUTUBE-DL'},
	]
		
chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')
