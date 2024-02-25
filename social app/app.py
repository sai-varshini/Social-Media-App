from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')
@app.route('/index')
def post():
    return render_template('index.html')
@app.route('/blog')
def blog():
    return render_template('blog.html')

if __name__ == '__main__':
    app.run(debug=True)
