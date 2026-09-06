from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class HerramientaForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(min=3, max=100)])
    descripcion = StringField('Descripción', validators=[DataRequired(), Length(min=4, max=300)])
    categoria = SelectField('Categoría', choices=[
        ('', '-- Selecciona categoría --'),
        ('Asistente Virtual', 'Asistente Virtual'),
        ('Investigación', 'Investigación'),
        ('Productividad', 'Productividad'),
        ('Diseño', 'Diseño'),
        ('Educación', 'Educación')
    ], validators=[DataRequired()])
    submit = SubmitField('Registrar')