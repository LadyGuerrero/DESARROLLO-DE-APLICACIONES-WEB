from flask import Flask, render_template, redirect, url_for, flash, request
from forms.herramienta_form import HerramientaForm
from forms.contacto_form import ContactoForm
from conexion.conexion import get_connection

app = Flask(__name__)
app.config['SECRET_KEY'] = 'uea2026secretkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/herramientas')
def herramientas_lista():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT h.id_herramienta, h.nombre, h.descripcion, c.nombre, h.disponible
        FROM herramientas h
        JOIN categorias c ON h.id_categoria = c.id_categoria
    ''')
    herramientas = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('herramientas.html', herramientas=herramientas)

@app.route('/herramientas/nueva', methods=['GET', 'POST'])
def nueva_herramienta():
    form = HerramientaForm()
    if form.validate_on_submit():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            'SELECT id_categoria FROM categorias WHERE nombre = %s',
            (form.categoria.data,)
        )
        categoria = cursor.fetchone()
        if categoria:
            cursor.execute(
                'INSERT INTO herramientas (nombre, descripcion, disponible, id_categoria) VALUES (%s, %s, %s, %s)',
                (form.nombre.data, form.descripcion.data, 1, categoria[0])
            )
            conn.commit()
        cursor.close()
        conn.close()
        flash('Herramienta registrada correctamente.', 'success')
        return redirect(url_for('herramientas_lista'))
    return render_template('formulario_herramienta.html', form=form)

@app.route('/herramientas/editar/<int:id>', methods=['GET', 'POST'])
def editar_herramienta(id):
    conn = get_connection()
    cursor = conn.cursor()
    form = HerramientaForm()
    if form.validate_on_submit():
        cursor.execute(
            'SELECT id_categoria FROM categorias WHERE nombre = %s',
            (form.categoria.data,)
        )
        categoria = cursor.fetchone()
        if categoria:
            cursor.execute(
                'UPDATE herramientas SET nombre=%s, descripcion=%s, id_categoria=%s WHERE id_herramienta=%s',
                (form.nombre.data, form.descripcion.data, categoria[0], id)
            )
            conn.commit()
        cursor.close()
        conn.close()
        flash('Herramienta actualizada correctamente.', 'success')
        return redirect(url_for('herramientas_lista'))
    cursor.execute('SELECT h.nombre, h.descripcion, c.nombre FROM herramientas h JOIN categorias c ON h.id_categoria = c.id_categoria WHERE h.id_herramienta = %s', (id,))
    h = cursor.fetchone()
    cursor.close()
    conn.close()
    if h:
        form.nombre.data = h[0]
        form.descripcion.data = h[1]
        form.categoria.data = h[2]
    return render_template('formulario_herramienta.html', form=form)

@app.route('/herramientas/eliminar/<int:id>')
def eliminar_herramienta(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM herramientas WHERE id_herramienta = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    flash('Herramienta eliminada.', 'warning')
    return redirect(url_for('herramientas_lista'))

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