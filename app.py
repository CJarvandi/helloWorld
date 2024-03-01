from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World! Cameron Jarvandi I am adding my first code change'

@app.route('/about-css')
def about():
    return render_template('about-css.html')
if __name__ == '__main__':
    app.run()
