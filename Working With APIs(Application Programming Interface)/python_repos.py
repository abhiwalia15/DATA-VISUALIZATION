import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call, and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# Store API response in a variable.
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Explore information about the repositories.
repo_dicts = response_dict['items']

#create 2 empty lists for storing names and no. of stars.
names, stars = [], []
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	stars.append(repo_dict['stargazers_count'])
	
#make visualization
my_style = LS('#333366', base_style = LCS)
#make a bar plot using bar method
chart = pygal.Bar(style = my_style, x_label_rotation = 45, show_legend = False)
chart.title = 'MOST -STARRED PYTHON PROJECTS ON GITHUB'
chart.x_label = names
chart.add(' ', stars)
chart.render_to_file('python_repos.svg')
 
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



