from flask import Flask, render_template, request  # NOT the same as requests 
from github_api import get_github_user

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/get_user')
def get_user_info():
    print('Form data is', request.args)  # just for debugging 
    username = request.args.get('username')
    if username:
        user_info, error = get_github_user(username)
        if error: 
            return render_template('error.html', error=error)
        else:
            return render_template('github.html', user_info=user_info)
    else:
        return render_template('error.html', error='Enter a username')


if __name__ == '__main__':
    app.run()