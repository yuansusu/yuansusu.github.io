from flask import Flask

app = Flask(__name__)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'Hello, %s' % username


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50009)
