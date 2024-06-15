# Shell Plus Model Imports
from datetime import date, datetime
from core.models import Grade, GradeDetail, Period, Professor, Student, Subject
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
# Shell Plus Django Imports
from django.core.cache import cache
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When
from django.db.models.functions import Length
from django.utils import timezone
from django.urls import reverse
from django.db.models import Exists, OuterRef, Subquery

def probar_orm():
    # INSERCIONES
    # Bulk_Create
    def bulk_create_periods():
        user = User.objects.get(id=1)
        periods = [
            Period(user=user,name='1ER SEMESTRE 2020' ,start_date=date(2020,3,2), end_date=date(2020,7,18)),
            Period(user=user,name='2DO SEMESTRE 2020' ,start_date=date(2020,8,2), end_date=date(2020,12,18)),
            Period(user=user,name='1ER SEMESTRE 2021' ,start_date=date(2021,3,2), end_date=date(2021,7,18)),
            Period(user=user,name='2DO SEMESTRE 2021' ,start_date=date(2021,8,2), end_date=date(2021,12,18)),
            Period(user=user,name='1ER SEMESTRE 2022' ,start_date=date(2022,3,2), end_date=date(2022,7,18)),
            Period(user=user,name='2DO SEMESTRE 2022' ,start_date=date(2022,8,2), end_date=date(2022,12,18)),
            Period(user=user,name='1ER SEMESTRE 2023' ,start_date=date(2023,3,2), end_date=date(2023,7,18)),
            Period(user=user,name='2DO SEMESTRE 2023' ,start_date=date(2023,8,2), end_date=date(2023,12,18)),
            Period(user=user,name='1ER SEMESTRE 2024' ,start_date=date(2024,3,2), end_date=date(2024,7,18)),
            Period(user=user,name='2DO SEMESTRE 2024' ,start_date=date(2024,8,2), end_date=date(2024,12,18))
        ]
        Period.objects.bulk_create(periods)
    # bulk_create_periods()

    def bulk_create_subjects():
        user = User.objects.get(id=1)
        subjects = [
            Subject(user=user, name='Cálculo I'),
            Subject(user=user, name='Cálculo Diferencial'),
            Subject(user=user, name='Física'),
            Subject(user=user, name='Cálculo II'),
            Subject(user=user, name='Algoritmo y Lógica de Programación'),
            Subject(user=user, name='Ingeniería Financiera'),
            Subject(user=user, name='Sistemas Operativos'),
            Subject(user=user, name='Realidad Nacional'),
            Subject(user=user, name='Cálculo Vectorial'),
            Subject(user=user, name='Sistemas Numéricos')
        ]
        Subject.objects.bulk_create(subjects)
    # bulk_create_subjects()

    def bulk_create_professors():
        user = User.objects.get(id=1)
        professors = [
            Professor(user=user, name='Esteban García', idcard='203845697'),
            Professor(user=user, name='Valentina Martínez', idcard='874512369'),
            Professor(user=user, name='Lucas Sánchez', idcard='632548971'),
            Professor(user=user, name='Esteban Rodríguez', idcard='958463217'),
            Professor(user=user, name='Oriol Romeu', idcard='741236985'),
            Professor(user=user, name='Mateo López', idcard='369875412'),
            Professor(user=user, name='Valeria Díaz', idcard='524197836'),
            Professor(user=user, name='Matías Gómez', idcard='486371925'),
            Professor(user=user, name='Isabella Pérez', idcard='215698347'),
            Professor(user=user, name='Sebastián González', idcard='793564128')
        ]
        Professor.objects.bulk_create(professors)
    # bulk_create_professors()

    def bulk_create_students():
        user = User.objects.get(id=1)
        students = [
            Student(user=user, name='Juan Torres', idcard= '567894321'),
            Student(user=user, name='María Navarro', idcard= '239875641'),
            Student(user=user, name='Pablo Ramírez', idcard= '908712345'),
            Student(user=user, name='Ana Ruiz', idcard= '653487912'),
            Student(user=user, name='Carlos Moreno', idcard= '124567890'),
            Student(user=user, name='Andrés Delgado', idcard= '789032145'),
            Student(user=user, name='Denisse Castillo', idcard= '432189076'),
            Student(user=user, name='Doménica Narváez', idcard= '876543210'),
            Student(user=user, name='David Serrano', idcard= '346798120'),
            Student(user=user, name='Gina Garcés', idcard= '981273456')
        ]
        Student.objects.bulk_create(students)
    # bulk_create_students()

    # Create y Save
    def create_grade(period_id, professor_id, subject_id):
        user = User.objects.get(id=1)
        period = Period.objects.get(id=period_id)
        subject = Subject.objects.get(id=subject_id)
        professor = Professor.objects.get(id=professor_id)

        Grade.objects.create(
            user=user,
            period = period,
            subject = subject,
            professor = professor
        )
    # create_grade(8, 2, 3)
    # create_grade(8, 4, 6)
    # create_grade(8, 1, 5)
    # create_grade(6, 7, 2)
    # create_grade(6, 7, 9)
    # create_grade(5, 3, 8)
    # create_grade(2, 10, 4)
    # create_grade(7, 6, 1)
    # create_grade(9, 5, 7)
    # create_grade(4, 8, 10)

    def save_grade_detail(grade_id, student_id, score1, score2, extension):
        user = User.objects.get(id=1)
        grade = Grade.objects.get(id=grade_id)
        student = Student.objects.get(id=student_id)
        grade_detail = GradeDetail(
            user=user,
            grade = grade,
            student = student,
            score1 = score1,
            score2 = score2,
            extension = extension
        )
        grade_detail.save()
    # save_grade_detail(1, 2, 8.5, 9.3, 7.4)
    # save_grade_detail(3, 4, 6.2, 7.8, 8.1)
    # save_grade_detail(5, 6, 9.0, 8.7, 6.5)
    # save_grade_detail(7, 8, 5.3, 6.6, 7.9)
    # save_grade_detail(10, 1, 9.2, 8.0, 7.6)
    # save_grade_detail(9, 10, 7.1, 8.2, 9.4)
    # save_grade_detail(2, 3, 6.9, 5.8, 7.2)
    # save_grade_detail(4, 5, 8.3, 9.1, 6.7)
    # save_grade_detail(6, 7, 7.5, 8.9, 9.0)
    # save_grade_detail(8, 9, 6.4, 7.7, 8.8)

    # Consultas

    # Seleccionar todos los estudiantes cuyo nombre comienza con 'Est'
    def query_1():
        students = Student.active_objects.filter(name__istartswith = 'Est')
        print(students)  
    # query_1()

    # Seleccionar todos los profesores cuyo nombre contiene 'or'
    def query_2():
        professors = Professor.active_objects.filter(name__icontains='or')
        print(professors)
    # query_2()

    # Seleccionar todas las asignaturas cuya descripción termina en '10'
    def query_3():
        subjects = Subject.active_objects.filter(name__endswith = '10')
        print(subjects)
    # query_3()

    # Seleccionar todas las notas con nota1 mayor que 8.0
    def query_4():
        scores = GradeDetail.active_objects.filter(score1__gt = 8.0)
        print(scores)
    # query_4()

    # Seleccionar todas las notas con nota2 menor que 9.0
    def query_5():
        scores = GradeDetail.active_objects.filter(score2__lt = 9)
        print(scores)
    # query_5()

    # Seleccionar todas las notas con recuperacion igual a 9.5
    def query_6():
        scores = GradeDetail.active_objects.filter(extension = 9.5)
        print(scores)
    # query_6()

    # Seleccionar todos los estudiantes cuyo nombre comienza con 'Est' y su cedula termina en '1'
    def query_7():
        students = Student.active_objects.filter(Q(name__istartswith = 'est') & Q(idcard__endswith = '1'))
        print(students)
    # query_7()

    # Seleccionar todas las asignaturas cuya descripción contiene 'Asig' o termina en '5'
    def query_8():
        subjects = Subject.active_objects.filter(Q(name__icontains = 'asig') | Q(name__endswith = '5'))
        print(subjects)
    # query_8()

    # Seleccionar todos los profesores cuyo nombre no contiene 'or'
    def query_9():
        professors = Professor.active_objects.filter(~Q(name__icontains='or'))
        print(professors)
    # query_9()

    # Seleccionar todas las notas con nota1 mayor que 7.0 y nota2 menor que 8.0
    def query_10():
        scores = GradeDetail.active_objects.filter(Q(score1__gt = 7) & Q(score2__lt = 8))
        print(scores)
    # query_10()

    # Seleccionar todas las notas con recuperacion igual a None o nota2 mayor que 9.0
    def query_11():
        scores = GradeDetail.active_objects.filter(Q(extension = None) | Q(score2__gt = 9))
        print(scores)
    # query_11()

    # Seleccionar todas las notas con nota1 entre 7.0 y 9.0
    def query_12():
        scores = GradeDetail.active_objects.filter(Q(score1__gte = 7) & Q(score1__lte = 9))
        print(scores)
    # query_12()

    # Seleccionar todas las notas con nota2 fuera del rango 6.0 a 8.0
    def query_13():
        scores = GradeDetail.active_objects.exclude(Q(score2__gte = 6) & Q(score2__lte = 8))
        print(scores)
    # query_13()

    # Seleccionar todas las notas cuya recuperacion no sea None
    def query_14():
        scores = GradeDetail.active_objects.filter(~Q(extension = None))
        print(scores)
    # query_14()

    # Seleccionar todas las notas creadas en el último año
    def query_15():
        scores = GradeDetail.active_objects.filter(created__year = datetime.now().year)
        print(scores)
    # query_15()

    # Seleccionar todas las notas creadas en el último mes
    def query_16():
        scores = GradeDetail.active_objects.filter(created__month = datetime.now().month)
        print(scores)
    # query_16()

    # Seleccionar todas las notas creadas en el último día
    def query_17():
        scores = GradeDetail.active_objects.filter(created__day = datetime.now().day)
        print(scores)
    # query_17()

    # Seleccionar todas las notas creadas antes del año 2023
    def query_18():
        scores = GradeDetail.active_objects.filter(created__year__lt = 2023)
        print(scores)
    # query_18()

    # Seleccionar todas las notas creadas en marzo de cualquier año
    def query_19():
        scores = GradeDetail.active_objects.filter(created__month = 3)
        print(scores)
    # query_19()

    # Seleccionar todos los estudiantes cuyo nombre tiene exactamente 10 caracteres:
    def query_20():
        students = Student.active_objects.filter(name__regex=r'^.{%d}$'%10)
        print(students)
    # query_20()
