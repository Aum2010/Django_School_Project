from django.db import models

# Create your models here.
class ExamScore(models.Model):

    allsubject = (
            ('Math','คณิตศาสตร์'),
            ('Sci','วิทยาศาสตร์'),
            ('Art','ศิลปะ'),
            ('Music','ดนตรี'),
            ('Physics','ฟิสิกส์'),
        )

    subject = models.CharField(max_length=50 , choices=allsubject , default='math')
    student_name = models.CharField(max_length=50)
    student_last = models.CharField(max_length=50)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.student_name} {self.student_last} {self.subject} : {str(self.score)}'
    

    

