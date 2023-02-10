from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="index")

@app.route("/features")
def features():
    return render_template("features.html", title="features")

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
