from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from .forms import LoginForm, RegisterForm
from .models import User, Student
from . import db, bcrypt

auth_bp = Blueprint("auth", __name__)


# REGISTER (Supports Student + Admin)
@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():

        # STOP normal users from creating admin accounts
        if form.role.data == "admin":
            if not current_user.is_authenticated or current_user.role != "admin":
                flash("Only admins can create admin accounts!", "danger")
                return redirect(url_for("auth.register"))

        # email check
        existing = User.query.filter_by(email=form.email.data).first()
        if existing:
            flash("Email already registered!", "danger")
            return redirect(url_for("auth.register"))

        # hash password
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode("utf-8")

        # create user with selected role
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_pw,
            role=form.role.data
        )
        db.session.add(user)
        db.session.commit()

        # create student profile only if role == "student"
        if user.role == "student":
            student = Student(name=form.username.data, user_id=user.id)
            db.session.add(student)
            db.session.commit()

        flash(f"{user.role.capitalize()} account created successfully!", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html", form=form)


# LOGIN
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Login successful!", "success")

            if user.role == "admin":
                return redirect(url_for("admin.dashboard"))
            elif user.role == "student":
                return redirect(url_for("student.dashboard"))
            else:
                return redirect(url_for("auth.login"))

        flash("Invalid email or password!", "danger")

    return render_template("login.html", form=form)


# LOGOUT
@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully", "info")
    return redirect(url_for("auth.login"))

