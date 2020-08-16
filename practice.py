from flask import Flask
from flask import render_template

## おまじない
app = Flask(__name__)

@app.route("/")
def top():
    return render_template("practice_top.html")

@app.route("/practice_profile", methods=['POST'])
def profile():
    return render_template



if __name__ == "__main__":
    app.run(debug=True)