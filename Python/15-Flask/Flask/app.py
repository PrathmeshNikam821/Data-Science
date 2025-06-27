from flask import Flask


#WSGI application 

app = Flask(__name__)


@app.route("/")
def welcome():
  return "Welcome to this Flask course . My name is pratham"

if __name__ == "__main__":
  app.run(debug=True)