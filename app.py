from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World! Cameron Jarvandi I am adding my first code change'

@app.route('/about-css')
def about():
    return render_template('about-css.html')
if __name__ == '__main__':
    app.run()

@app.route('/favorite-course')
def fCourse():
    print('Course: ' + request.args.get('course'))
    print('Grade: ' + request.args.get('grade'))
    return render_template('favorite-course.html')

@app.route('/contact')
def Contact():
    return render_template('Contact.html')