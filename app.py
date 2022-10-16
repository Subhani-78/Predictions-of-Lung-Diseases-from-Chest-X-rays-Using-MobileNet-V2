from crypt import methods
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])

def index() -> None:
    return "Starting a Machine Learning Project"

if __name__ == "__main__":
    app.run(debug=True)