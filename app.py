from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "my_secret_key" 

teachers = [{"username": "admin", "password": "admin"}]
students = [
    {"username": "210501", "password": "password1", "marks": {"Data Structures": 80, "Object Oriented Programming": 75,"Digital Electronics":90,"Probability Statistics":88,"Discrete Mathematics":92,"Engineering Economics":96}},
    {"username": "210502", "password": "password2", "marks": {"Data Structures": 90, "Object Oriented Programming": 85,"Digital Electronics":90,"Probability Statistics":88,"Discrete Mathematics":92,"Engineering Economics":96}},
    {"username": "210503", "password": "password2", "marks": {"Data Structures": 90, "Object Oriented Programming": 85,"Digital Electronics":90,"Probability Statistics":88,"Discrete Mathematics":92,"Engineering Economics":96}},
    {"username": "210504", "password": "password2", "marks": {"Data Structures": 90, "Object Oriented Programming": 85,"Digital Electronics":90,"Probability Statistics":88,"Discrete Mathematics":92,"Engineering Economics":96}},
    {"username": "210505", "password": "password2", "marks": {"Data Structures": 90, "Object Oriented Programming": 85,"Digital Electronics":90,"Probability Statistics":88,"Discrete Mathematics":92,"Engineering Economics":96}},
    {"username": "210506", "password": "password2", "marks": {"Data Structures": 90, "Object Oriented Programming": 85,"Digital Electronics":90,"Probability Statistics":88,"Discrete Mathematics":92,"Engineering Economics":96}},
    {"username": "210507", "password": "password2", "marks": {"Data Structures": 90, "Object Oriented Programming": 85,"Digital Electronics":90,"Probability Statistics":88,"Discrete Mathematics":92,"Engineering Economics":96}},
    {"username": "210508", "password": "password2", "marks": {"Data Structures": 90, "Object Oriented Programming": 85,"Digital Electronics":90,"Probability Statistics":88,"Discrete Mathematics":92,"Engineering Economics":96}},
    {"username": "210509", "password": "password2", "marks": {"Data Structures": 90, "Object Oriented Programming": 85,"Digital Electronics":90,"Probability Statistics":88,"Discrete Mathematics":92,"Engineering Economics":96}},
    {"username": "210510", "password": "password2", "marks": {"Data Structures": 90, "Object Oriented Programming": 85,"Digital Electronics":90,"Probability Statistics":88,"Discrete Mathematics":92,"Engineering Economics":96}},
    {"username": "210511", "password": "password2", "marks": {"Data Structures": 90, "Object Oriented Programming": 85,"Digital Electronics":90,"Probability Statistics":88,"Discrete Mathematics":92,"Engineering Economics":96}},
    {"username": "210512", "password": "password2", "marks": {"Data Structures": 90, "Object Oriented Programming": 85,"Digital Electronics":90,"Probability Statistics":88,"Discrete Mathematics":92,"Engineering Economics":96}},
    {"username": "210513", "password": "password2", "marks": {"Data Structures": 90, "Object Oriented Programming": 85,"Digital Electronics":90,"Probability Statistics":88,"Discrete Mathematics":92,"Engineering Economics":96}},
    {"username": "210514", "password": "password2", "marks": {"Data Structures": 90, "Object Oriented Programming": 85,"Digital Electronics":90,"Probability Statistics":88,"Discrete Mathematics":92,"Engineering Economics":96}},
    {"username": "210515", "password": "password2", "marks": {"Data Structures": 90, "Object Oriented Programming": 85,"Digital Electronics":90,"Probability Statistics":88,"Discrete Mathematics":92,"Engineering Economics":96}},
    {"username": "210516", "password": "password2", "marks": {"Data Structures": 90, "Object Oriented Programming": 85,"Digital Electronics":90,"Probability Statistics":88,"Discrete Mathematics":92,"Engineering Economics":96}},
    {"username": "210517", "password": "password2", "marks": {"Data Structures": 90, "Object Oriented Programming": 85,"Digital Electronics":90,"Probability Statistics":88,"Discrete Mathematics":92,"Engineering Economics":96}},
    {"username": "210518", "password": "password2", "marks": {"Data Structures": 90, "Object Oriented Programming": 85,"Digital Electronics":90,"Probability Statistics":88,"Discrete Mathematics":92,"Engineering Economics":96}},
    {"username": "210519", "password": "password2", "marks": {"Data Structures": 90, "Object Oriented Programming": 85,"Digital Electronics":90,"Probability Statistics":88,"Discrete Mathematics":92,"Engineering Economics":96}},
    {"username": "210520", "password": "password2", "marks": {"Data Structures": 90, "Object Oriented Programming": 85,"Digital Electronics":90,"Probability Statistics":88,"Discrete Mathematics":92,"Engineering Economics":96}}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/teacher_login', methods=['GET', 'POST'])
def teacher_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        for teacher in teachers:
            if teacher['username'] == username and teacher['password'] == password:
                session['username'] = username
                return redirect('/teacher_dashboard')

        return render_template('teacher_login.html', error='Invalid credentials')

    return render_template('teacher_login.html', error=None)

@app.route('/teacher_dashboard')
def teacher_dashboard():
    if 'username' in session:
        num_students = len(students)
        return render_template('teacher_dashboard.html', username=session['username'], num_students=num_students, students=students)
    else:
        return redirect('/teacher_login')

@app.route('/edit_marks/<username>', methods=['GET', 'POST'])
def edit_marks(username):
    if 'username' in session:
        if request.method == 'POST':
            marks = {}
            for key, value in request.form.items():
                if key != 'submit':
                    marks[key] = int(value)

            for student in students:
                if student['username'] == username:
                    student['marks'] = marks
                    break

            return redirect('/teacher_dashboard')

        student = next((student for student in students if student['username'] == username), None)
        if student:
            marks = student['marks']
            return render_template('edit_marks.html', username=username, marks=marks)
        else:
            return redirect('/teacher_dashboard')
    else:
        return redirect('/teacher_login')

@app.route('/student_login', methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        for student in students:
            if student['username'] == username and student['password'] == password:
                session['username'] = username
                return redirect('/student_dashboard')

        return render_template('student_login.html', error='Invalid credentials')

    return render_template('student_login.html', error=None)

@app.route('/student_dashboard')
def student_dashboard():
    if 'username' in session:
        student = next((student for student in students if student['username'] == session['username']), None)
        if student:
            marks = student['marks']
            return render_template('student_dashboard.html', username=session['username'], marks=marks)
        else:
            return redirect('/')
    else:
        return redirect('/student_login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        for student in students:
            if student['username'] == username:
                return render_template('register.html', error='Username already exists')

        students.append({"username": username, "password": password, "marks": {}})
        session['username'] = username
        return redirect('/student_dashboard')

    return render_template('register.html', error=None)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
