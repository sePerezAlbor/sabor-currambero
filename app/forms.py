from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms import StringField, TextAreaField, IntegerField, SubmitField,SelectField, DecimalField
from wtforms.validators import DataRequired, EqualTo, Email, Optional, Length, NumberRange

class RestauranteForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=100)])
    direccion = StringField('Dirección', validators=[Optional(), Length(max=200)])
    tipo_comida = SelectField('Tipo de comida', choices=[])  # choices se llenará en la vista
    precio_promedio = IntegerField('Precio promedio', validators=[DataRequired(), NumberRange(min=0)])
    latitud = DecimalField('Latitud', places=6, validators=[Optional()])
    longitud = DecimalField('Longitud', places=6, validators=[Optional()])
    calificacion_prom = DecimalField('Calificación promedio', places=1, validators=[DataRequired(), NumberRange(min=0, max=5)])
    estado = SelectField('Estado', choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], validators=[DataRequired()])
    instagram = StringField('Instagram', validators=[Optional(), Length(max=50)])
    submit = SubmitField('Agregar Restaurante')

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
from app.models import Usuario  

class RegisterForm(FlaskForm):
    primer_nombre = StringField('Primer nombre', validators=[DataRequired()])
    primer_apellido = StringField('Primer apellido', validators=[DataRequired()])
    correo = StringField('Correo', validators=[DataRequired()])
    contrasenia = PasswordField('Contraseña', validators=[DataRequired()])
    confirmar_contrasenia = PasswordField('Confirmar contraseña', validators=[DataRequired(), EqualTo('contrasenia')])
    submit = SubmitField('Registrarse')


    def validate_correo(self, field):
        if Usuario.query.filter_by(correo=field.data).first():
            raise ValueError('Este correo ya está registrado.')

