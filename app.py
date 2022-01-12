from flask import Flask,render_template,request, redirect
from temp import Gogo

app = Flask(__name__)



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
    if result == ("No results found"):
        return redirect('/PassCheck/Invalid')
    return render_template('options.html', result=result)

@app.route('/PassCheck/Invalid/', methods = ['POST', 'GET'])
def invalid():
    if request.method == 'GET':
        return render_template('my-form.html', message = "No results found please try again")

    if request.method == 'POST':
        text = request.form['text']
        processed_text = text.upper()
        return redirect("/PassCheck/" + processed_text, code=302)



