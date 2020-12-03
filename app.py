from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import stories_list

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.route("/")
def create_homepage():
    """ returns homepage html with a question form"""
    titles = [story.title for story in stories_list]
    return render_template("story-select.html", story_titles=titles)



@app.route("/questions")
def generate_questions():
    """ Gets user selected story and returns html with that story's prompts"""
    """TO-DO: Just loop through instead of doing comprehension
    or could also create a class method on Story class to find story by title"""
    story = [story for story in stories_list
            if story.title == request.args["story-selection"]]
    prompts = story[0].prompts
    title = story[0].title

    return render_template("questions.html", prompts=prompts, title=title)


@app.route("/story")
def generate_story():
    """ generate a story from form data upon form submission '"""
    answers = request.args
    story = [story for story in stories_list
        if story.title == request.args["title"]]
    story_text = story[0].generate(answers)

    return render_template("story.html", story=story_text)
