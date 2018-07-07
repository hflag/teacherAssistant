from django.db import models


# Create your models here.
class Schedule(models.Model):
    teacher_name = models.CharField(max_length=50, verbose_name="教师名字")
    course_name = models.CharField(max_length=100, verbose_name="课程名字")
    class_name = models.CharField(max_length=100, verbose_name="班级名字")
    room_name = models.CharField(max_length=100, verbose_name="教室名")
    week = models.CharField(max_length=10, verbose_name="星期几")
    order = models.CharField(max_length=5, verbose_name="第几节")

    class Meta:
        index_together = ['week', 'order']

    def __str__(self):
        return "{}的{}，{}主讲".format(self.class_name, self.course_name, self.teacher_name)


class Customer(models.Model):
    c_name = models.CharField(max_length=50)
    c_tel = models.CharField(max_length=20)
    c_email= models.EmailField()
    messages = models.TextField()
    is_finished = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.c_name