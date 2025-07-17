
from flask import Flask, render_template, request
import pyfiglet

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    ascii_art = ''
    # Define available fonts (using valid pyfiglet font names)
    fonts = [
        ('standard', 'Standard'),
        ('slant', 'Slant'),
        ('block', 'Block'),
        ('digital', 'Digital'),
        ('banner', 'Banner')
    ]
    
    if request.method == 'POST':
        text = request.form.get('text')
        font = request.form.get('font', 'standard')  # Default to standard if not specified
        if text:
            try:
                ascii_art = pyfiglet.figlet_format(text, font=font)
            except Exception as e:
                # Fallback to standard font if the selected font fails
                ascii_art = pyfiglet.figlet_format(text, font='standard')
                print(f"Font '{font}' not found, using standard font instead. Error: {e}")
    return render_template('index.html', ascii_art=ascii_art, fonts=fonts)

if __name__ == '__main__':
    app.run(debug=True)
