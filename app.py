
from flask import Flask, render_template, request
import pyfiglet

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    ascii_art = ''
    if request.method == 'POST':
        text = request.form.get('text')
        if text:
            ascii_art = pyfiglet.figlet_format(text)
    return render_template('index.html', ascii_art=ascii_art)

if __name__ == '__main__':
    app.run(debug=True)
