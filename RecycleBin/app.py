from flask import Flask, render_template, request, redirect, url_for
from Mongo import PharmaDBMainDS

app = Flask(__name__)
app.dts = PharmaDBMainDS()
app.dts.set_localhost()
app.my_ip = '0.0.0.0'  # '192.168.43.27'
app.my_port = 5000


@app.route('/med_search', methods=['POST', 'GET'])
def med_search():
    html_data = {
        'my_ip': app.my_ip,
        'my_port': app.my_port,
        'message': '',
        'available': False,
        'table_head': [],
        'table_data': []
    }
    if request.method == 'POST':
        query = request.form['cond_name']
        if len(query) > 1:
            result = app.dts.find({'condition': {'$regex': r'(?i)'+query}}, {'_id': 0})
            if result:
                html_data['message'] = '{} Search Results'.format(len(result))
                html_data['available'] = True
                html_data['table_head'] = result[0].keys()
                html_data['table_data'] = result
            else:
                html_data['message'] = 'No Results Found'
        else:
            html_data['message'] = 'Enter more than 2 alphabets'

    elif request.method == 'GET':
        pass
    return render_template('RecycleBin/med_search.html', html_data=html_data)


@app.route('/home')
def home():
    return render_template('RecycleBin/home.html')


@app.route('/')
def root():
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host=app.my_ip, port=app.my_port)
