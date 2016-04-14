from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def trangchu():
   return render_template("404.html")

if __name__ == '__main__':
    app.run()
