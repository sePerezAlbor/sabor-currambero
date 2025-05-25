from flask import Blueprint, render_template, jsonify, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.forms import LoginForm
from app.models import Usuario, Restaurante
from app import bcrypt
from app.forms import RegisterForm
from app import db

main = Blueprint('main', __name__)

# Página principal
@main.route('/')
def index():
    return render_template('index.html')

# Login
@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))

    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(correo=form.correo.data).first()
        if usuario and usuario.contrasenia == form.contrasenia.data:
            login_user(usuario)
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('main.dashboard'))
        else:
            flash('Correo o contraseña inválidos', 'danger')

    return render_template('login.html', form=form)

# Dashboard protegido
@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', usuario=current_user)

# Logout
@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión.', 'info')
    return redirect(url_for('main.login'))

# API de restaurantes
@main.route('/api/restaurantes')
def api_restaurantes():
    restaurantes = Restaurante.query.filter_by(estado=True).all()
    data = []
    for r in restaurantes:
        data.append({
            "id": r.id_restaurante,
            "nombre": r.nombre,
            "latitud": float(r.latitud),
            "longitud": float(r.longitud),
            "tipo_comida": r.tipo_comida,
            "precio_promedio": r.precio_promedio,
            "calificacion_prom": float(r.calificacion_prom),
            "instagram": r.instagram
        })
    return render_template("api.json", data=data) if request.args.get("view") else jsonify(data)



@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))

    form = RegisterForm()
    if form.validate_on_submit():
        # Nota: sin hash ya que es prototipo
        nuevo_usuario = Usuario(
            primer_nombre=form.primer_nombre.data,
            primer_apellido=form.primer_apellido.data,
            correo=form.correo.data,
            contrasenia=form.contrasenia.data,
            rol="cliente",
            fecha_registro=db.func.current_timestamp()
        )
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('main.login'))
    
    return render_template('register.html', form=form)
