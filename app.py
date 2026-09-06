from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/herramientas')
def herramientas():
    herramientas = [
        {"nombre": "ChatGPT", "descripcion": "Asistente de escritura e investigación", "categoria": "Asistente Virtual", "disponible": True},
        {"nombre": "Consensus", "descripcion": "Búsqueda de papers científicos", "categoria": "Investigación", "disponible": True},
        {"nombre": "Canva IA", "descripcion": "Diseño con inteligencia artificial", "categoria": "Diseño", "disponible": True},
        {"nombre": "Grammarly", "descripcion": "Corrección de textos en inglés", "categoria": "Productividad", "disponible": False},
        {"nombre": "Elicit", "descripcion": "Análisis de literatura científica", "categoria": "Investigación", "disponible": True}
    ]
    return render_template('herramientas.html', herramientas=herramientas)

@app.route('/impacto')
def impacto():
    titulo = "Impacto de la IA en la Educación"
    impactos = [
        {"area": "Aprendizaje", "descripcion": "Personalización del contenido según cada estudiante"},
        {"area": "Investigación", "descripcion": "Aceleración en la búsqueda de información científica"},
        {"area": "Productividad", "descripcion": "Mayor eficiencia en tareas académicas"},
        {"area": "Ética", "descripcion": "Desafíos en integridad académica"}
    ]
    return render_template('impacto.html', titulo=titulo, impactos=impactos)

@app.route('/recursos')
def recursos():
    recursos = [
        {"nombre": "Coursera", "tipo": "Curso online", "gratuito": True},
        {"nombre": "edX", "tipo": "Curso online", "gratuito": True},
        {"nombre": "Google Scholar", "tipo": "Buscador académico", "gratuito": True},
        {"nombre": "Udemy", "tipo": "Curso online", "gratuito": False}
    ]
    return render_template('recursos.html', recursos=recursos)

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)