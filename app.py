from flask import Flask,render_template

app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def kido():
    return render_template("index.html")

@app.route("/contact")
def kiki():
    return (" my contacts id is")
if(__name__=="__main__"):
    app.run(debug=True)