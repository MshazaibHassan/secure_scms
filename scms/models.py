from . import db
from flask_login import UserMixin
from . import login_manager


# Load user for login sessions
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# USER MODEL
class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # "admin" or "student"

    student = db.relationship("Student", backref="user", uselist=False)


# STUDENT PROFILE MODEL
class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    enrollments = db.relationship("Enrollment", backref="student", lazy=True)


# COURSE MODEL
class Course(db.Model):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(200), nullable=False)

    enrollments = db.relationship("Enrollment", backref="course", lazy=True)


# ENROLLMENT MODEL
class Enrollment(db.Model):
    __tablename__ = "enrollments"

    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(db.Integer, db.ForeignKey("students.id"))
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"))
