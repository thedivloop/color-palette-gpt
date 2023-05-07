import openai
from dotenv import dotenv_values
from flask import Flask, render_template, request
import json


config = dotenv_values(".env")
openai.api_key = config["OPEN_API_KEY"]

app = Flask(__name__, template_folder='templates',
            static_url_path='', static_folder='static')


def get_colors(msg):
    prompt = f"""
    You are a color palette generating assistant that responds to text prompts for color palettes

    Desired Format: a JSON array of hexadecimal color codes

    Text: {msg}

    Result:
    """

    result = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        echo=False
    )

    colors = json.loads(result["choices"][0]["text"])
    return colors


@app.route("/palette", methods=["POST"])
def prompt_to_palette():
    query = request.form.get("query")
    colors = get_colors(query)
    return {"colors": colors}


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
