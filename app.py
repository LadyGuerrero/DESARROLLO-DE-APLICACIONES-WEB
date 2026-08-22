from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/herramientas')
def herramientas():
    return render_template('herramientas.html')

@app.route('/impacto')
def impacto():
    return render_template('impacto.html')

@app.route('/recursos')
def recursos():
    return render_template('recursos.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)