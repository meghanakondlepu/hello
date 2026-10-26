from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "<h1>Home Page</h1>"
@app.route("/menu")
def menu():
    return "<h1>Menu Page</h1>"
@app.route("/contact")
def contact():
    return "<h1>Contact Page</h1>"
if __name__ == "__main__":
    app.run()


