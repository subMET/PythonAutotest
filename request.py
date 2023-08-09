import yaml
import requests
import logging

with open('testdata.yaml') as f:
    data = yaml.safe_load(f)

login = data["login"]
password = data["password"]
api_posts = data["api_posts"]

def get_other_posts_titles(token):
    try:
        data = requests.get(api_posts, params={'owner': 'notMe'}, headers={'X-Auth-Token': token})
    except:
        logging.exception(f"Exception while sending request to server: GET {api_posts}. token: {token}")
        return None
    other_titles = []
    for item in data.json()['data']:
        other_titles.append(item['title'])
    logging.debug("Getting other posts titles.")
    return other_titles

def get_my_posts_descriptions(token):
    try:
        data = requests.get(api_posts, params={'owner': 'Me'}, headers={'X-Auth-Token': token})
    except:
        logging.exception(f"Exception while sending request to server: GET {api_posts}. token: {token}")
        return None
    my_descriptions = []
    for item in data.json()['data']:
        my_descriptions.append(item['description'])
    logging.debug("Getting my posts descriptions.")
    return my_descriptions

def send_post(token, title, description, content):
    try:
        data = requests.post(api_posts, params={'title': title, 'description': description, 'content': content},
                                                headers={'X-Auth-Token': token})
    except:
        logging.exception(f"Exception while sending request to server: POST {api_posts}. token: {token}")
        return False
    logging.debug(f"Post request sent. title: {title}")
    return True