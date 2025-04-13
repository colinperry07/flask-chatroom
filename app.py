from flask import Flask, render_template, request, session, redirect
from flask_socketio import SocketIO, send # type: ignore

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*")

messages=[]

@socketio.on('message')
def handle_message(msg):
    send(msg, broadcast=True)

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        session["user"] = request.form["user"]
        return redirect("/chatroom")
    return render_template("index.html")

@app.route("/chatroom", methods=["GET"])
def chatroom():
    return render_template("chatroom.html", user=session["user"])



if __name__ == "__main__":
    socketio.run(app, debug=True)