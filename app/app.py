from flask import Flask, render_template, request, url_for, redirect
import controller

app = Flask(__name__)

""" 
Routes 
"""


@app.route("/")
@app.route("/students")
def students():
    return render_template("students.html")


@app.route('/form_insert_student')
def form():
    return render_template('form_insert_student.html')


@app.route("/save_student", methods=["POST"])
def save_student():
    passport = request.form["passport"]
    name = request.form["name"]
    birth = request.form["birth"]
    height = request.form["height"]
    controller.insert_students(passport, name, birth, height)
    return redirect("/students_list")


@app.route('/students_list')
def students_list():
    students = controller.obtain_student()
    return render_template('students_list.html', students=students)


@app.route("/delete_student", methods=["POST"])
def delete_student():
    controller.delete_student(request.form["passport"])
    return redirect("/students_list")


@app.route("/edit_student/<passport>")
def edit_student(passport):
    student = controller.obtain_student_from_passport(passport)
    return render_template("edit_student.html", student=student)


@app.route("/update_student", methods=["POST"])
def update_student():
    passport = request.form["passport"]
    name = request.form["name"]
    birth = request.form["birth"]
    height = request.form["height"]
    controller.update_student(name, birth, height, passport)
    return redirect("/students_list")


# Launch server
if __name__ == ("__main__"):
    app.run(debug=True)
