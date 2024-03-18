import main_helpers

from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    res="" if request.args.get('result') is None else request.args.get('result')
    hex="" if request.args.get('hex') is None else request.args.get('hex')
    return render_template('index.html', result=res, hex=hex)

@app.route("/submit", methods=['POST'])
def calc():
    if request.method == 'POST':
        bmantissa = request.form['bmantissa']
        exp = request.form['exp']

        sBinary = main_helpers.inputDecimalBase10(bmantissa, exp)
        sHex = main_helpers.binaryToHex(sBinary)
        return redirect(url_for('index', result=sBinary, hex=sHex))

if __name__ == '__main__':
    # need to handle negative (check if '-' at first pos)
    # bawal floating points ata for exponent?
    app.run(port=5000, debug=True)
    

"""
def entry_page():
    if request.method == 'POST':
        date = request.form['date']
        title = request.form['blog_title']
        post = request.form['blog_main']
        post_entry = models.BlogPost(date = date, title = title, post = post)
        db.session.add(post_entry)
        db.session.commit()
        return redirect(url_for('database'))
    else:
        return render_template('entry.html')

@app.route('/database')        
def database():
    query = []
    for i in session.query(models.BlogPost):
        query.append((i.title, i.post, i.date))
    return render_template('database.html', query = query)
"""