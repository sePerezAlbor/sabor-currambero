from flask import Blueprint, render_template, jsonify, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.forms import LoginForm,RegisterForm, PerfilForm, RestauranteForm
from app.models import Usuario, Restaurante, PerfilGastronomico
from app import bcrypt
from app import db

main = Blueprint('main', __name__)
def perfil_a_dict(perfil):
    return {
        "tipo_comida_fav": perfil.tipo_comida_fav,
        "presupuesto_promedio": perfil.presupuesto_promedio
    }
    
# Página principal
@main.route('/')
def index():
    perfil = None
    tipos_comida = db.session.query(Restaurante.tipo_comida).distinct().all()
    if current_user.is_authenticated:
        perfil = current_user.perfil  # accede a la relación definida en el modelo Usuario
        perfil_dict = perfil_a_dict(perfil) if perfil else None

    return render_template('index.html', usuario=current_user, perfil=perfil_dict, tipos_comida=tipos_comida) 

# Login
@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.perfil'))

    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(correo=form.correo.data).first()
        if usuario and usuario.contrasenia == form.contrasenia.data:
            login_user(usuario)
            return redirect(url_for('main.perfil'))
        else:
            flash('Correo o contraseña inválidos', 'danger')

    return render_template('login.html', form=form)

@main.route('/GestionarRestaurantes', methods=['GET', 'POST'])
@login_required
def gestionar_restaurantes():
    if not current_user.is_authenticated or current_user.rol != 'admin':
        flash('No tienes permiso para acceder a esta página.', 'danger')
        return redirect(url_for('main.index'))

    restaurantes = Restaurante.query.all()
    return render_template('gestionar_restaurantes.html',usuario=current_user, restaurantes=restaurantes)

@main.route('/ActualizarRestaurantes', methods=['POST'])
@login_required
def ActualizarRestaurantes():
    if not current_user.is_authenticated or current_user.rol != 'admin':
        flash('No tienes permiso para realizar esta acción.', 'danger')
        return redirect(url_for('main.index'))

    for r in Restaurante.query.all():
        prefix = f"r_{r.id_restaurante}_"
        r.nombre = request.form.get(prefix + "nombre")
        r.direccion = request.form.get(prefix + "direccion")
        r.tipo_comida = request.form.get(prefix + "tipo_comida")
        r.precio_promedio = request.form.get(prefix + "precio_promedio", type=int)
        r.calificacion_prom = request.form.get(prefix + "calificacion_prom", type=float)
        r.estado = True if request.form.get(prefix + "estado") == 'activo' else False
        r.instagram = request.form.get(prefix + "instagram")

    db.session.commit()
    flash('Restaurantes actualizados correctamente.', 'success')
    return redirect(url_for('main.GestionarRestaurantes'))

@main.route('/AgregarRestaurante', methods=['GET', 'POST'])
@login_required
def AgregarRestaurante():
    if not current_user.is_authenticated or current_user.rol != 'admin':
        flash('No tienes permiso para acceder a esta página.', 'danger')
        return redirect(url_for('main.index'))

    form = RestauranteForm()

    if form.validate_on_submit():
        nuevo_restaurante = Restaurante(
            nombre=form.nombre.data,
            direccion=form.direccion.data,
            tipo_comida=form.tipo_comida.data,
            precio_promedio=form.precio_promedio.data,
            latitud=form.latitud.data,
            longitud=form.longitud.data,
            calificacion_prom=form.calificacion_prom.data,
            estado=True if form.estado.data == 'activo' else False,
            instagram=form.instagram.data
        )
        db.session.add(nuevo_restaurante)
        db.session.commit()
        flash('Restaurante agregado correctamente.', 'success')
        return redirect(url_for('main.GestionarRestaurantes'))

    return render_template('agregar_restaurante.html', form=form, usuario=current_user)

@main.route('/perfil', methods=['GET', 'POST'])
@login_required
def perfil():
    usuario = current_user
    form = PerfilForm(obj=usuario)

    # ✅ Poblar opciones únicas desde la base de datos
    tipos_comida = db.session.query(Restaurante.tipo_comida).distinct().all()
    form.tipo_comida_fav.choices = [(tipo[0], tipo[0]) for tipo in tipos_comida if tipo[0]]

    # Precargar valores si ya existen
    if request.method == 'GET':
        if usuario.perfil:
            form.tipo_comida_fav.data = usuario.perfil.tipo_comida_fav
            form.restricciones.data = usuario.perfil.restricciones
            form.presupuesto_promedio.data = usuario.perfil.presupuesto_promedio

    if form.validate_on_submit():
        usuario.primer_nombre = form.primer_nombre.data
        usuario.segundo_nombre = form.segundo_nombre.data
        usuario.primer_apellido = form.primer_apellido.data
        usuario.segundo_apellido = form.segundo_apellido.data
        usuario.correo = form.correo.data

        if not usuario.perfil:
            usuario.perfil = PerfilGastronomico(id_usuario=usuario.id_usuario)

        usuario.perfil.tipo_comida_fav = form.tipo_comida_fav.data
        usuario.perfil.restricciones = form.restricciones.data
        usuario.perfil.presupuesto_promedio = form.presupuesto_promedio.data

        db.session.commit()
        flash("Perfil actualizado exitosamente.", "success")
        return redirect(url_for('main.perfil'))

    return render_template('perfil.html', form=form, usuario=usuario)

# Logout
@main.route('/logout')
@login_required
def logout():
    logout_user()
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
        return redirect(url_for('main.perfil'))

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
