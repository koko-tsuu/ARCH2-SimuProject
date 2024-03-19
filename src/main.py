import main_helpers

from flask import Flask, request, render_template, redirect, url_for, send_file
app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    with open("static/uploads/out.txt", "w") as f:
        f.write("")
        
    res='_ _____ __________' if request.args.get('result') is None else request.args.get('result')
    hex='____' if request.args.get('bHex') is None else request.args.get('bHex')
    man = '_' if request.args.get('pMan') is None else request.args.get('pMan')
    exp='_' if request.args.get('pExp') is None else request.args.get('pExp')
    chk='10' if request.args.get('pChk') is None else request.args.get('pChk')

    return render_template('index.html', result=res, bHex=hex, pMan=man, pExp=exp, pChk=chk)

@app.route("/submit", methods=['POST'])
def calc():
    if request.method == 'POST':
        bMantissa = request.form['inmantissa']
        bExp = request.form['exp']
        
        try:
            if request.form['based'] == 'on':
                bChk = 10
        except:
            bChk = 2
            pass

        if bChk == 10:
            sBinary = main_helpers.inputDecimalBase10(bMantissa, bExp)
        else:
            sBinary = main_helpers.inputBinaryMantissaBase2(bMantissa, bExp)

        sHex = main_helpers.binaryToHex(sBinary)
        #hold = [sBinary, sHex, bMantissa, bExp, bBased]

        with open('./static/uploads/out.txt', 'w') as f:
            f.write(f'Input: {bMantissa} x {bChk}^{bExp}\n\n')
            f.write(f'Hex: 0x{sHex}\n')
            f.write(f'Bin: {sBinary}\n')

        return redirect(url_for('index', result=sBinary, bHex=sHex, pMan=bMantissa, pExp=bExp, pChk=bChk), code=307)

@app.route("/save", methods=['GET'])
def save():
    return send_file('static/uploads/out.txt', as_attachment=True)
        

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