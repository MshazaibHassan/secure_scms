from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import User, Student, Course, Enrollment
from . import db, bcrypt

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


# --------- ACCESS CONTROL ----------
def admin_only():
    if not current_user.is_authenticated or current_user.role != "admin":
        flash("Unauthorized access!", "danger")
        return False
    return True


# --------- ADMIN DASHBOARD ----------
@admin_bp.route("/dashboard")
@login_required
def dashboard():
    if not admin_only():
        return redirect(url_for("auth.login"))
    return render_template("admin/dashboard.html")


# --------- VIEW STUDENTS ----------
@admin_bp.route("/students")
@login_required
def students():
    if not admin_only():
        return redirect(url_for("auth.login"))

    all_students = Student.query.all()
    return render_template("admin/students.html", students=all_students)


# --------- ADD STUDENT ----------
@admin_bp.route("/add-student", methods=["GET", "POST"])
@login_required
def add_student():
    if not admin_only():
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        if not name or not email or not password:
            flash("All fields required!", "danger")
            return redirect(url_for("admin.add_student"))

        # Create User
        hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")
        user = User(username=name, email=email, password=hashed_pw, role="student")
        db.session.add(user)
        db.session.commit()

        # Create Student Profile
        student = Student(name=name, user_id=user.id)
        db.session.add(student)
        db.session.commit()

        flash("Student added successfully!", "success")
        return redirect(url_for("admin.students"))

    return render_template("admin/add_student.html")


# --------- DELETE STUDENT ----------
@admin_bp.route("/delete-student/<int:id>")
@login_required
def delete_student(id):
    if not admin_only():
        return redirect(url_for("auth.login"))

    student = Student.query.get(id)

    if student:
        Enrollment.query.filter_by(student_id=id).delete()
        user = User.query.get(student.user_id)
        db.session.delete(student)
        db.session.delete(user)
        db.session.commit()

    flash("Student deleted!", "info")
    return redirect(url_for("admin.students"))


# --------- VIEW COURSES ----------
@admin_bp.route("/courses")
@login_required
def courses():
    if not admin_only():
        return redirect(url_for("auth.login"))

    all_courses = Course.query.all()
    return render_template("admin/courses.html", courses=all_courses)


# --------- ADD COURSE ----------
@admin_bp.route("/add-course", methods=["GET", "POST"])
@login_required
def add_course():
    if not admin_only():
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        course_name = request.form.get("course_name")

        if not course_name:
            flash("Course name is required!", "danger")
            return redirect(url_for("admin.add_course"))

        course = Course(course_name=course_name)
        db.session.add(course)
        db.session.commit()

        flash("Course added successfully!", "success")
        return redirect(url_for("admin.courses"))

    return render_template("admin/add_course.html")


# --------- DELETE COURSE ----------
@admin_bp.route("/delete-course/<int:id>")
@login_required
def delete_course(id):
    if not admin_only():
        return redirect(url_for("auth.login"))

    course = Course.query.get(id)

    if course:
        Enrollment.query.filter_by(course_id=id).delete()
        db.session.delete(course)
        db.session.commit()

    flash("Course deleted!", "info")
    return redirect(url_for("admin.courses"))


# --------- ASSIGN COURSE ----------
@admin_bp.route("/assign-course", methods=["GET", "POST"])
@login_required
def assign_course():
    if not admin_only():
        return redirect(url_for("auth.login"))

    students = Student.query.all()
    courses = Course.query.all()

    if request.method == "POST":
        student_id = request.form.get("student_id")
        course_id = request.form.get("course_id")

        # Check duplicate assignment
        already = Enrollment.query.filter_by(student_id=student_id, course_id=course_id).first()
        if already:
            flash("Course already assigned to this student.", "warning")
            return redirect(url_for("admin.assign_course"))

        enrollment = Enrollment(student_id=student_id, course_id=course_id)
        db.session.add(enrollment)
        db.session.commit()

        flash("Course assigned successfully!", "success")
        return redirect(url_for("admin.assign_course"))

    return render_template("admin/assign_course.html", students=students, courses=courses)
