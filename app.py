from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample
from stories import stories, stories_dict

app = Flask(__name__)
app.config['SECRET_KEY'] = "chickenzarecool21837"
debug = DebugToolbarExtension(app)


@app.route('/')
def show_homepage():
    """Brings us to the homepage of the application"""
    story_index = stories_dict.keys()
    story_name = list(stories_dict.values())
    return render_template('home.html', stories=story_name, index=story_index)

@app.route('/word-choice')
def choose_words():
    """Generates form for someone to pick their madlib words"""
    index = int(request.args['story'])
    prompts = stories[index].prompts
    return render_template('word_choice.html', prompts=prompts)

@app.route('/story')
def show_madlib():
    """Shows the Madlib story we just created from the homepage"""
    for story in stories:
        if story.prompts[0] == list(request.args.keys())[0]:
          madlib = story.generate(request.args)
          return render_template('madlib.html', madlib=madlib)