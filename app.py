import json
from flask import Flask, jsonify
import click

app = Flask(__name__)

# Opening the JSON file
f = open('cv_data.json')

# returns JSON object as a dictionary
cv_data = json.load(f)


@app.route('/personal')
def personal():
    return jsonify(cv_data['personal'])


@app.route('/experience')
def experience():
    return jsonify(cv_data['experience'])


@app.route('/education')
def education():
    return jsonify(cv_data['education'])


@app.cli.command()
def show_cv():
    for key in cv_data:
        print(f"{key.capitalize()}:")
        for item in cv_data[key]:
            print("\t", item)


if __name__ == '__main__':
    app.run()
