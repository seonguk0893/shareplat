from flask import Flask, Response, request, render_template, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')



@app.route('/company', methods=['GET', 'POST'])
def company():
    return render_template('company.html')

@app.route('/business', methods=['GET', 'POST'])
def business():
    return render_template('business.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    # 배포 시에 debug=False, host='0.0.0.0', port=80
    app.run(debug=False, host='0.0.0.0', port=80)
