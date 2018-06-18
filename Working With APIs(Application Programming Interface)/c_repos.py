import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call, and store the response.
url = 'https://api.github.com/search/repositories?q=language:C&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# Store API response in a variable.
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Explore information about the repositories.
repo_dicts = response_dict['items']

#create 2 empty lists for storing names and no. of stars.
names, plot_dicts = [], []
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	description = repo_dict['description']
	if not description:
		description = 'No description provided'
	
	plot_dict = {
			'value': repo_dict['stargazers_count'],
			'label': description,
			'xlink': repo_dict['html_url'],
			}
	plot_dicts.append(plot_dict)
		
#make visualization
my_style = LS('#333366', base_style = LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
#minor axis refers to x-axis
my_config.label_font_size = 14
#major axis refers to y-axis
my_config.major_label_font_size = 18
#we use truncate to shorten the longer project names to 15 characters
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

#make a bar plot using bar method
chart = pygal.Bar(my_config, style = my_style)
chart.title = 'MOST -STARRED C PROJECTS ON GITHUB'
chart.x_label = names
chart.add(' ', plot_dicts)
chart.render_to_file('c.svg')
''' 

print("repositories returned: ",len(repo_dicts))
print("SELECTED INFORMATION ABOUT EACH REPOSITORY:")
#loop through each of repository.
for repo_dict in repo_dicts:
	print("\nNAME:", repo_dict['name'])
	print("OWNER:", repo_dict['owner']['login'])
	print("STARS:", repo_dict['stargazers_count'])
	print("REPOSITORY:", repo_dict['html_url'])
	print("CREATED:", repo_dict['created_at'])
	print("UPDATED:", repo_dict['updated_at'])
	print("DESCRIPTION:", repo_dict['description'])

'''


