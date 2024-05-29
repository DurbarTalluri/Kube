from flask import Flask
import os
APP_PORT = os.environ.get("APPLICATION_PORT",5000)
app = Flask(__name__)

'''print("PID: ", os.getpid())
for key, value in os.environ.items():
    try:
        print(key, "     ", value)
    except:
        pass'''

@app.route("/")
def home():
    return "welcome to flask application"

if __name__ == "__main__":
    app.run(debug=True,port=APP_PORT)