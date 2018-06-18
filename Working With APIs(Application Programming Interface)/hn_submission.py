import requests
from operator import itemgetter

#make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r= requests.get(url)
print('STATUS CODE:', r.status_code)

#process information about each submission.
#make a list in python to store top 30 submission and store it in a empty list
submission_ids = r.json()
submission_dicts = []

#loop through the top 30 submissions.
for submission_id in submission_ids[:30]:
	#make a seprate API call for each submission.
	url = 'https://hacker-news.firebaseio.com/v0/item/'+ str(submission_id)+ '.json'
	submission_r = requests.get(url)
	print(submission_r.status_code)
	response_dict = submission_r.json()
	
	submission_dict = {
				'title':response_dict['title'],
				'link':'https://news.ycombinator.com/item?id='+ str(submission_id),
				'comments':response_dict.get('descendants', 0)
				}
				
	submission_dicts.append(submission_dict)
	submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse = True)
	
for submission_dict in submission_dicts:
	print('\nTITLE:', submission_dict['title'])
	print('DISCUSSION LINK:', submission_dict['link'])
	print('COMMENTS:', submission_dict['comments'])
