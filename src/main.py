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
        match sHex:
            case "0001":
                msg = "Smallest Positive Denormalized Number"
            case "03FF":
                msg = "Largest Denormalized Number"
            case "0400":
                msg = "Smallest Positive Normalized Number"
            case "3BFF":
                msg = "Largest Number less than One"
            case "3C01":
                msg = "Smallest Number larger than One"
            case "7BFF":
                msg = "Largest Normal Number"
            case "8000":
                msg = "Negative Zero"
            case "0000":
                msg = "Positive Zero"
            case "7C00":
                msg = "Special Case: Positive Infinity"
            case "FC00":
                msg = "Special Case: Negative Infinity"
            case "7D00":
                msg = "Special Case: Signalling NaN"
            case "7E00":
                msg = "Special Case: Quiet NaN"
            case _:
                msg = "Normalized Finite"


        with open('uploads/out.txt', 'w') as f:
            f.write(f'Input: {bMantissa} x {bChk}^{bExp}\n\n')
            f.write(f'Hex: 0x{sHex}\n')
            f.write(f'Bin: {sBinary}\n')

        return redirect(url_for('index', result=sBinary, bHex=sHex, pMan=bMantissa, pExp=bExp, pChk=bChk, pMsg=msg), code=307)

@app.route("/save", methods=['GET'])
def save():
    return send_file('../uploads/out.txt', as_attachment=True)
        

if __name__ == '__main__':
    # need to handle negative (check if '-' at first pos)
    # bawal floating points ata for exponent?
    app.run(port=5000, debug=True)
    