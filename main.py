from flask import Flask, render_template, request, session
from src.generator import Generator
from src.helper import Helper
from datetime import datetime

app = Flask(__name__)
@app.route('/')
def index():
    filter = session['filter'] if 'filter' in session else {}
    current_year = datetime.now().year
    helper = Helper()
    return render_template('index.html', filter=filter, current_year=current_year, makers=helper.makers, body_types=helper.body_types)

@app.route('/submit', methods=['POST'])
def submit():
    filter = request.form
    session['filter'] = filter
    gen = Generator(filter)
    list = gen.create_all_links()
    return render_template('submit.html', list=list, filter=filter)

@app.route('/website_undefined')
def website_undefined():
    return render_template('website_undefined.html')

if __name__ == "__main__":
    app.secret_key = 'fj89ewfu839unewjkdls'
    app.run(host="0.0.0.0", port=5000, debug=True)
