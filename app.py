from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "chickenzarecool21837"
debug = DebugToolbarExtension(app)

@app.route('/')
def show_homepage():
    """Brings us to the homepage of the application"""
    prompts = story.prompts
    return render_template('home.html', prompts=prompts)

@app.route('/story')
def show_madlib():
    """Shows the Madlib story we just created from the homepage"""
    madlib = story.generate(request.args)
    return render_template('madlib.html', madlib=madlib)