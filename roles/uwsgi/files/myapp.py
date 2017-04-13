from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@application.route("/test")
def test():
    return "<h1 style='color:blue'>Hey There i am a simply test site/h1>"

if __name__ == "__main__":
    application.run(host='0.0.0.0')