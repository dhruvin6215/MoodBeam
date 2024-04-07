import requests
import json


CLIENT_ID = "oEAmwUXePmj8mbP5pL9d5g"
SECRET_KEY = "R6SKfSsWoB20q0GsRkww15B-01Xvpw"
NUM_POSTS = 3

auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

data = {
    'grant_type': 'password',
    'username': 'k_areem',
    'password': 'ilovekittens'
}

headers = {'User-Agent': 'windows:sf_script:v0.0.1 (by /u/k_areem)'}

response = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)

TOKEN = response.json()['access_token']

# update headers
headers = {'User-Agent': 'windows:sf_script:v0.0.1 (by /u/k_areem)', 'Authorization': f'bearer {TOKEN}'}

sf_response = requests.get('https://oauth.reddit.com/r/sanfrancisco/new', headers=headers)
sf_new_posts = [] # each post is a [title, content]
for post in sf_response.json()['data']['children'][:NUM_POSTS]:
    sf_new_posts.append( [post['data']['title'], post['data']['selftext']] )

sfsu_response = requests.get('https://oauth.reddit.com/r/sfsu/new', headers=headers)
sfsu_new_posts = [] # each post is a [title, content]
for post in sfsu_response.json()['data']['children'][:NUM_POSTS]:
    sfsu_new_posts.append( [post['data']['title'], post['data']['selftext']] )


FIREWORKS_SECRET_KEY = "QKx6caXQKUAZzm4MC21HtsDKCt4uQ7UisEGYUc767Hm09u6q"
url = "https://api.fireworks.ai/inference/v1/chat/completions"
headers = {
  "Accept": "application/json",
  "Content-Type": "application/json",
  "Authorization": f"Bearer {FIREWORKS_SECRET_KEY}"
}

sf_total_score = 0
for post in sf_new_posts:
    text = f"Title: {post[0]}\nContent: {post[1]}"
    payload = {
    "model": "accounts/fireworks/models/mixtral-8x7b-instruct",
    "max_tokens": 100,
    "top_p": 1,
    "top_k": 40,
    "presence_penalty": 0,
    "frequency_penalty": 0,
    "temperature": 0.6,
    "messages": [
        {
        "role": "user",
        "content": f'''Please output a number as the output on a scale from 1 to 5. The scale from 1 to 5 works like this: 1 is exceedingly negative, 
        2 is moderately negative, 3 is neutral, 4 is slightly positive, 5 is positive. Output that number and nothing else. Again, to emphasize this, 
        please output one number and nothing else. Do NOT include an explanation of why you chose that rating. Your output should be one character in 
        the list [1,2,3,4,5]. Your input is the following text: {text}'''
        }
    ]
    }
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    score = int(response.json()['choices'][0]['message']['content'][0])
    sf_total_score += score

sf_average = sf_total_score/NUM_POSTS
print(f'sf_average: {sf_average}')

sfsu_total_score = 0
for post in sfsu_new_posts:
    text = f"Title: {post[0]}\nContent: {post[1]}"
    payload = {
    "model": "accounts/fireworks/models/mixtral-8x7b-instruct",
    "max_tokens": 100,
    "top_p": 1,
    "top_k": 40,
    "presence_penalty": 0,
    "frequency_penalty": 0,
    "temperature": 0.6,
    "messages": [
        {
        "role": "user",
        "content": f'''Please output a number as the output on a scale from 1 to 5. The scale from 1 to 5 works like this: 1 is exceedingly negative, 
        2 is moderately negative, 3 is neutral, 4 is slightly positive, 5 is positive. Output that number and nothing else. Again, to emphasize this, 
        please output one number and nothing else. Do NOT include an explanation of why you chose that rating. Your output should be one character in 
        the list [1,2,3,4,5]. Your input is the following text: {text}'''
        }
    ]
    }
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    score = int(response.json()['choices'][0]['message']['content'][0])
    sfsu_total_score += score

sfsu_average = sfsu_total_score/NUM_POSTS
print(f'sfsu_average: {sfsu_average}')