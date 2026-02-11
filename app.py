from flask import Flask, render_template, request, redirect, url_for, flash, session
from functools import wraps
import requests
import re
import os

app = Flask(__name__)

# ==========================================
# CONFIGURACIÓN GENERAL
# ==========================================
app.secret_key = os.environ.get('SECRET_KEY', 'clave-secreta-temporal')

# ==========================================
# CONFIGURACIÓN DE reCAPTCHA (CORRECTA PARA RENDER)
# ==========================================
RECAPTCHA_SITE_KEY = os.environ.get('RECAPTCHA_SITE_KEY')
RECAPTCHA_SECRET_KEY = os.environ.get('RECAPTCHA_SECRET_KEY')

# ==========================================
# BASE DE DATOS SIMULADA
# ==========================================
usuarios_db = []

# ==========================================
# DECORADOR DE AUTENTICACIÓN
# ==========================================
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session:
            flash('Debes iniciar sesión para acceder a esta página', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# ==========================================
# VERIFICACIÓN DE reCAPTCHA
# ==========================================
def verify_recaptcha(recaptcha_response):
    if not recaptcha_response:
        return False

    verify_url = 'https://www.google.com/recaptcha/api/siteverify'

    data = {
        'secret': RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response,
        'remoteip': request.remote_addr
    }

    try:
        response = requests.post(verify_url, data=data)
        result = response.json()

        if result.get('success'):
            return True
        else:
            print('❌ reCAPTCHA falló:', result.get('error-codes'))
            return False

    except Exception as e:
        print('❌ Error reCAPTCHA:', str(e))
        return False

# ==========================================
# RUTAS
# ==========================================
@app.route('/')
def index():
    breadcrumbs = [{'nombre': 'Inicio', 'url': url_for('index')}]
    return render_template(
        'index.html',
        breadcrumbs=breadcrumbs,
        recaptcha_site_key=RECAPTCHA_SITE_KEY
    )

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    breadcrumbs = [
        {'nombre': 'Inicio', 'url': url_for('index')},
        {'nombre': 'Registro', 'url': url_for('registro')}
    ]

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        correo = request.form.get('correo')
        password = request.form.get('password')
        recaptcha_response = request.form.get('g-recaptcha-response')

        if not verify_recaptcha(recaptcha_response):
            flash('Por favor completa el reCAPTCHA', 'error')
            return render_template(
                'registro.html',
                breadcrumbs=breadcrumbs,
                recaptcha_site_key=RECAPTCHA_SITE_KEY
            )

        if not nombre or not correo or not password:
            flash('Todos los campos son obligatorios', 'error')
            return render_template(
                'registro.html',
                breadcrumbs=breadcrumbs,
                recaptcha_site_key=RECAPTCHA_SITE_KEY
            )

        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ]+$', nombre):
            flash('El nombre solo debe contener letras', 'error')
            return render_template(
                'registro.html',
                breadcrumbs=breadcrumbs,
                recaptcha_site_key=RECAPTCHA_SITE_KEY
            )

        if not re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]{2,}$', correo):
            flash('Correo inválido', 'error')
            return render_template(
                'registro.html',
                breadcrumbs=breadcrumbs,
                recaptcha_site_key=RECAPTCHA_SITE_KEY
            )

        if len(password) < 8:
            flash('La contraseña debe tener al menos 8 caracteres', 'error')
            return render_template(
                'registro.html',
                breadcrumbs=breadcrumbs,
                recaptcha_site_key=RECAPTCHA_SITE_KEY
            )

        if any(u['correo'] == correo for u in usuarios_db):
            flash('Este correo ya está registrado', 'error')
            return render_template(
                'registro.html',
                breadcrumbs=breadcrumbs,
                recaptcha_site_key=RECAPTCHA_SITE_KEY
            )

        usuarios_db.append({
            'nombre': nombre,
            'correo': correo,
            'password': password
        })

        flash('¡Registro exitoso!', 'success')
        return redirect(url_for('login'))

    return render_template(
        'registro.html',
        breadcrumbs=breadcrumbs,
        recaptcha_site_key=RECAPTCHA_SITE_KEY
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    breadcrumbs = [
        {'nombre': 'Inicio', 'url': url_for('index')},
        {'nombre': 'Iniciar Sesión', 'url': url_for('login')}
    ]

    if request.method == 'POST':
        correo = request.form.get('correo')
        password = request.form.get('password')
        recaptcha_response = request.form.get('g-recaptcha-response')

        if not verify_recaptcha(recaptcha_response):
            flash('Completa el reCAPTCHA', 'error')
            return render_template(
                'login.html',
                breadcrumbs=breadcrumbs,
                recaptcha_site_key=RECAPTCHA_SITE_KEY
            )

        usuario = next(
            (u for u in usuarios_db if u['correo'] == correo and u['password'] == password),
            None
        )

        if usuario:
            session['usuario'] = usuario['nombre']
            flash(f'Bienvenido {usuario["nombre"]}', 'success')
            return redirect(url_for('dashboard'))

        flash('Credenciales incorrectas', 'error')

    return render_template(
        'login.html',
        breadcrumbs=breadcrumbs,
        recaptcha_site_key=RECAPTCHA_SITE_KEY
    )

@app.route('/dashboard')
@login_required
def dashboard():
    breadcrumbs = [{'nombre': 'Panel', 'url': url_for('dashboard')}]
    return render_template('dashboard.html', breadcrumbs=breadcrumbs)

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    flash('Sesión cerrada', 'success')
    return redirect(url_for('index'))

# ==========================================
# INICIO DEL SERVIDOR (RENDER)
# ==========================================
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
