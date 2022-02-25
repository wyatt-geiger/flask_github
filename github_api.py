# TODO make requests to github API

import requests

def get_github_user_info(username):
    response = requests.get(f'https://api.github.com/users/{username}').json()
    print(response)
    return response
