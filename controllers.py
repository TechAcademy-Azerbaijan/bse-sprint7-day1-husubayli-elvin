from flask import Flask, render_template

from app import app


students = [
    {
        'id': 1,
        'name': 'Enver',
        'surname': 'Azimov',
        'gender': 'Male',
        'status': 'active',
        'img': 'https://www.univ-amu.fr/system/files/2018-10/DFD-TUILE-Devenir_doctorant.jpg',
        'bio': ''
    },
    {
        'id': 2,
        'name': 'Nizami',
        'surname': 'Suleymanov',
        'gender': 'Male',
        'status': 'active',
        'img': 'https://www.univ-amu.fr/system/files/2018-10/DFD-TUILE-Devenir_doctorant.jpg',
        'bio': ''
    },
    {
        'id': 3,
        'name': 'Kenan',
        'surname': 'Samandarli',
        'gender': 'Male',
        'status': 'active',
        'img': 'https://www.univ-amu.fr/system/files/2018-10/DFD-TUILE-Devenir_doctorant.jpg',
        'bio': 'Now! I learning PYTHON'
    },
    {
        'id': 4,
        'name': 'Kenan',
        'surname': 'Samandarli',
        'gender': 'Male',
        'status': 'deactive',
        'img': 'https://www.univ-amu.fr/system/files/2018-10/DFD-TUILE-Devenir_doctorant.jpg',
        'bio': 'sadasdasda'
    }
]

@app.route('/students/<int:post_index>')
def get_bio_student(post_index):

    student = list(filter(lambda student: student['id'] == post_index, students))[0]

    return render_template('bio-student.html', student=student)


@app.route('/students')
def show_students():

    return render_template('main-page.html', students=students)
