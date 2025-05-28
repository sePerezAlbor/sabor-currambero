from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms import StringField, TextAreaField, IntegerField, SubmitField,SelectField
from wtforms.validators import DataRequired, EqualTo, Email, Optional

class PerfilForm(FlaskForm):
    primer_nombre = StringField('Primer nombre', validators=[DataRequired()])
    segundo_nombre = StringField('Segundo nombre', validators=[Optional()])
    primer_apellido = StringField('Primer apellido', validators=[DataRequired()])
    segundo_apellido = StringField('Segundo apellido', validators=[Optional()])
    correo = StringField('Correo electrónico', validators=[DataRequired(), Email()])

    tipo_comida_fav = SelectField('Tipo de comida favorita', choices=[], validators=[Optional()])
    restricciones = TextAreaField('Restricciones alimentarias', validators=[DataRequired()])
    presupuesto_promedio = IntegerField('Presupuesto promedio', validators=[Optional()])

    submit = SubmitField('Actualizar perfil culinario')
# Formulario de Login
# ----------------------
class LoginForm(FlaskForm):
    correo = StringField('Correo', validators=[DataRequired()])
    contrasenia = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar sesión')

# ----------------------
# Formulario de Registro
# ----------------------
class RegisterForm(FlaskForm):
    primer_nombre = StringField('Primer nombre', validators=[DataRequired()])
    primer_apellido = StringField('Primer apellido', validators=[DataRequired()])
    correo = StringField('Correo', validators=[DataRequired()])
    contrasenia = PasswordField('Contraseña', validators=[DataRequired()])
    confirmar_contrasenia = PasswordField('Confirmar contraseña', validators=[DataRequired(), EqualTo('contrasenia')])
    submit = SubmitField('Registrarse')
