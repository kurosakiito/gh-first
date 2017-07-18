import requests

url = 'https://raw.githubusercontent.com/opendatajson/football.json/master/2012-13/en.1.json'

json_data = requests.get(url).json()
#print(json_data)

for each in json_data['rounds']:
	print (each['name'])
	print (each['matches'][0]['date'])
	print (each['matches']['team1']['name'])	

json_league = json_data['name']
json_round = json_data['rounds'][0]['name']
json_date = json_data ['rounds'][0]['matches'][0]['date']
team = json_data ['rounds'][0]['matches'][0]['team1']['name'] + ' vs ' + json_data ['rounds'][0]['matches'][0]['team2']['name']
score = str(json_data ['rounds'][0]['matches'][0]['score1']) + ' - ' + str(json_data ['rounds'][0]['matches'][0]['score2'])

#print (json_league)
#print (json_round) 
#print (json_date)
#print (team)
#print (score)
