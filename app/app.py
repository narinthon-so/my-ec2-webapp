from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def root():
    return render_template("root.html", title="root")

@app.route("/home")
def home():
    return render_template("home.html", title="home")

@app.route("/features")
def features():
    return render_template("features.html", title="features")

@app.route("/pricing")
def pricing():
    return render_template("pricing.html", title="pricing")

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
