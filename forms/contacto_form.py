from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class ContactoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(min=3)])
    correo = StringField('Correo', validators=[DataRequired(), Email()])
    asunto = StringField('Asunto', validators=[DataRequired(), Length(min=3)])
    mensaje = TextAreaField('Mensaje', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Enviar')