from flask import Flask,render_template,request, redirect
from temp import Gogo

app = Flask(__name__)




@app.route("/")
def index():
    return "Welcome to the index page"

@app.route("/hi")
def who():
    return "who are you?"

@app.route("/hi/<username>")
def greet(username):
    return f"Hi there, {username}"

@app.route("/PassCheck/")
def form():
    return render_template('my-form.html')


@app.route('/PassCheck/', methods = ['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return redirect("/PassCheck/" + processed_text, code=302)


@app.route('/PassCheck/<text>/')
def lists(text):
    processed_text = text.upper()
    result = []
    result = Gogo(text)
    print(result)
    return render_template('options.html', result=result)
