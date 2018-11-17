from flask import *

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    # return render_template("index.html")
    return "Hello World"


if __name__ == '__main__':
    app.run(debug=True)
