from flask import render_template, redirect, url_for, flash, request, send_file, jsonify,session
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import  Cliente
from app import login_manager, db
import base64
from io import BytesIO
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return Cliente.query.get(int(user_id))

def init_routes(app):
    @app.route("/")
    @login_required
    def home():
        return render_template("index.html")
 
    @app.route("/login", methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
           email = request.form.get('email')
           password = request.form.get('password')
           user = Cliente.query.filter_by(email=email).first()

           if not user:
            flash('Usuario no encontrado', 'danger')
            return redirect(url_for('login'))

           if not check_password_hash(user.password, password):
            flash('Contraseña incorrecta', 'danger')
            return redirect(url_for('login'))

           login_user(user)
           flash('Inicio de sesión exitoso', 'success')
           return redirect(url_for('home'))

        return render_template("login.html")

    @app.route("/registro", methods=['GET', 'POST'])
    def registro():
        if request.method == 'POST':
            username = request.form.get('username')
            nombre = request.form.get('nombre')
            apellido = request.form.get('apellido')
            email = request.form.get('email')
            telefono = request.form.get('telefono')
            direccion = request.form.get('direccion')
            password = request.form.get('password')

            # Verificar si el username o el email ya existen
            user_by_username = Cliente.query.filter_by(username=username).first()
            user_by_email = Cliente.query.filter_by(email=email).first()

            if user_by_username:
                flash('El nombre de usuario ya está en uso. Por favor, elige otro.', 'danger')
                return redirect(url_for('registro'))
            
            if user_by_email:
                flash('El correo electrónico ya está en uso. Por favor, elige otro.', 'danger')
                return redirect(url_for('registro'))

            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            nuevo_cliente = Cliente(username=username, email=email, password=hashed_password, nombre=nombre, apellido=apellido, telefono=telefono, direccion=direccion)
            db.session.add(nuevo_cliente)
            db.session.commit()
            flash('Cliente registrado exitosamente', 'success')
            return redirect(url_for('login'))
        return redirect(url_for('login'))

   