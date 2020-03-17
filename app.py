from flask import Flask, render_template, request, redirect, url_for
from Mongo import PharmaDBMainDS
import json

app = Flask(__name__)
app.dts = PharmaDBMainDS()
# app.dts.set_localhost()
app.my_ip = '192.168.43.27'
app.my_port = 80


@app.route('/')
def root():
    return redirect(url_for('home'))


@app.route('/home', methods=['POST', 'GET'])
def home():
    html_data = {
        'my_ip': app.my_ip,
        'my_port': app.my_port,
        'result': False,
        'message': 'Data is here',
        'pre_set': {
            'd_list': json.dumps(["Rahul", "Justin", "Ankit", "Aakash", "Tarun", "Anurag", "Shankar",
                                  "Akshay", "Aryan", "Sushant", "Deepika", "Ankita"])
        },
        'current_query': {
            'p_name': 'none',
            'no_of_dis': 1,
            'd_list': [],
            'gender': 'none',
            'age': '1'
        },
        'query_result': {
        }
    }
    if request.method == 'POST':
        html_data['current_query']['p_name'] = request.form['p_name']
        html_data['current_query']['age'] = request.form['age']
        html_data['current_query']['gender'] = request.form['gender']
        html_data['current_query']['no_of_dis'] = request.form['no_of_dis']
        for i in range(int(request.form['no_of_dis'])):
            html_data['current_query']['d_list'].append(request.form['dis_{}'.format(i+1)])
        html_data['result'] = True

        html_data['message'] = 'Data Retrieved'
    return render_template('index.html', html_data=html_data)


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
