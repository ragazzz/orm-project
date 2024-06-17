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
from django.db.models.functions import Length

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

    # Consultas combinadas con funciones avanzadas
    print(".........................................")
    #20. Seleccionar todos los estudiantes cuyo nombre tiene exactamente 10 caracteres:✔️
    def student_length_10():
        return Student.objects.filter(name__exact=10)
    
    # print("✔️ Estudiantes con nombre de longitud 10 ", student_length_10())

    print(".........................................")
    #21. Seleccionar todas las notas con nota1 y nota2 mayores a 7.5:✔️
    def query_21():
        consult = GradeDetail.objects.filter(score1__gt =7.5, score2__gt =7.5)
        return consult
    
    # print("✔️ notas con nota1 y nota2 mayores a 7.5 ", query_21())

    print(".........................................")
    #22. Seleccionar todas las notas con recuperacion no nula y nota1 mayor a nota2:✔️
    def query_22():
        grades = GradeDetail.objects.filter(observation__isnull=False, score1__gt=F('score2'))
        return grades
    
    # print("✔️ todas las notas con recuperacion no nula y nota1 mayor a nota2:", query_22())

    print(".........................................")
    #23. Seleccionar todas las notas con nota1 mayor a 8.0 o nota2 igual a 7.5:✔️
    def query_23():
        grades = GradeDetail.objects.filter(Q(score1__gt=8.0) | Q(score2=7.5))
        return grades
    # print("✔️ todas las notas con nota1 mayor a 8.0 o nota2 igual a 7.5: ", query_23())

    print(".........................................")
    #24. Seleccionar todas las notas con recuperacion mayor a nota1 y nota2:✔️
    def query_24():
        grades = GradeDetail.objects.filter(extension__gt=F('score1')).filter(extension__gt=F('score2'))
        return grades
    # print("✔️ Todas las notas con extensión mayor que score1 y score2:", query_24())

    print(".........................................")
    #Consultas con subconsultas y anotaciones
    #25. Seleccionar todos los estudiantes con al menos una nota de recuperación:✔️
    def query_25():
        students = Student.objects.filter(grades__extension__isnull=False).distinct()
        return students
    # print("✔️ Estudiantes con al menos una nota de recuperación: ", query_25())

    print(".........................................")
    #26. Seleccionar todos los profesores que han dado una asignatura específica:✔️
    def query_26(id):
        professors = Professor.objects.filter(grades__subject_id=id).distinct()
        return professors
    # print("✔️ profesores que han dado una asignatura específica ", query_26(4))

    print(".........................................")
    #27. Seleccionar todas las asignaturas que tienen al menos una nota registrada:✔️
    def query_27():
        subjects = Subject.objects.annotate(grades_count=Count('grades')).filter(grades_count__gt=0)
        return subjects
    # print("✔️ asignaturas que tienen al menos una nota registrada ", query_27())

    print(".........................................")
    #28. Seleccionar todas las asignaturas que no tienen notas registradas:✔️
    def query_28():
        subjects = Subject.objects.annotate(grades_count=Count('grades')).filter(grades_count=0)
        return subjects
    # print("✔️ todas las asignaturas que no tienen notas registradas ", query_28())

    print(".........................................")
    # 29. Seleccionar todos los estudiantes que no tienen notas de recuperación:✔️
    def query_29():
        students = Student.objects.exclude(grades__extension__isnull=False).distinct()
        return students
    # print("✔️ todos los estudiantes que no tienen notas de recuperación ", query_29())

    print(".........................................")
    # 30. Seleccionar todas las notas cuyo promedio de nota1 y nota2 es mayor a 8.0:✔️
    def query_30():
        grades = GradeDetail.objects.annotate(average_score=Avg((F('score1') + F('score2')) / 2)).filter(average_score__gt=8.0)
        return grades
    # print("✔️ notas cuyo promedio de nota1 y nota2 es mayor a 8.0 ", query_30())

    print(".........................................")
    #31. Seleccionar todas las notas con nota1 menor que 6.0 y nota2 mayor que 7.0:✔️
    def query_31():
        grades = GradeDetail.objects.filter(score1__lt=6.0, score2__gt=7.0)
        return grades
    # print("✔️ todas las notas con nota1 menor que 6.0 y nota2 mayor que 7.0 ", query_31())

    print(".........................................")
    #32. Seleccionar todas las notas con nota1 en la lista [7.0, 8.0, 9.0]:✔️
    def query_32():
        grades = GradeDetail.objects.filter(score1__in=[7.0, 8.0, 9.0])
        return grades
    # print("✔️ Notas con nota1 en la lista [7.0, 8.0, 9.0] ", query_32())
    

    print(".........................................")
    #33. Seleccionar todas las notas cuyo id está en un rango del 1 al 5:✔️
    def query_33():
        grades = GradeDetail.objects.filter(id__range=(1, 5)).order_by('id')
        for grade in grades:
            total = print(f"ID: {grade.id}, Nota1: {grade.score1}, Nota2: {grade.score2}, Nota de recuperacion: {grade.extension}")
        return total
    # query_33()

    print(".........................................")
    #34. Seleccionar todas las notas cuyo recuperacion no está en la lista [8.0, 9.0,10.0]:✔️
    def query_34():
        grades = GradeDetail.objects.filter(~Q(extension__in=[8.0, 9.0, 10.0]))
        return grades
    # print("✔️ Notas cuyo recuperacion no está en la lista [8.0, 9.0, 10.0] ", query_34())

    print(".........................................")
    #35. Suma de todas las notas de un estudiante:✔️
    def query_35(student_id):
        total = GradeDetail.objects.filter(student_id=student_id).aggregate(total=Sum('score1') + Sum('score2') + Sum('extension'))
        return total
    # print("✔️ Suma de todas las notas de un estudiante ", query_35(1))

    print(".........................................")
    #36. Nota máxima obtenida por un estudiante:✔️
    def query_36(student_id):
        max_scores = GradeDetail.objects.filter(student_id=student_id).aggregate(
            max_score1=Max('score1'),
            max_score2=Max('score2'),
            max_extension=Max('extension')
        )
        # Retornar la nota máxima entre score1, score2 y extension
        max_score = max(max_scores['max_score1'], max_scores['max_score2'], max_scores['max_extension'])
        return max_score
    # print("✔️ Nota máxima obtenida por un estudiante:", query_36(10))

    print(".........................................")
    #37. Nota mínima obtenida por un estudiante:✔️
    def query_37(student_id):
        min_scores = GradeDetail.objects.filter(student_id=student_id).aggregate(
            min_score1=Min('score1'),
            min_score2=Min('score2'),
            min_extension=Min('extension')
        )
        # Retornar la nota mínima entre score1, score2 y extension
        min_score = min(min_scores['min_score1'], min_scores['min_score2'], min_scores['min_extension'])
        return min_score
    # print("✔️ Nota mínima obtenida por un estudiante:", 37(10))

    print(".........................................")
    #38. Contar el número total de notas de un estudiante:✔️
    def query_38(student_id):
        total_notas = GradeDetail.objects.filter(student_id=student_id).aggregate(
            count_score1=Count('score1'),
            count_score2=Count('score2'),
            count_extension=Count('extension')
            )
        total_grades = total_notas['count_score1'] + total_notas['count_score2'] + total_notas['count_extension']
        return total_grades
    # print("✔️ Contar el número total de notas de un estudiante ", query_38(1))

    print(".........................................")
    #39. Promedio de todas las notas de un estudiante sin incluir recuperación ✔️
    def query_39(student_id):
        average = GradeDetail.objects.filter(student_id=student_id).aggregate(average=(Avg('score1') + Avg('score2')) / 2)
        return average
    # print("✔️ Promedio de todas las notas de un estudiante sin incluir recuperación ", query_39(1))

    # Consultas con subconsultas con los modelos relacionado. Aplicar relaciones inversas donde sea necesario
    # 40. Dado un estudiante obtener todas sus notas con el detalle de todos sus datos relacionados:✔️
    def query_40(student_id):
        student = Student.objects.prefetch_related(
            Prefetch(
                'grades',
                queryset=GradeDetail.objects.select_related(
                    'grade','grade__subject','grade__period','grade__professor'
                    )
                    )
                    ).get(id=student_id)
        for grade_detail in student.grades.all():
            return print(grade_detail)
    # print("✔️ Todas las notas de un estudiante con el detalle de todos sus datos relacionados:")
    # query_40(1)

    # Obtener todas las notas de un período específico
    def query_41(periodo_id):
        notas = GradeDetail.objects.filter(grade__period_id=periodo_id)
        print(notas)
    #query_41(1)

    # Consultar todas las notas de una asignatura dada en un período
    def query_42(asignatura_id, periodo_id):
        notas = GradeDetail.objects.filter(grade__subject_id=asignatura_id, grade__period_id=periodo_id)
        print(notas)
    # obtener_notas_por_asignatura_y_periodo(1, 1)

    def query_43(profesor_id):
        notas = GradeDetail.objects.filter(grade__professor_id=profesor_id)
        print(notas)
    # query_43(1)

    #
    def query_44(estudiante_id, valor):
        notas = GradeDetail.objects.filter(student_id=estudiante_id).filter(score1__gt=valor)
        print(notas)
    #query_44()

    #
    def query_45(estudiante_id):
        notas = GradeDetail.objects.filter(student_id=estudiante_id).order_by('grade__period__start_date')
        print(notas)
    # query_45()

    # ejercicio_46
    def query_46(estudiante_id):
        cantidad = GradeDetail.objects.filter(student_id=estudiante_id).count()
        print(cantidad)
    # query_46()

    # ejercicio_47
    def promedio_notas_por_estudiante_y_periodo(estudiante_id, periodo_id):
        promedio = GradeDetail.objects.filter(student_id=estudiante_id, grade__period_id=periodo_id).aggregate(Avg('score1'))
        print(promedio)
    # promedio_notas_por_estudiante_y_periodo(1, 1)

    # ejercicio_48
    def obtener_notas_por_observacion(observacion):
        notas = GradeDetail.objects.filter(observacion=observacion)
        print(notas)
    # obtener_notas_por_observacion('Aprobado')

    # ejercicio_49
    def obtener_notas_por_estudiante_ordenadas_por_asignatura(estudiante_id):
        notas = GradeDetail.objects.filter(student_id=estudiante_id).order_by('grade__subject__name')
        print(notas)
    # obtener_notas_por_estudiante_ordenadas_por_asignatura(1)

    # ejercicio_50
    def actualizar_nota1():
        GradeDetail.objects.filter(score1__lt=20).update(score1=20)
    # actualizar_nota1()

    # ejercicio_51
    def actualizar_nota2():
        GradeDetail.objects.filter(score2__lt=15).update(score2=15)
    # actualizar_nota2()

    # ejercicio_52
    def actualizar_extension():
        GradeDetail.objects.filter(extension__lt=10).update(extension=10)
    # actualizar_extension()

    # ejercicio_53
    def actualizar_observacion_aprobados():
        GradeDetail.objects.filter(score1__gte=50).update(observacion="Aprobado")
    # actualizar_observacion_aprobados()

    # ejercicio_54
    def actualizar_notas_por_periodo(periodo_id, nueva_nota):
        GradeDetail.objects.filter(grade__period_id=periodo_id).update(score1=nueva_nota, score2=nueva_nota, extension=nueva_nota)
    # actualizar_notas_por_periodo(1, 50)

    # ejercicio_55
    def eliminar_notas_por_estudiante(estudiante_id):
        GradeDetail.objects.filter(student_id=estudiante_id).delete()
    # eliminar_notas_por_estudiante(1)

    # ejercicio_56
    def eliminar_logicamente_notas_por_estudiante(estudiante_id):
        GradeDetail.objects.filter(student_id=estudiante_id).update(state='inactive')
    # eliminar_logicamente_notas_por_estudiante(1)

    # ejercicio_57
    def eliminar_notas_por_periodo(periodo_id):
        GradeDetail.objects.filter(grade__period_id=periodo_id).delete()
    # eliminar_notas_por_periodo(1)

    # ejercicio_58
    def eliminar_logicamente_notas_por_periodo(periodo_id):
        GradeDetail.objects.filter(grade__period_id=periodo_id).update(state='inactive')
    # eliminar_logicamente_notas_por_periodo(1)

    # ejercicio_59
    def eliminar_notas_con_nota1_menor_10():
        GradeDetail.objects.filter(score1__lt=10).delete()
    # eliminar_notas_con_nota1_menor_10()

    # ejercicio_60
    def crear_nota(estudiante_id, periodo_id, profesor_id, asignatura_id, score1, score2, extension):
        user = User.objects.get(id=1)
        estudiante = Student.objects.get(id=estudiante_id)
        periodo = Period.objects.get(id=periodo_id)
        profesor = Professor.objects.get(id=profesor_id)
        asignatura = Subject.objects.get(id=asignatura_id)

        grade = Grade.objects.create(
            user=user,
            period=periodo,
            subject=asignatura,
            professor=profesor
        )

        GradeDetail.objects.create(
            user=user,
            grade=grade,
            student=estudiante,
            score1=score1,
            score2=score2,
            extension=extension
        )
# crear_nota(1, 1, 1, 1, 9.0, 8.5, 7.0)