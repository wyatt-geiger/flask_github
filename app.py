from flask import Flask, render_template, request  # NOT the same as requests 
from github_api import get_github_user_info

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/about')
def about():
    author = 'wyatt'
    class_code = 2905
    concepts = ['flask', 'web apps', 'html']
    return render_template('about.html', author=author, class_code=class_code, concepts=concepts)

@app.route('/get_user')
def get_github_user():
    print(request.args)
    username = request.args.get('username')
    
    user_info = get_github_user_info(username)
    # todo make API request
    # todo send data about user in response
    if username:
        return render_template('github.html', username=username, user_info=user_info)
    else:
        return 'error'

if __name__ == '__main__':
    app.run()