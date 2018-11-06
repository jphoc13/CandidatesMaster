from FlaskApp import USCandidateCSV
from flask import Flask, render_template, request, redirect, Response
app = Flask(__name__)


@app.route("/")
def output():
    return render_template('index.html')


@app.route('/receiver', methods=['GET'])
def worker():
    result = USCandidateCSV.open_CSV()
    return result


@app.route('/sorter', methods=['POST'])
def sorter():
    data = request.data
    result = USCandidateCSV.sort_CSV(data)
    return result


if __name__ == "__main__":
    app.run()
