from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>App 2 Placeholder</h1><p>Welcome to App 2!</p>"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
  
