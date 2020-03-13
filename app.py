from flask import Flask, render_template, request, redirect, url_for
from Mongo import PharmaDBMainDS

app = Flask(__name__)
app.dts = PharmaDBMainDS()
app.dts.set_localhost()
app.my_ip = '192.168.43.27'
app.my_port = 80


@app.route('/')
def root():
    return redirect(url_for('home'))


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/dep')
def dep():
    return render_template('dep.html')


@app.route('/doctor')
def doctor():
    return render_template('doctor.html')


@app.route('/elements')
def elements():
    return render_template('elements.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/single_blog')
def single_blog():
    return render_template('single-blog.html')


if __name__ == '__main__':
    app.run(host=app.my_ip, port=app.my_port)
