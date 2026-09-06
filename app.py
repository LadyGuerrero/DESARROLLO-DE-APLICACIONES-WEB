from flask import Flask, render_template, redirect, url_for, flash
from forms.herramienta_form import HerramientaForm
from forms.contacto_form import ContactoForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'uea2026secretkey'

herramientas = [
    {"nombre": "ChatGPT", "descripcion": "Asistente de escritura e investigación", "categoria": "Asistente Virtual", "disponible": True},
    {"nombre": "Consensus", "descripcion": "Búsqueda de papers científicos", "categoria": "Investigación", "disponible": True},
    {"nombre": "Canva IA", "descripcion": "Diseño con inteligencia artificial", "categoria": "Diseño", "disponible": True},
    {"nombre": "Grammarly", "descripcion": "Corrección de textos en inglés", "categoria": "Productividad", "disponible": False},
    {"nombre": "Elicit", "descripcion": "Análisis de literatura científica", "categoria": "Investigación", "disponible": True}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/herramientas')
def herramientas_lista():
    return render_template('herramientas.html', herramientas=herramientas)

@app.route('/herramientas/nueva', methods=['GET', 'POST'])
def nueva_herramienta():
    form = HerramientaForm()
    if form.validate_on_submit():
        herramientas.append({
            "nombre": form.nombre.data,
            "descripcion": form.descripcion.data,
            "categoria": form.categoria.data,
            "disponible": True
        })
        flash('Herramienta registrada correctamente.', 'success')
        return redirect(url_for('herramientas_lista'))
    return render_template('formulario_herramienta.html', form=form)

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

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    form = ContactoForm()
    if form.validate_on_submit():
        flash('Mensaje enviado correctamente.', 'success')
        return redirect(url_for('contacto'))
    return render_template('contacto.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)