from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/calculate')
def calculate():
    try:
        x = request.args.get("x")
        result = 1/(1-float(x))
        return str(result)
    except ZeroDivisionError:
        return "undefined"
    except Exception as exc:
        logging.exception(exc)
        return "invalid input"
