from flask import Flask, render_template, request
import openai
from dotenv import dotenv_values
import json

config = dotenv_values('.env')
openai.api_key = config["OPENAI.API_KEY"]


#create templates folder 
app = Flask(__name__, 
            template_folder='templates', 
            static_url_path='', 
            static_folder='static',
            )

def get_colors(msg):
    prompt = f"""
    You are a color palette generating assistant that responds to text prompts for color palettes.
    You should generate colors palettes that fit the theme, mood, or instructions in the prompt.
    The palettes should be between 2 and 8 colors.

    Q:Convert the following verbal description of a color palette into a list of colors: The Mediterranean sea
    A: ["#006699", "#66CCCC", "#F0E68C", "#008000", "#F08080"]


    Q:Convert the following verbal description of a color palette into a list of colors: sage, nature, earth
    A: ["#EDF1D6", "#9DC08B", "#609966", "#40513B"]

    Desired Format: a JSON array of hexadecimal color code

    Q:Convert the following verbal description of a color palette into a list of colors: {msg}
    A:
    """
    response = openai.Completion.create(
        prompt = prompt, 
        model = "text-davinci-003", 
        max_tokens = 200
    )
    colors = json.loads(response["choices"][0]["text"])
    return colors

@app.route("/palette", methods=["POST"])
def prompt_to_palette():
    # to test if the post is working using postman 
    query = request.form.get("query")
    colors =  get_colors(query)
    # in order to have a javascritp object  we return like this : {"colors" : colors}
    return {"colors" : colors }

    # OPEN AI COMPLETION CALL

    # RETURN LIST OF COLORS 

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)