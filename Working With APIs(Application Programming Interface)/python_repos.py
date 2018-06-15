import requests

# Make an API call, and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# Store API response in a variable.
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Explore information about the repositories.
repo_dicts = response_dict['items']

print("repositories returned: ",len(repo_dicts))

print("SELECTED INFORMATION ABOUT EACH REPOSITORY:")
#loop through each of repository.
for repo_dict in repo_dicts:
	print("\nNAME:", repo_dict['name'])
	print("OWNER:", repo_dict['owner']['login'])
	print("STARS:", repo_dict['stargazers_count'])
	print("REPOSITORY:", repo_dict['html_url'])
	print("DESCRIPTION:", repo_dict['description'])

#examine the first repository.
repo_dict = repo_dicts[0]

#print all the inforamtion about the first repository in github
print('\nSelected information about first repository:')
print("NAME:", repo_dict['name'])
print("OWNER:", repo_dict['owner']['login'])
print("STAR:", repo_dict['stargazers_count'])
print("REPOSITORY:", repo_dict['html_url'])
print("CREATED:", repo_dict['created_at'])
print("UPDATED:", repo_dict['updated_at'])
print("DESCRIPTION:", repo_dict['description'])
print("\nkeys :", len(repo_dict))



