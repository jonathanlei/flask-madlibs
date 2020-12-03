from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.route("/")
def create_homepage():
    """ returns homepage html with a question form"""
    prompts = silly_story.prompts
    return render_template("questions.html", prompts=prompts)


@app.route("/story")
def generate_story():
    """ generate a story from form data upon form submission '"""
    answers = request.args
    story = silly_story.generate(answers)
    return render_template("story.html", story=story)
