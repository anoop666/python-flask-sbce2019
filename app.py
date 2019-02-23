from flask import Flask

app=Flask(__name__)
@app.route("/")
def index():
    return "hello.... anoop"

@app.route("/home")
def kido():
    return ("my home page")

@app.route("/contact")
def kiki():
    return (" my contacts page")
if(__name__=="__main__"):
    app.run()