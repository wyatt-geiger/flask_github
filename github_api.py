# TODO make requests to github API

import logging
import requests

def get_github_user(username):

    """ Makes a request to the GitHub API to discover info about a user 
    with the given username.

    Returns a tuple of data, error message

    If the request completes successfully, the return value will be 

    data, None

    If the request fails, the return value will be 

    None, error message
    
    """

    try:
        response = requests.get(f'https://api.github.com/users/{username}')
        if response.status_code == 404:   # unknown user.. or TODO url may be invalid
            return None, f'User {username} not found'
        response.raise_for_status()   
        user_info = extract_user_info(response.json())
        return user_info, None 
    except Exception as e:
        logging.exception(e)  # includes stack trace 
        return None, 'Unknown error'
    

def extract_user_info(json_response):
    """ Return a dictionary of the user's name, login, public repo count,
    avatar URL, and github home page URL. 

    Remove un-used data, organize in a way that makes it easy for the templates to use
    
    Note that the dictionary response from GitHub is basically the same 
    structure but as the data we'll return to the app, but it's common 
    to need to do some processing on the response so we'll do some here. 
    """

    return {
        # use get instead of [] syntax so missing data will be None
        # instead of raising a key error 
        'login': json_response.get('login'),
        'name': json_response.get('name'),
        'avatar_url': json_response.get('avatar_url'),
        'home_page': json_response.get('html_url'),
        'repos': json_response.get('public_repos'),
    }

