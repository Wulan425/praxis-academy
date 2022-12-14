from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'halo sahabattt'

@app.route('/user/<user_name>')
def show_user_profile(user_name):
    return f"User, {user_name}"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"Post {post_id}"

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f"path {subpath}"

if __name__ == "__main__":
    app.run()

