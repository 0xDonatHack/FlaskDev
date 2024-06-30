from flask import Flask , render_template , url_for

app = Flask(__name__ , static_folder='static')

@app.route("/")
def rhome():
    return render_template('index.html')

@app.route("/index.html")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run('0.0.0.0' , debug=True)
