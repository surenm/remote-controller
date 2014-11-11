from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import requests
app = Flask(__name__)

def send_request_to_server(direction):
  print "sending direction to server: " + direction
  requests.get("http://10.0.7.167/" + direction)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/execute", methods=['POST'])
def execute():
  direction = request.form["direction"]
  if direction == "up":
    send_request_to_server("start")
    send_request_to_server("forward")
  elif direction == "down":
    send_request_to_server("start")
    send_request_to_server("backward")
  else:
    send_request_to_server(direction)


  return "OK"

if __name__ == "__main__":
  app.run()