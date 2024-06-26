from flask import Flask, render_template
from flask_compress import Compress

app = Flask(__name__)
compress = Compress(app)


@app.route("/")
def index():
    return render_template("preston.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
