# Shell Plus Model Imports
from datetime import date
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
from django.utils import timezone
from django.urls import reverse
from django.db.models import Exists, OuterRef, Subquery

def probar_orm():
    #INSERCIONES
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


