from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from forms.herramienta_form import HerramientaForm
from forms.contacto_form import ContactoForm
from forms.login_form import LoginForm
from forms.usuario_form import UsuarioForm
from forms.recurso_form import RecursoForm
from conexion.conexion import get_connection
from models import Usuario

app = Flask(__name__)
app.config['SECRET_KEY'] = 'uea2026secretkey'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, usuario, password FROM usuarios WHERE id = %s', (user_id,))
    u = cursor.fetchone()
    cursor.close()
    conn.close()
    if u:
        return Usuario(u[0], u[1], u[2])
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, usuario, password FROM usuarios WHERE usuario = %s', (form.usuario.data,))
        u = cursor.fetchone()
        cursor.close()
        conn.close()
        if u and check_password_hash(u[2], form.password.data):
            login_user(Usuario(u[0], u[1], u[2]))
            return redirect(url_for('dashboard'))
        flash('Usuario o contraseña incorrectos.', 'danger')
    return render_template('login.html', form=form)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    form = UsuarioForm()
    if form.validate_on_submit():
        hashed = generate_password_hash(form.password.data)
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO usuarios (usuario, password) VALUES (%s, %s)',
                      (form.usuario.data, hashed))
        conn.commit()
        cursor.close()
        conn.close()
        flash('Usuario registrado. Inicia sesión.', 'success')
        return redirect(url_for('login'))
    return render_template('registro.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/herramientas')
@login_required
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
@login_required
def nueva_herramienta():
    form = HerramientaForm()
    if form.validate_on_submit():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id_categoria FROM categorias WHERE nombre = %s', (form.categoria.data,))
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
@login_required
def editar_herramienta(id):
    conn = get_connection()
    cursor = conn.cursor()
    form = HerramientaForm()
    if form.validate_on_submit():
        cursor.execute('SELECT id_categoria FROM categorias WHERE nombre = %s', (form.categoria.data,))
        categoria = cursor.fetchone()
        if categoria:
            cursor.execute(
                'UPDATE herramientas SET nombre=%s, descripcion=%s, id_categoria=%s WHERE id_herramienta=%s',
                (form.nombre.data, form.descripcion.data, categoria[0], id)
            )
            conn.commit()
        cursor.close()
        conn.close()
        flash('Herramienta actualizada.', 'success')
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
@login_required
def eliminar_herramienta(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM herramientas WHERE id_herramienta = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    flash('Herramienta eliminada.', 'warning')
    return redirect(url_for('herramientas_lista'))

@app.route('/recursos')
@login_required
def recursos_lista():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT r.id_recurso, r.nombre, r.tipo, r.url, c.nombre, r.gratuito
        FROM recursos r
        JOIN categorias c ON r.id_categoria = c.id_categoria
    ''')
    recursos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('recursos.html', recursos=recursos)

@app.route('/recursos/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo_recurso():
    form = RecursoForm()
    if form.validate_on_submit():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO recursos (nombre, tipo, url, gratuito, id_categoria) VALUES (%s, %s, %s, %s, %s)',
            (form.nombre.data, form.tipo.data, form.url.data, int(form.gratuito.data), int(form.categoria.data))
        )
        conn.commit()
        cursor.close()
        conn.close()
        flash('Recurso registrado.', 'success')
        return redirect(url_for('recursos_lista'))
    return render_template('formulario_recurso.html', form=form)

@app.route('/recursos/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_recurso(id):
    form = RecursoForm()
    conn = get_connection()
    cursor = conn.cursor()
    if form.validate_on_submit():
        cursor.execute(
            'UPDATE recursos SET nombre=%s, tipo=%s, url=%s, gratuito=%s, id_categoria=%s WHERE id_recurso=%s',
            (form.nombre.data, form.tipo.data, form.url.data, int(form.gratuito.data), int(form.categoria.data), id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        flash('Recurso actualizado.', 'success')
        return redirect(url_for('recursos_lista'))
    cursor.execute('SELECT nombre, tipo, url, gratuito, id_categoria FROM recursos WHERE id_recurso = %s', (id,))
    r = cursor.fetchone()
    cursor.close()
    conn.close()
    if r:
        form.nombre.data = r[0]
        form.tipo.data = r[1]
        form.url.data = r[2]
        form.gratuito.data = str(r[3])
        form.categoria.data = str(r[4])
    return render_template('formulario_recurso.html', form=form)

@app.route('/recursos/eliminar/<int:id>')
@login_required
def eliminar_recurso(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM recursos WHERE id_recurso = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    flash('Recurso eliminado.', 'warning')
    return redirect(url_for('recursos_lista'))

@app.route('/impacto')
@login_required
def impacto():
    titulo = "Impacto de la IA en la Educación"
    impactos = [
        {"area": "Aprendizaje", "descripcion": "Personalización del contenido según cada estudiante"},
        {"area": "Investigación", "descripcion": "Aceleración en la búsqueda de información científica"},
        {"area": "Productividad", "descripcion": "Mayor eficiencia en tareas académicas"},
        {"area": "Ética", "descripcion": "Desafíos en integridad académica"}
    ]
    return render_template('impacto.html', titulo=titulo, impactos=impactos)

@app.route('/contacto', methods=['GET', 'POST'])
@login_required
def contacto():
    form = ContactoForm()
    if form.validate_on_submit():
        flash('Mensaje enviado correctamente.', 'success')
        return redirect(url_for('contacto'))
    return render_template('contacto.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)