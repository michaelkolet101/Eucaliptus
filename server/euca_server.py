from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route("/")
def wellcome():
    return "wellcome to are server!"





app.run()