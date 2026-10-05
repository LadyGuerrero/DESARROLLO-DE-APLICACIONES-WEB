from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class RecursoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(min=3)])
    tipo = StringField('Tipo', validators=[DataRequired()])
    url = StringField('URL')
    gratuito = SelectField('¿Gratuito?', choices=[('1', 'Sí'), ('0', 'No')])
    categoria = SelectField('Categoría', choices=[
        ('1', 'Asistente Virtual'),
        ('2', 'Investigación'),
        ('3', 'Productividad'),
        ('4', 'Diseño'),
        ('5', 'Educación')
    ], validators=[DataRequired()])
    submit = SubmitField('Guardar')s