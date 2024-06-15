from flask import Flask, render_template


UPLOAD_FOLDER = r'~/Works/crypto_trader/sites'
ALLOWED_EXTENSIONS = {'jpeg', 'jpg', 'png'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RECAPTCHA_USE_SSL']= False
app.config['RECAPTCHA_PUBLIC_KEY'] ='6LeBCfIZAAAAAO39_L4Gd7f6uCM0PfP_N3XjHxkW'
app.config['RECAPTCHA_PRIVATE_KEY'] ='6LeBCfIZAAAAAJTjq0Xz_ndAW9LByCo1nJJKy'
app.config['RECAPTCHA_OPTIONS'] = {'theme':'black'}

@app.route('/')
def index():
    return render_template('index.html', method='utf-8')

app.secret_key = 'some_secret_key'
if __name__ == "__main__":
    app.run(debug=True)