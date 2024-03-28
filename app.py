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
    print('Subject: ' + request.args.get('Subject'))
    print('Course_number: ' + request.args.get('Course Number'))
    return render_template('favorite-course.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')