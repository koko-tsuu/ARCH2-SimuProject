import main_helpers

from flask import Flask, request, render_template, redirect, url_for, send_file
app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    res='_ _____ __________' if request.args.get('result') is None else request.args.get('result')
    hex='____' if request.args.get('bHex') is None else request.args.get('bHex')
    man = '_' if request.args.get('pMan') is None else request.args.get('pMan')
    exp='_' if request.args.get('pExp') is None else request.args.get('pExp')
    chk='10' if request.args.get('pChk') is None else request.args.get('pChk')
    msg = '' if request.args.get('pMsg') is None else request.args.get('pMsg')

    return render_template('index.html', result=res, bHex=hex, pMan=man, pExp=exp, pChk=chk, pMsg=msg)

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

        # this portion checks and gives feedback on special cases
        if "0001" < sHex < "03FF":
            msg = "Denormalized Number"
        elif sHex == "0001":
            msg = "Smallest Positive Denormalized Number"
        elif sHex == "8001":
            msg = "Smallest Negative Denormalized Number"
        elif sHex == "03FF":
            msg = "Largest Denormalized Number"
        elif sHex == "0400":
            msg = "Smallest Positive Normalized Number"
        elif sHex == "8400":
            msg = "Smallest Negative Normalized Number"
        elif sHex == "3BFF":
            msg = "Largest Number less than One"
        elif sHex == "3C01":
            msg = "Smallest Number larger than One"
        elif sHex == "7BFF":
            msg = "Largest Normal Number"
        elif sHex == "FBFF":
            msg = "Largest Negative Normal Number"
        elif sHex == "8000":
            msg = "Negative Zero"
        elif sHex == "0000":
            msg = "Positive Zero"
        elif sHex == "7C00":
            msg = "Special Case: Positive Infinity"
        elif sHex == "FC00":
            msg = "Special Case: Negative Infinity"
        elif sHex == "7D00":
            msg = "Special Case: Signalling NaN"
        elif sHex == "7E00":
            msg = "Special Case: Quiet NaN"
        else:
            msg = "Normalized Finite"


        with open('uploads/out.txt', 'w') as f:
            f.write(f'Input: {bMantissa} x {bChk}^{bExp}\n\n')
            f.write(f'Hex: 0x{sHex}\n')
            f.write(f'Bin: {sBinary}\n')
            f.write(f'\n{msg}\n')

        return redirect(url_for('index', result=sBinary, bHex=sHex, pMan=bMantissa, pExp=bExp, pChk=bChk, pMsg=msg), code=307)

@app.route("/save", methods=['GET'])
def save():
    return send_file('../uploads/out.txt', as_attachment=True)
        

if __name__ == '__main__':
    # need to handle negative (check if '-' at first pos)
    # bawal floating points ata for exponent?
    app.run(port=5000, debug=True)
    