from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>MY APP 2</h1><p>Welcome to App 2!</p><p> check out my other app too at <a href="https://google-custom-search.softwares.calyxtech.net"</a>! Bieee!</p><h2>UPDATE SUCCESSFUL!</p>"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
  
