from django.db import models
from django.contrib.auth.models import User


class ModelBase(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField('Fecha de Creación', auto_now_add=True)
    updated = models.DateTimeField('Fecha de modificación', auto_now=True)
    state = models.BooleanField('Estado', default=True)

    class Meta:
        abstract = True
    
    def delete(self, *args, **kwargs):
        self.state = False
        self.save()


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(state=True)


class Period(ModelBase):
    name = models.CharField(max_length=50)

    objects = models.Manager()
    active_objects = ActiveManager()

    def __str__(self):
        return self.name
    

class Subject(ModelBase):
    name = models.CharField(max_length=100)

    objects = models.Manager()
    active_objects = ActiveManager()

    def __str__(self):
        return self.name
    


class Professor(ModelBase):
    identification = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    objects = models.Manager()
    active_objects = ActiveManager()

    def __str__(self):
        return self.name
    
class Student(ModelBase):
    identification = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    objects = models.Manager()
    active_objects = ActiveManager()

    def __str__(self):
       return self.name
    

class Grade(ModelBase):
    period = models.ForeignKey(Period, on_delete=models.PROTECT, related_name='grades')
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, related_name='grades')
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT, related_name='grades')

    objects = models.Manager()
    active_objects = ActiveManager()

    def __str__(self):
        return f'{self.subject} - {self.professor}'
    
class GradeDetail(ModelBase):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='gradedetails')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    score1 = models.DecimalField(max_digits=5, decimal_places=2)
    score2 = models.DecimalField(max_digits=5, decimal_places=2)
    extension = models.DecimalField(max_digits=5, decimal_places=2)
    observation = models.CharField(max_length=100)

    objects = models.Manager()
    active_objects = ActiveManager()

    def __str__(self):
        return f'{self.student}: {self.score1} - {self.score2}'
    