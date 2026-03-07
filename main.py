from flask import Flask, request

app = Flask(__name__)
data = ""

@app.route("/post", methods = ["POST"])
def receive_data():
    global data
    data = request.data.decode("utf-8")
    print(f"Data received successfully: {data}")
    return "OK", 200

@app.route("/get", methods = ["GET"])
def show_data():
    return f"<p>{data}</p>"