from flask import Flask, render_template, request
#create templates folder 
app = Flask(__name__, 
            template_folder='templates'
            )


@app.route("/dog")
def dog():
    return "Wof Wof Wof!!!"

@app.route("/")
def index():
    return "Hello There from flask!!!"

if __name__ == "__main__":
    app.run(debug=True)