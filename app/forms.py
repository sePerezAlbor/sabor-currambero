from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo

# ----------------------
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
