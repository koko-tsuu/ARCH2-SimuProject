import main_helpers
import sub_helpers
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

if __name__ == '__main__':
    # need to handle negative (check if '-' at first pos)
    # bawal floating points ata for exponent?
    sBinary = main_helpers.inputDecimalBase10("2132", "-5")
    print(sBinary)
    app.run(port=5000, debug=True)
    

