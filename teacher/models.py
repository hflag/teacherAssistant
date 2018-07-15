from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Banji(models.Model):
    name = models.CharField(max_length=100, verbose_name='班级名')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    banji = models.ForeignKey(Banji, on_delete=models.CASCADE)
    # act = models.ForeignKey(Act, on_delete=models.CASCADE, null=True, blank=True)
    No = models.CharField(max_length=10, verbose_name='学号')
    name = models.CharField(max_length=20, verbose_name='姓名')
    sex = models.CharField(max_length=4, verbose_name='性别')

    def __str__(self):
        return self.name


class Act(models.Model):
    # student = models.ManyToManyField(Student, related_name='joined_act', blank=True)
    banji = models.ForeignKey(Banji, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, verbose_name='活动题目')
    # score = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name='开展时间')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title


class StudentActScore(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    act = models.ForeignKey(Act, on_delete=models.CASCADE)
    score = models.FloatField(default=0)


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='课程名')
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name='课程封面图')

    def __str__(self):
        return self.name


class Schedule(models.Model):
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                verbose_name='任课教师',
                                null=True, blank=True)
    banji = models.ForeignKey(Banji, on_delete=models.CASCADE, verbose_name='班级', null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    room_name = models.CharField(max_length=100, verbose_name="教室名")
    week = models.CharField(max_length=10, verbose_name="星期几")
    order = models.CharField(max_length=5, verbose_name="第几节")

    class Meta:
        index_together = ['week', 'order']

    def __str__(self):
        return "{}的{}，{}主讲".format(self.banji.name, self.course.name, self.teacher.username)


class Customer(models.Model):
    c_name = models.CharField(max_length=50)
    c_tel = models.CharField(max_length=20)
    c_email = models.EmailField()
    messages = models.TextField()
    is_finished = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.c_name