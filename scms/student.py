from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Student, Enrollment

student_bp = Blueprint("student", __name__, url_prefix="/student")


# STUDENT DASHBOARD
@student_bp.route("/dashboard")
@login_required
def dashboard():
    if current_user.role != "student":
        return "Unauthorized Access", 403

    student = Student.query.filter_by(user_id=current_user.id).first()
    enrollments = Enrollment.query.filter_by(student_id=student.id).all()

    return render_template("student/dashboard.html", student=student, enrollments=enrollments)


# STUDENT PROFILE PAGE
@student_bp.route("/profile")
@login_required
def profile():
    if current_user.role != "student":
        return "Unauthorized Access", 403

    student = Student.query.filter_by(user_id=current_user.id).first()
    enrollments = Enrollment.query.filter_by(student_id=student.id).all()

    return render_template("student/profile.html", student=student, enrollments=enrollments)
